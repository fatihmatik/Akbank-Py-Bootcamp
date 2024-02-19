import time

class Library:
    def __init__(self) -> None:
        self.file_path = "books.txt"
        self.file = open(file=self.file_path, mode="a+")


    def list_books(self):
        self.file.seek(0)  # Move cursor to the beginning of the file
        book_lines = self.file.read().split("\n")
        for book_line in book_lines:
            book_info = book_line.split(",")

            if book_info != [""]: # An empty line is equal to [""], after the operations we have done
                print(f"Book Name: {book_info[0]}, Author: {book_info[1]}")
            else: pass


    def add_book(self):
        try:
            book_name = str(input("Enter the book name: "))
            author = str(input("Enter the author of the book: "))
            year = int(input("Enter the publishment year: "))
            numberOfPages = int(input("Enter the number of pages: "))
            book_info = f"\n{book_name}, {author}, {year}, {numberOfPages}"
            self.file.write(book_info)
            print(f"Book succesfully added to the library!")
        except Exception as e:
            print(f"An error occured as: {e}")


    def remove_book(self):
        title = str(input("Enter the name of the book you'd like to delete: "))
        self.file.seek(0)  # Move cursor to the beginning of the file
        book_lines = self.file.read().split("\n")
        
        indexToDelete = None

        for itr, book_info in enumerate(book_lines):
            parts = book_info.split(",")
            if title == parts[0]:
                indexToDelete = itr
                break
            else: pass
        
        if indexToDelete is not None:
            book_lines.pop(indexToDelete)
            self.file = open(file=self.file_path, mode="w") # make the file mode "w" so we can overwrite the entire file
            
            for itr in range(0,len(book_lines),1):
                self.file.write(book_lines[itr] + "\n")
            print(f"The book {title} deleted succesfully.")

            self.file = open(file=self.file_path, mode="a+") # Revert the file mode back to a+
        else: print("The name wasn't in the library.")


if __name__ == "__main__":
    while True:
        lib = Library() # Creating the our object of the Library class.
        
        menu_string = """\n\n*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book""" 
        print(menu_string) # Printing out the choice menu.
        
        user_input = str(input("Enter your command as 1,2,3 or q for quitting:\n")) # Taking the user input.

        if user_input == "1":
            lib.list_books()
        elif user_input == "2":
            lib.add_book()
        elif user_input == "3":
            lib.remove_book()
        elif user_input == "q":
            exit()
        else: print("Try entering the given characters!")
    
        time.sleep(1)


