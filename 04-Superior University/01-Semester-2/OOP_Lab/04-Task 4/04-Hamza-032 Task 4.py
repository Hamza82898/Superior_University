class Book:
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year

    def __str__(self):
        return f"Title:{self.title} Author:{self.author} Publication_year:{self.publication_year}"
    
book1 = Book("Macbeth","William Shakespeare",1623)
print(book1)    

        