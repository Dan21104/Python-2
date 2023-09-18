print("Hello World! \n ~ My name is Wi.")
name = input("What is your name?\n >")
print("Nice to meet you " + name + ", how old are you?")
while True:
    try:
        age = int(input(" >"))
        if age <= 13:
            print("You have to be older than 13 y.o.")
            continue
        elif age > 116:
            print("That is not real.")
            continue
        else:
            break
    except ValueError:
        print("Try again, insert eligible number.")
        continue
