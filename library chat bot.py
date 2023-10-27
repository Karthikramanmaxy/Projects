import random

# Define a dictionary to simulate the library book inventory
library_inventory = {
    "Harry Potter and the Sorcerer's Stone": 5,
    "To Kill a Mockingbird": 3,
    "1984": 2,
    "Pride and Prejudice": 4,
    "The Great Gatsby": 1,
}

# Define a dictionary to simulate user reservations
user_reservations = {}

# Function to check book availability
def check_availability(book_title):
    if book_title in library_inventory and library_inventory[book_title] > 0:
        return True
    else:
        return False

# Bot introduction
print("Welcome to the Library! How can I assist you today?")

# Function to simulate the chatbot
def library_bot():
    while True:
        user_input = input("You: ")

        # Possible user inputs and corresponding bot responses
        if 'hello' in user_input.lower():
            print("Library Bot: Hello! How can I help you today?")
        elif 'find a book' in user_input.lower():
            book = input("You: Please specify the name of the book you are looking for: ")
            if check_availability(book):
                print(f"Library Bot: Yes, the book '{book}' is available!")
            else:
                print(f"Library Bot: I'm sorry, the book '{book}' is not available at the moment.")
        elif 'reserve a book' in user_input.lower():
            book = input("You: Please specify the name of the book you want to reserve: ")
            if check_availability(book):
                if book in user_reservations:
                    print("Library Bot: Sorry, this book has already been reserved by another user.")
                else:
                    user_reservations[book] = 1
                    print("Library Bot: Your reservation for the book has been placed!")
            else:
                print("Library Bot: I'm sorry, the book cannot be reserved right now. Please try again later.")
        elif 'return a book' in user_input.lower():
            book = input("You: Please specify the name of the book you want to return: ")
            if book in user_reservations:
                user_reservations.pop(book)
                library_inventory[book] += 1
                print(f"Library Bot: Thank you for returning '{book}'. We hope you enjoyed it!")
            else:
                print("Library Bot: I'm sorry, it seems you haven't reserved this book.")
        elif 'check my reservations' in user_input.lower():
            if user_reservations:
                print("Library Bot: You have the following books reserved:")
                for book in user_reservations:
                    print(f" - {book}")
            else:
                print("Library Bot: You don't have any reservations at the moment.")
        elif 'exit' in user_input.lower() or 'bye' in user_input.lower():
            print("Library Bot: Thank you for visiting the Library. Have a great day!")
            break
        else:
            print("Library Bot: I'm sorry, I didn't understand that. Could you please rephrase your request?")

# Starting the conversation
library_bot()
