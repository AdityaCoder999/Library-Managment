class Library:
    def __init__(self, list, name):
        self.books = list
        self.lib_name = name
        self.lend_book = {}
    
    def display(self):
        i = 1
        for item in self.books:
            print(f"{i}. {item}\n")
            i = i + 1
    
    def lend(self, book, name):
        if book not in self.lend_book.keys():
            self.lend_book.update({book:name})
            print("Now you can take this book")
        else:
            print(f"The book {book} is not available in our library. Please try anywhere else")

    def add(self, book):
        self.books.append = book
        print("Your book is successfully added in our library")

    def rem(self, book):
        self.books.remove(book)



aditya = Library(["Harry Potter", "Alice in the wonderland", "Wings of fire", "Unity in diversity", "Cpp"], "Ak Library")

if __name__ == '__main__':
    print(f"Welcome to {aditya.lib_name} Library")

    while True:
        print("Enter what do you want to do below are the options: ")
        print('''1 - TO DISPLAY ALL BOOKS
        2 - TO LEND A BOOK
        3 - TO DONATE A BOOK
        4 - TO RETURN A BOOK: \n
        and enter q to quit''')
        user_input = input()

        if user_input == "1":
            aditya.display()
        elif user_input == "2":
            user_book = input("Enter which book you want to lend:- ")
            user_name = input("Enter Your name :- ")
            aditya.lend(user_book, user_name)
        elif user_input == "3":
            user_book = input("Enter which book you want to lend:- ")
            aditya.add(user_book)
        elif user_input == "4":
            user_book = input("Enter which book you want to lend:- ")
            aditya.rem(user_book)
        elif user_input == "q":
            break
        else : 
            continue




            


        

