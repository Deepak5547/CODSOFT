import re

def simple_chatbot(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    rules_responses = {
        r'hello|hi|hey': 'Hello! How can I assist you?',
        r'how are you|how are you doing': 'I am a chatbot and I am doing well, thank you!',
        r'what is your name': 'I am a simple chatbot.',
        r'bye|goodbye|see you': 'Goodbye! Have a great day!',
        r'help': 'I can respond to greetings, ask about my name, and bid farewell. How can I help you?',
        r'.*': 'I'm sorry, I didn't understand that. Please ask something else or type "help" for assistance.'
    }

    # Iterate through rules and find a match
    for pattern, response in rules_responses.items():
        if re.match(pattern, user_input):
            return response

# Main loop for user interaction
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("User: ")
    
    # Check for exit condition
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye! Have a great day.")
        break

    # Get the chatbot's response
    response = simple_chatbot(user_input)
    
    # Display the response
    print("Simple Chatbot:", response)
