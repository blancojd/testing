import time

# Initialize an empty dictionary to store the messages
messages = {}

# Define a function to add a message to the chat
def add_message(sender, message):
    timestamp = time.time()
    messages[timestamp] = (sender, message)

# Define a function to print the chat history
def print_chat_history():
    for timestamp, message in messages.items():
        if time.time() - timestamp < 24 * 60 * 60:
            print(f"{message[0]}: {message[1]}")

# Start the chat loop
while True:
    sender = input("Enter your name: ")
    message = input("Enter your message: ")
    add_message(sender, message)
    print_chat_history()
