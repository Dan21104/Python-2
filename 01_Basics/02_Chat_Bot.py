import random

print("Hello! I am your chatbot. My name is Wi.")
name = input("What's your name?\n> ")
print(f"Nice to meet you, {name}! How old are you?")

while True:
    try:
        age = int(input("> "))
        if age <= 13:
            print("You have to be older than 13 years old.")
            continue
        elif age > 116:
            print("That doesn't seem likely. Please enter a valid age.")
            continue
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

print("Is there anything you would like to know about me?")

while True:
    user_input = input("> ").lower()

    if "hello" in user_input:
        responses = ["Hello!", "Hi there!", "Hey!", f"How can I help you today, {name}?"]
        print(random.choice(responses))
    elif "how are you" in user_input:
        responses = ["I'm just a computer program, so I don't have feelings, but I'm here to assist you.", "I'm doing well, thanks for asking.", "I'm functioning properly. What can I do for you?"]
        print(random.choice(responses))
    elif "age" in user_input:
        print(f"I'm just a computer program, so I don't have an age. But you mentioned you are {age} years old.")
    elif "hobbies" in user_input:
        hobbies = input("I love chatting with people online. What are your hobbies?\n> ")
        print(f"Wow, {hobbies} sounds interesting! I'm always here to chat about your interests.")
    elif "goodbye" in user_input or "bye" in user_input:
        print(f"Goodbye, {name}! If you have more questions, feel free to ask anytime.")
        break
    else:
        print("I'm not sure how to respond to that. Can you please ask me something else?")
