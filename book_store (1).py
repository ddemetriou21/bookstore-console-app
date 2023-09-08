import json

users = {}

class Book:
    def __init__(self, ISBN, title, author, price, genre, overview):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre
        self.overview = overview 

    def book_information():
        while True: 
            info_request = input('\nEnter book title to view info [C to cancel]:  ')
            if info_request.lower() == 'c':
                break
            book_data = load_books_data()
            found_book = None
            
            for book_id, book_info in book_data.items():
                if info_request.lower() == book_info['title'].lower():
                    found_book = book_info
                    break

            if found_book:
                print(f'\nBook: {found_book["title"]} \nAuthor: {found_book["author"]} \nGenre: {found_book["genre"]} \nPrice: {found_book["price"]} \nISBN: {found_book["ISBN"]}')
                print(f'Overview: {found_book["overview"]}')
                more_info = input("\nWould you like to view another book's information? [Y/N]: ")
                if more_info.lower() == 'y':
                    info_request
                elif more_info.lower() == 'n':
                    break
                else:
                    print('Invalid option.')
            else:
                print('Book not found.')

class Shopping_Basket:
    def __init__(self):
        # Initialize an empty shopping basket
        self.books_in_basket = []

    def add_book(self, book):
        # Add a book to the shopping basket
        self.books_in_basket.append(book)

    def remove_book(self, book):
        # Remove a book from the shopping basket
        for basket_book in self.books_in_basket:
            if basket_book.ISBN == book.ISBN:
                self.books_in_basket.remove(basket_book)
                return
        else:
            print("Book not found in the shopping basket.")

    def view_basket(self, book_data):
    # View and interact with the books in the shopping basket
        while True:
            if not self.books_in_basket:
                print("\nShopping basket is empty.")
            else:
                print("\nBooks in shopping basket:\n")
                for index, book in enumerate(self.books_in_basket, start=1):
                    print(f"{index}: {book.title} by {book.author}")

            print("\nPlease select an option:\n \n[1] Add a book \n[2] Remove a book \n[3] Main Menu")
            choice = input("\nEnter your choice: ")

            if choice == '1':
                book_title = input("\nEnter the book title to add to your cart (or C to cancel): ").lower()
                if book_title == 'c':
                    print("\nCancelled adding a book to your cart.")
                else:
                    selected_book = None
                    for book_info in book_data.values():
                        if book_title == book_info['title'].lower():
                            selected_book = Book(book_info['ISBN'], book_info['title'], book_info['author'], book_info['price'], book_info['genre'], book_info['overview'])
                            break

                    if selected_book:
                        self.add_book(selected_book)
                        print(f"\n{selected_book.title} added to your cart.")
                    else:
                        print("\nBook not found.")
            elif choice == '2':
                book_title = input("\nEnter the book title to remove from your cart (or C to cancel): ").lower()
                if book_title == 'c':
                    print("\nCancelled removal from cart.")
                else:
                    selected_book = None
                    for book_info in book_data.values():
                        if book_title == book_info['title'].lower():
                            selected_book = Book(book_info['ISBN'], book_info['title'], book_info['author'], book_info['price'], book_info['genre'], book_info['overview'])
                            break

                    if selected_book:
                        self.remove_book(selected_book)
                        print(f"\n{selected_book.title} removed from your cart.")
                    else:
                        print("\nBook not found.")
            elif choice == '3':
                break
            else:
                print("\nInvalid choice. Please select a valid option.")

class User:
    def __init__(self, username, name, password, email):
        self.username = username
        self.name = name
        self.password = password
        self.email = email 
        self.shopping_basket = Shopping_Basket()
        self.order_history = []

    def create_user(users):
        email = input('Enter an email: ')
        for user in users.values():
            if user.email == email:
                print('This email is already registered with an account.')
                return None  # Return None to indicate that the user creation failed

        username = input('Enter a username: ')
        name = input('Enter your full name: ')
        password = input('Enter a password: ')
        user = User(username, name, password, email)
        users[username] = user
        print('\nUser creation successful.')
        return user

    def login(users):
        login_attempts = 0
        while True:
            email = input('\nEnter your email: ')
            password = input('Enter your password: ')
            user = users.get(email)
            if user and user.password == password:
                print('\nLogin successful.')
                return user, login_attempts
            else:
                print('\nLogin unsuccessful. Check for spelling errors.')
                login_attempts += 1
                if login_attempts == 3:
                    print('\nLogin failed. Check spelling or log in as guest.')
                    return None, login_attempts

    def edit(self):
        print(f"\nEditing User: {self.username}, Name: {self.name}, Email: {self.email}")
        edit_choice = input("\nWhat would you like to edit?\n \n[1] Name \n[2] Email \n[3] Password \n[4] All\n \nEnter your choice: ").lower()
        if edit_choice =='1':
            self.name = input(f"\nUpdating name from ({self.name}) to: ")
        elif edit_choice == '2':
            self.email = input(f'\nUpdating email from ({self.email}) to: ')
        elif edit_choice == '3':
            self.password = input(f'\nEnter updated password: ')   
        elif edit_choice == '4':
                self.edit_all_details()
        else:
            print("\nInvalid choice.")

    def edit_all_details(self):
        self.name = input(f"\nUpdating name from ({self.name}) to: ")
        self.email = input(f'\nUpdating email from ({self.email}) to: ')
        self.password = input(f'\nEnter updated password: ')

    def view_details(self):
        print(f'\nAccount details for {self.username}: \nName: {self.name} \nEmail: {self.email}')

    def view_orders(self):  
            if not self.order_history:
                print("\nNo order history available.")
            else:
                print("\nOrder History:")
                for order in self.order_history:
                    # Display order details as needed
                    print(order)

    def checkout(self):
        if not self.shopping_basket.books_in_basket:
            print("\nShopping basket is empty. Add books to your basket before checkout.")
        else:
            total_price = sum(book.price for book in self.shopping_basket.books_in_basket)
            print("\nOrder Summary:\n")
            for index, book in enumerate(self.shopping_basket.books_in_basket, start=1):
                # Display book details as needed
                print(f"[{index}]Book: {book.title}, Price: {book.price}")
            print(f"\nTotal Price: {total_price}")
            confirm_checkout = input("\nConfirm checkout? [Y/N]: ")
            if confirm_checkout.lower() == 'y':
                # Add the current shopping basket to order history and clear the basket
                self.order_history.append(self.shopping_basket.books_in_basket)
                self.shopping_basket.books_in_basket = []
                print("\nCheckout successful. Order added to order history.")
            else:
                print("\nCheckout canceled.")
 
    @classmethod
    def from_dict(cls, users_dict):
        username = users_dict['username']
        name = users_dict['name']
        password = users_dict['password']
        email = users_dict['email']
        user = cls(username, name, password, email)
        return user
 
