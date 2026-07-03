# Simple Library Management System

books = [
    {'id': 101, 'title': 'Python Basics', 'author': 'Sumita Arora', 'issued': False},
    {'id': 102, 'title': 'Data Structures using Python', 'author': 'Narasimha Karumanchi', 'issued': True},
    {'id': 103, 'title': 'Computer Networks', 'author': 'Andrew Tanenbaum', 'issued': False},
    {'id': 104, 'title': 'AI Foundations in Python', 'author': 'Stuart Russell', 'issued': True},
    {'id': 105, 'title': 'Machine Learning', 'author': 'Tom Mitchell', 'issued': False}
]

# 1. Display all book records

def Display ():
    for i in books:
        return i
 
# 2. Search book by ID

def search_book(book_id):
    for i in books:
       if i['id'] == book_id:
          print(i)
          return i
    return None

# 3. Issue book
    
def issue_book(book_id):
    book = search_book(book_id)
    
    if book['issued'] == False:
            book['issued'] = True
            print("Book issued successfully.")
    else:
        print("Book is already issued.")
    
# 4. Return book

def return_book(book_id):
    book = search_book(book_id)
    
    if book['issued'] == True:
            book['issued'] = False
            print("Book returned successfully.")
    else:
            print("Book was not issued.")
    
# 5. List available books

def list_available_books():
    for i in books:
        if i['issued']== False:
            print(i)

# 6. Display all book titles by a specific author   

def books_by_author(author_name):
    for i in books:
        if i['author'] == author_name:
            print(i['title'])
        
# 7. Count books by issue status

#def count_books_by_status(status):
      
      



# 8. Display books containing the word "Python"

def books_with_python():
    for i in books:
        if 'Python' in i['title']:
            print(i['title'])

# 9. Menu-driven 

def menu():
    while True:
        print("===== Library Menu =====")
        print("1. Display all books")
        print("2. Search book by ID")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. List available books")
        print("6. Show books by author")
        print("7. Count books by issue status")
        print("8. Show books with 'Python' in title")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Display()
        elif choice == '2':
            search_book(int(input("Enter Book ID to search: ")))
        elif choice == '3':
            issue_book(int(input("Enter Book ID to issue: ")))
        elif choice == '4':
            return_book(int(input("Enter Book ID to return: ")))
        elif choice == '5':
            list_available_books()
        elif choice == '6':
            books_by_author(input("Enter author name: "))
        #elif choice == '7':
            #count_books_by_status(input("Enter status (True for issued / False for available): "))
        elif choice == '8':
            books_with_python()
        elif choice == '9':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")    
menu()            













             
    