class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f'{self.title} - Author:{self.author} ({self.year})'

class BookManager:

    def __init__(self):
        self.bookstock = []

    def book_add(self,title,author,year):
        print(f'Book added !')
        new_book = Book(title,author,year)
        return self.bookstock.append(new_book)
    
    def book_list(self):
        if not self.bookstock:
            print("There is no book")
        else:
            print("there is book list:")
            for b in self.bookstock:
                print(b)

    def searching(self, keyword):
        found = False 
        for b in self.bookstock:
            if b.title == keyword:
                print("Your book is in stock!")
                found = True
                break  
        if not found:
            print("Sorry, we don't have this type of book")


class UserInterface:
    def __init__(self):
        self.manager = BookManager()

    def run(self):
        while True:
            print("========== BOOK SYSTEM ==========")
            print("1. Add book")
            print("2. Show all books")
            print("3. Search book")
            print("4. Exit")
            choice = input("Choose option: ")

            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                while True:
                    year_input = input("Year: ")

                    try:
                        year = int(year_input)

                        if year < 0:
                            print("Year cannot be negative!")
                        elif year > 2025:
                            print("Year greater than current period, please try again.")
                        elif len(year_input) != 4:
                            print("Year must be 4 digits.")
                        else:
                            break

                    except ValueError:
                        print("Please enter numbers only!")

                self.manager.book_add(title, author, year)

            elif choice == "2":
                self.manager.book_list()

            elif choice == "3":
                keyword = input("Search by exact title: ")
                self.manager.searching(keyword) 

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option, try again.")


user = UserInterface()
user.run()
