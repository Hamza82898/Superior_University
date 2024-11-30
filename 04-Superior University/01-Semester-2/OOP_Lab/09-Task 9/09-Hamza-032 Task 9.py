import os

class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book(Document):
    def __init__(self, title, author, genre = None, pages = None):
        super().__init__(title, author)
        self.genre = genre or "Unknown"
        self.pages = pages or 0

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")

class Article(Document):
    def __init__(self, title, author, journal = None, doi = None):
        super().__init__(title, author)
        self.journal = journal or "Unknown"
        self.doi = doi or "Unknown"

    def display_info(self):
        super().display_info()
        print(f"Journal: {self.journal}")
        print(f"DOI: {self.doi}")    

def save_books(books, filename = "books.txt"):
    with open(filename, "w") as file:
        for book in books:
            file.write(f"{book.title},{book.author},{book.genre},{book.pages}\n")

def read_books(filename = "books.txt"):
    books = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title, author, genre, pages = line.strip().split(",")
                books.append(Book(title, author, genre, int(pages)))
    return books 

def save_article(articles, filename = "articles.txt"):
    with open(filename, "w") as file:
        for article in articles:
            file.write(f"{article.title},{article.author},{article.journal},{article.doi}\n")

def read_article(filename = "articles.txt"):
    articles = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                title, author, journal, DOI = line.strip().split(",")
                articles.append(Article(title, author, journal, DOI))
    return articles

if __name__ == "__main__":
    book1 = Book("Pride and Prejudice","Jane Austen","Fiction",376)
    book2 = Book("The Book Thief","Markus Zusak","Historical Fiction",584)
    article1 = Article("Judical Branck","History","Judical","9.890/abdf")
    article2 = Article("The Impact of Climate Change","Jane Smith","Environmental Studies","10.1234")

    save_books([book1,book2])
    save_article([article1,article2])

    read_books_list = read_books()
    read_articles_list = read_article()

    print("\nLoad Book")
    for book in read_books_list:
        book.display_info()

    print("Load Article")
    for article in read_articles_list:
        article.display_info()                                                     

                    