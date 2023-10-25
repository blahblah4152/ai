# Perfect

# import random
import openai

# Set your OpenAI API key here
api_key = "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"
# api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Responses for different types of programming questions
responses = {
    "how are you": "I am good! What about you?",
    "help": "Sure, I can help you with programming questions. Just ask!",
    "python": "Python is a popular programming language known for its simplicity and versatility.",
    "java": "Java is a widely used programming language, especially for building enterprise-level applications.",
    "c++": "C++ is a powerful programming language commonly used for system development and game development.",
    "web": "Web development involves creating websites and web applications using technologies like HTML, CSS, and JavaScript.",
    "database": "Databases are used to store and manage data. Common database systems include MySQL, PostgreSQL, and MongoDB.",
    "algorithm": "An algorithm is a step-by-step procedure or formula for solving a problem.",
    "loop": "Loops are used to repeatedly execute a block of code. Common types are 'for' and 'while' loops.",
    "exit": "Goodbye! Feel free to return if you have more questions."
}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    return generate_gpt_response(user_input)

def generate_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the GPT-3.5 engine
        prompt=prompt,
        max_tokens=50  # You can adjust the max_tokens as needed
    )
    return response.choices[0].text.strip()

def main():
    print("Hello! I'm your programming guidance chatbot. How can I assist you?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot:", get_response("exit"))
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()