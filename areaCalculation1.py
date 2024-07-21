try:
    total_value = float(input("Enter total value: "))
    if total_value == 0:
        print("Your total value can not be zero")
        exit()
    value = float(input("Enter value: "))
    area = value / total_value * 100
    print(f"That is {area}")

except (SyntaxError, ValueError):
    print("This is under except")
