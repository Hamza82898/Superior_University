class Item:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title : {self.title}  \nAuthor : {self.author}"

class Book(Item):
    def __init__(self, title, author,pages):
        super().__init__(title, author)
        self.pages = pages

    def additional_info(self):
        return f"Pages : {self.pages}"

class Magazine(Item):
    def __init__(self, title, author,issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def additional_info(self):
        return f"Issue Number : {self.issue_number}"


book = Book("Pride and Prejudice","Jane Austen",273)
magazine = Magazine("Earth Chronicles","Zecharia Sitchin",119900)

print(book.display_info())
print(book.additional_info())
print(magazine.display_info())
print(magazine.additional_info())


