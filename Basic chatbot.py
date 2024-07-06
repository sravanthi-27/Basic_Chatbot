import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('nps_chat')
nltk.download('punkt')

# Define Patterns and Responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI. You can call me ChatGPT.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you today?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"what does this code do?",
        ["This code creates a simple text-based chatbot using Python and the NLTK library.",]
    ],
    [
        r"what is nltk?",
        ["NLTK, or Natural Language Toolkit, is a suite of libraries and programs for symbolic and statistical natural language processing for English.",]
    ],
    [
        r"how do you define patterns and responses?",
        ["Patterns and responses are defined using regular expressions and corresponding responses in the pairs list.",]
    ],
    [
        r"what are reflections?",
        ["Reflections are a dictionary of input/output pairs used to convert pronouns and verbs to provide more natural responses.",]
    ],
    [
        r"how does the chatbot work?",
        ["The chatbot works by matching the user's input against the predefined patterns and returning the corresponding response.",]
    ],
    [
        r"how do you handle unrecognized inputs?",
        ["Unrecognized inputs are handled by default responses defined in the default_responses list.",]
    ],
    [
        r"how do you start the chat?",
        ["The chat is started by calling the chat() function, which enters a loop to interact with the user until 'quit' is typed.",]
    ],
    [
        r"what is a function?",
        ["A function is a block of organized, reusable code that is used to perform a single, related action.",]
    ],
    [
        r"what is a while loop?",
        ["A while loop repeatedly executes a target statement as long as a given condition is true.",]
    ],
    [
        r"how do you exit the chat?",
        ["To exit the chat, you type 'quit'. The chat() function breaks the loop and ends the session.",]
    ],
    [
        r"what is a regular expression?",
        ["A regular expression is a sequence of characters that defines a search pattern, mainly for use in pattern matching with strings.",]
    ],
    [
        r"what is a list?",
        ["A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.",]
    ],
    [
        r"what is a dictionary?",
        ["A dictionary is a collection which is unordered, changeable, and indexed. In Python, dictionaries are written with curly brackets and have keys and values.",]
    ],
    [
        r"what is a string?",
        ["A string is a sequence of characters, and in Python, strings are surrounded by either single quotation marks, or double quotation marks.",]
    ],
    [
        r"what is an integer?",
        ["An integer is a whole number, positive or negative, without decimals, of unlimited length in Python.",]
    ],
    [
        r"what is a float?",
        ["A float is a number, positive or negative, containing one or more decimals.",]
    ],
    [
        r"what is a boolean?",
        ["A boolean represents one of two values: True or False.",]
    ],
    [
        r"what is type casting?",
        ["Type casting is the process of converting one data type to another, such as converting an integer to a string.",]
    ],
    [
        r"what is a module?",
        ["A module is a file containing Python definitions and statements. Modules can define functions, classes, and variables, and can also include runnable code.",]
    ],
    [
        r"what is an import statement?",
        ["An import statement allows you to include the definitions (functions, classes, variables) from a module into your script.",]
    ],
    [
        r"what is an exception?",
        ["An exception is an error that occurs during the execution of a program. In Python, exceptions are handled using try and except blocks.",]
    ],
    [
        r"what is a comment?",
        ["A comment is a part of the code that is not executed. Comments in Python start with a #.",]
    ],
    [
        r"what is a for loop?",
        ["A for loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string) with an automatic counter.",]
    ],
]

# Default responses
default_responses = [
    "I didn't understand that.",
    "Could you say that again?",
    "I'm not sure what you mean.",
]

# Initialize the Chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chat
def chat():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Bye, take care!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(response)
        else:
            print(default_responses[0])

# Start the chat
if __name__ == "__main__":
    chat()
