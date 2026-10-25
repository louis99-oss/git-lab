from zad_1 import Student


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: {self.street}, {self.zip_code} {self.city}, godziny otwarcia: {self.open_hours}, tel: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Pracownik: {self.first_name} {self.last_name}, ur. {self.birth_date}, zatrudniony: {self.hire_date}, "
                f"adres: {self.street}, {self.zip_code} {self.city}, tel: {self.phone}")


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Książka: {self.author_name} {self.author_surname}, wydana {self.publication_date}, "
                f"{self.number_of_pages} stron\n    {self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        text = f"Zamówienie z dnia {self.order_date}\n  {self.employee}\n  {self.student}\n  Książki:"
        for book in self.books:
            text += f"\n  - {book}"
        return text


if __name__ == "__main__":
    library1 = Library("Kraków", "Rajska 1", "31-124", "8:00-20:00", "123456789")
    library2 = Library("Warszawa", "Koszykowa 26", "00-553", "9:00-18:00", "222333444")

    employee1 = Employee("Anna", "Nowak", "2020-03-01", "1990-05-12", "Kraków", "Długa 5", "31-147", "987654321")
    employee2 = Employee("Piotr", "Kowalski", "2018-09-15", "1985-11-02", "Kraków", "Wawelska 10", "30-001", "600700800")
    employee3 = Employee("Kasia", "Wiśniewska", "2022-01-10", "1998-02-20", "Warszawa", "Marszałkowska 3", "00-001", "511222333")

    student1 = Student("John", [60, 70, 80])
    student2 = Student("Alice", [40, 50, 60])
    student3 = Student("Tomek", [90, 85, 70])

    book1 = Book(library1, "1997-06-26", "J.K.", "Rowling", 320)
    book2 = Book(library1, "1954-07-29", "J.R.R.", "Tolkien", 423)
    book3 = Book(library1, "1949-06-08", "George", "Orwell", 328)
    book4 = Book(library2, "1834-06-28", "Adam", "Mickiewicz", 340)
    book5 = Book(library2, "1993-01-01", "Andrzej", "Sapkowski", 288)

    order1 = Order(employee1, student1, [book1, book2, book3], "2026-10-20")
    order2 = Order(employee3, student3, [book4, book5], "2026-10-25")

    print(order1)
    print()
    print(order2)
