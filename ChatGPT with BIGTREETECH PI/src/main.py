# Importing the OpenAI module to use its functionality
from openai import OpenAI

# Initializing the OpenAI client with API keys
client = OpenAI(
    api_key = ""
)

# List to store messages exchanged between user and assistant
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant"
    }
]

# Continuous loop to interact with the chatbot
while True:
    # Prompting user for input
    message = input("You: ")

    # Appending user's message to the list
    messages.append(
        {
            "role": "user",
            "content": message
        },
    )

    # Generating a response from the chatbot using the OpenAI API
    chat = client.chat.completions.create(
        messages = messages,  # Previous messages exchanged
        model = "gpt-3.5-turbo"  # Model used for generating responses
    )

    # Extracting the reply from the chatbot's response
    reply = chat.choices[0].message

    # Displaying the assistant's reply
    print("Assistant: ", reply.content)
    
    # Appending assistant's reply to the list for continuity in conversation
    messages.append(reply)