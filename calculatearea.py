try:
    l = float(input("Enter length"))
    b = float(input("Enter breath"))
    if l == b:
        exit("l and b should be different")
    print(l * b)
except ValueError:
    print("Please enter value in int or in float")
