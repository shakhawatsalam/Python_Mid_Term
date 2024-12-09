class Library :
    book_list = []
    
    # Add book
    def entry_book(self, book_id ,title ,author, availability):
        self.book_list.append({'ID': book_id, 'Title': title, 'Author': author, 'Availability': availability})
    
    
class Book(Library):
    def __init__(self, book_id ,title ,author, availability):
        self.__book_id = book_id
        self._title = title
        self._author = author
        self.__availability = availability
        super().entry_book(self.__book_id ,self._title ,self._author, self.__availability)
    
    # Borrow a book 
    @classmethod  
    def borrow_book(self, id):
        for x in self.book_list:
            if x["ID"] == id and x['Availability'] == True:
                x['Availability'] = False
                print(f"Book : {x['Title']} borrowed successfully")
                return
            elif x["ID"] == id and x['Availability'] == False:
                print('This book is borrowed already! Not Available')
                return
         
        print('Invalid book ID')
    # Return the book  
    @classmethod  
    def return_book(self, id):
        for x in self.book_list:
            if x["ID"] == id and x['Availability'] == False:
                x['Availability'] = True
                print(f"Book : {x['Title']} returned successfully")
                return
         
        print('Invalid Book ID !!!')
    # View Book Info
    @classmethod    
    def view_book_info(self, id):
          for x in self.book_list:
            if x["ID"] == id :
                print(x)
                return
         
          print('Book not found')
    @classmethod
    def view_all_book(self) -> None:
          for x in self.book_list:
                print(x)
          
                   
               
        
    
        
        
  
book1 = Book(101, 'Learn JavScript the Easy Way', 'Jane Doe', True)
book2 = Book(102, 'C and C++ Easy Way', 'John Smith', True)
book3 = Book(103, 'Mastering Problem Solving', 'Alice Brown', True)
book4 = Book(104, 'Python Basics: With Database', 'Chris Johnson', True)
book5 = Book(105, 'Introduction to Python Coding', 'David Clark', True)





while True:
    print("----------Welcome to the Library----------")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. View Book Info")
    print("5. Exit")
    
    user_input = int(input('Enter you Choice: '))
    if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input != 5:
        print("Invalid Menu Option! Chose Option Carefully")
    if user_input == 1:
        Book.view_all_book()
    elif user_input == 2 :
        book_id = int(input('Enter book ID to borrow: '))
        Book.borrow_book(book_id)
    elif user_input == 3 :
        book_id = int(input('Enter book ID to return: '))
        Book.return_book(book_id)
    elif user_input == 4 :
        book_id = int(input('Enter book ID See Book Info: '))
        Book.view_book_info(book_id)
    elif user_input == 5 :
        break
      