class Library:
    def __init__(self):
        self._books=["Python Basics","Data Science 101","AI for beginners"]
        self.__password="admin123"
    def show_books(self):
        print("Books available",self._books)

    def add_book(self,book_name,password):
        if password ==self.__password:
            self._books.append(book_name)
            print(f"Book {book_name} added successfully")

        else:
            print("Access denied! Wrong Password.")

lib=Library()
lib.show_books()
lib.add_book("Machine Learning","admin123")
lib.add_book("Java","wrongpass")

    


        