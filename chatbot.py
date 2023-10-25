# from chatterbot import ChatBot

# ai = ChatBot("bot")


import re, random

knowledge_base = {
    "greetings": "Hello How can i help you?",
    "menu": "We offer a variety of pizzas including Margherita, Vegeterian, Non-Vegeterian, and more. You can also customize your pizza with your favorite toppings.",
    "prices": "Pizza prices vary depending on the size and toppings. A small Margherita is ₹99, a medium Margharita is ₹169, and a large Margharita is ₹229.",
    "price": "Pizza prices vary depending on the size and toppings. A small Margherita is ₹99, a medium Margharita is ₹169, and a large Margharita is ₹229.",
    "delivery": "Yes, we offer delivery. It typically takes 30-45 minutes for your order to arrive.",
    "toppings": "There are vaarious kinds of toppings available at our store like extram cheese, ketchup, vegggies, corn, mushrooms and many more",
    "crust": "For every pizza there are varioous crusts like hand toast, thin crust and cheese burst",
    "hours": "Our store is open from 11:00 AM to 10:00 PM every day.",
    "location": "We are located at 123 High Street, Pune, Maharashtra.",
    "contact": "You can reach us at (240) 456-7890 or email us at shop@pizza.com.",
}

def chatbot_response(query):
    for pattern, response in knowledge_base.items():
        if re.search(pattern, query, re.IGNORECASE):
            return response
    return "I am sorry i don't have any information on your query"

def chat():
    print("Pizza shop Chatbot")
    print("")
    while True:
        query = input("User: ").lower()
        if query in ["bye", "exit", "quit"]:
            print("Chatbot: Good bye! Have a nice day.")
            break
        if query.__contains__("hello") or query.__contains__("hi") or query.__contains__("hey"):
            query = "greetings"
        response = chatbot_response(query)
        print("Chatbot: ", response)


if __name__ == "__main__":
    chat()