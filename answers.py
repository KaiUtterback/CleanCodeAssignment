# Building a Modular Online Bookstore System
'''
Objective:
 The objective of this assignment is to create a modular online bookstore system using Python.
 The focus will be on applying the principle of modularity to enhance code organization, maintainability, and scalability.
 The system will be broken down into different modules, each handling specific funcitonalities of the bookstore.

Task:
 Create a module for managing book-realted functionalities. 
 This includes classes and functions for book attributes, book availability, and any other book-specific operations.

Problem Statement:
 The bookstore system requires a dedicated module for handling various aspects related to books, such as title, author, price, and stock status.

Expected Outcome:
 A main.py module that effectively integrates the book, user, and cart modules, allowing for a smooth and modular operation of the online bookstore system. 
 The integration should highlight the benefits of modularity in software design.

'''

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def update_stock(self, count):
        self.stock += count

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Stock: {self.stock}"

def search_by_title(books, title):
    title = title.lower()
    for book in books:
        if book.title.lower() == title:
            return book
    return None

def search_by_author(books, author):
    author = author.lower()
    results = [book for book in books if book.author.lower() == author]
    return results

def display_all_books(books):
    if not books:
        print("No books available.")
    for book in books:
        print(book.display_info())

class Cart:
    def __init__(self):
        self.items = {}

    def add_book(self, book, quantity):
        if book in self.items:
            self.items[book] += quantity
        else:
            self.items[book] = quantity

    def remove_book(self, book, quantity):
        if book in self.items:
            self.items[book] -= quantity
            if self.items[book] <= 0:
                del self.items[book]

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        total_cost = 0
        print("Your cart contains:")
        for book, quantity in self.items.items():
            print(f"{book.title} - {quantity} book(s) at ${book.price:.2f} each")
            total_cost += book.price * quantity
        print(f"Total cost: ${total_cost:.2f}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def authenticate(username, password, user_db):
        return user_db.get(username) == password

    def update_password(self, new_password):
        self.password = new_password

user_db = {
    "admin": "admin123",
    "user1": "password1"
}



def main():
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99, 5),
        Book("War and Peace", "Leo Tolstoy", 19.99, 10),
        Book("Ulysses", "James Joyce", 12.99, 2)
    ]
    cart = Cart()
    current_user = None

    while True:
        print("Please log in to continue.")
        username = input("Username: ")
        password = input("Password: ")
        if User.authenticate(username, password, user_db):
            current_user = User(username, password)
            print("Login successful.")
            break
        else:
            print("Login failed. Please try again.")

    while True:
        print("\n--- Bookstore Menu ---")
        print("1. Search for a book by title")
        print("2. Search for books by author")
        print("3. Display all books")
        print("4. View cart")
        print("5. Add book to cart")
        print("6. Remove book from cart")
        print("7. Change password")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            book = search_by_title(books, title)
            if book:
                print("Book found:", book.display_info())
            else:
                print("Book not found.")
        
        elif choice == '2':
            author = input("Enter the author's name: ")
            author_books = search_by_author(books, author)
            if author_books:
                print("Books found:")
                for book in author_books:
                    print(book.display_info())
            else:
                print("No books found by this author.")
        
        elif choice == '3':
            display_all_books(books)
        
        elif choice == '4':
            cart.display_cart()
        
        elif choice == '5':
            title = input("Enter the title of the book to add to your cart: ")
            quantity = int(input("Enter the quantity: "))
            book = search_by_title(books, title)
            if book and quantity <= book.stock:
                cart.add_book(book, quantity)
                book.update_stock(-quantity)
                print("Book added to cart.")
            else:
                print("Book not found or insufficient stock.")
        
        elif choice == '6':
            title = input("Enter the title of the book to remove from your cart: ")
            quantity = int(input("Enter the quantity to remove: "))
            book = search_by_title(books, title)
            if book:
                cart.remove_book(book, quantity)
                book.update_stock(quantity)
                print("Book removed from cart.")
            else:
                print("Book not found in cart.")
        
        elif choice == '7':
            new_password = input("Enter your new password: ")
            current_user.update_password(new_password)
            user_db[username] = new_password
            print("Password updated successfully.")
        
        elif choice == '8':
            print("Exiting the bookstore system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

main()
print()

'''2. Refactoring a Weather Forecast Application into Classes and Modules 

Objective:
 The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. 
 The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

Task 1: Identifying and Creating Classes
 Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. 
 Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

Problem Statement:
 The existing script for the weather forecast application is written in a procedural style and lacks organization.

Expected Outcome:
A main.py script that demonstrates how the different modules and classes come together to form a fully functional weather forecast application. 
The script should exemplify the benefits of using OOP and modular programming in Python.
'''
# Weather Forecast Application Script

def get_weather_data():
    return {
        "New York": {"city": "New York", "temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"city": "London", "temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"city": "Tokyo", "temperature": 75, "condition": "Rainy", "humidity": 70}
    }

def fetch_weather_data(city):
    weather_data = get_weather_data()
    return weather_data.get(city.title(), None)  

def parse_weather_data(data):
    if not data:
        return "Weather data not available"
    return f"Weather in {data['city']}: {data['temperature']} degrees, {data['condition']}, Humidity: {data['humidity']}%"

def display_weather(city, detailed=False):
    data = fetch_weather_data(city)
    if not data:
        return f"Weather data not available for {city}"
    return parse_weather_data(data)

def main_weather_forcast():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        forecast = display_weather(city)
        print(forecast)

main_weather_forcast()