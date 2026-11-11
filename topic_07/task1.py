class Book:

    def __init__(self, title, author, year):
        self.title = title     
        self.author = author
        self.year = year


    def __str__(self):
        return f'Книга: "{self.title}" | Автор: {self.author} ({self.year} р.)'


if __name__ == "__main__":
    book1 = Book("Кобзар", "Тарас Шевченко", 1840)
    book2 = Book("Місто", "Валер'ян Підмогильний", 1928)


    print(book1)
    print(book2)