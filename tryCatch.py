user_action = input("What is your choice?")

if 'add' in user_action:
    print("This is for addition")

elif 'sub' in user_action:
    print("This is for Subtraction")

elif 'mul' in user_action:
    print("This is for multiplication")

elif 'div' in user_action:
    try:
        print(10/0)
    except ZeroDivisionError:
        print("it is invalid")