def list_all_books():
    book_data = load_books_data()
    
    if not book_data:
        print("\nNo books found.")
    else:
        for index, (book_id, book_info) in enumerate(book_data.items(), start=1):
            print(f"\n[{index}] Title: {book_info['title']}")
            print(f"    Author: {book_info['author']}")
            print(f"    Price: {book_info['price']}")
            print('----------------------------')

def search_book(current_user=None):  
    user_input = input("\nSearch books by author or ISBN number: ")
    book_data = load_books_data()
    found_books = []

    for book_id, book_info in book_data.items():
        if user_input.lower() in book_info['author'].lower() or user_input == book_info['ISBN']:
            found_book = Book(book_info['ISBN'], book_info['title'], book_info['author'], book_info['price'], book_info['genre'], book_info['overview'])
            found_books.append(found_book)

    if not found_books:
        print("\nBook not found.")
    else:
        for i, book in enumerate(found_books, 1):
            print(f"\n[{i}] Book: {book.title}, Author: {book.author}, ISBN: {book.ISBN}")
            
def load_books_data():
    try:
        with open('books_data.json', 'r') as file:
            data = json.load(file)
        return data 
    except FileNotFoundError:
        print("File 'books_data.json' not found.")
        return {} 

def user_menu(current_user):
    book_data = load_books_data()
    while True:
        print(f"\n--------------\n| Book Store |\n-------------- \n \nLogged in as: {current_user.username}")
        print("\nPlease select an option:\n \n[1] Search for a book \n[2] View all books available \n[3] Book information \n[4] View Shopping Cart")
        print('[5] View Order history \n[6] View account details \n[7] Checkout \n[8] Logout')
        user_input = input('\nEnter your choice: ')
        if user_input == '1':
            search_book(current_user)
        elif user_input == '2':
            list_all_books()
        elif user_input == '3':
            Book.book_information()
        elif user_input == '4':
            current_user.shopping_basket.view_basket(book_data)
        elif user_input == '5':
            current_user.view_orders()
        elif user_input == '6':
            choice = input('\nSelect one of the following options:\n \n[1] View account details \n[2] Manage account details\n \nEnter your choice: ')
            if choice == '1':
                User.view_details(current_user)
            elif choice == '2':
                User.edit(current_user)
            else:
                print('\nInvalid option.')
        elif user_input == '7':
            current_user.checkout()
        elif user_input == '8':
            print('\nLogging out.')
            break
        else:
            print('\nInvalid choice. Please select one of the options provided.')

def guest_menu():
    while True:
        print("\n--------------\n| Book Store |\n-------------- \n\nLogged in as: Guest")
        print("\nPlease select an option:\n \n[1] Search for a book \n[2] View all books available \n[3] Book information \n[4] Logout")
        user_input = input('\nEnter your choice: ')
        if user_input == '1':
            search_book()
        elif user_input == '2':
            list_all_books()
        elif user_input == '3':
            Book.book_information()
        elif user_input == '4':
            print('\nLogging out.')
            break
        else:
            print('\nInvalid choice. Please select one of the options provided.')

def main():
    while True: 
        print("\n--------------\n| Book Store |\n--------------")
        print('\nPlease select an option:\n \n[1] Login \n[2] Register \n[3] Exit\n')
        user_login = input("Enter your choice: ")
        if user_login == '1':
            while True:
                user_choice = input('\n[1] Login with registered account \n[2] Login with guest account\n[3] Return to main menu\n \nEnter your choice: ')
                if user_choice == '1':
                    current_user, login_attempts = User.login(users)
                    if current_user:
                        user_menu(current_user)
                    elif login_attempts == 3:
                        continue
                elif user_choice == '2':
                    guest_menu()
                elif user_choice == '3':
                    break
                else:
                    print('\nInvalid choice.')
        elif user_login == '2': 
            User.create_user(users)
        elif user_login == '3':
            print('\nGoodbye!')
            break
        else: 
            print('\nInvalid choice.')

if __name__ == '__main__':
    main()

# fix email verification method, where program checks to see if email is already in stored data (DONE) keep it in loop if email exists
# fix order history to be saved with the current user and showing the correct books. not the book object location
# add file handling for user data
# add encapsulation for user info 
# add multithreading 
# add cancellation to few options to return to main menu. (DONE)
# when viewing shopping cart when empty, show menu where you can add/remove items. (DONE)
# registered/unregistered user class?
