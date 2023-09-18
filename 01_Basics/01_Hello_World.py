print("Hello World!\n~ My name is Wi.")
name = input("What is your name?\n> ")
print("Nice to meet you, " + name + "! How old are you?")

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

print("Great! You are " + str(age) + " years old.")
hobbies = input("What are your hobbies?\n> ")
print("Interesting! You enjoy " + hobbies + ".")
location = input("Where are you from?\n> ")
print("I've heard " + location + " is a beautiful place.")
print("Unfortunately, I have to go now, " + name + ".")
