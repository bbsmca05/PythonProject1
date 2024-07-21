password=input("Enter password")
test_criteria = {}
if len(password) >= 8:
    test_criteria["length"] = True

upp_check = False
for i in password:
    if i.isupper():
        upp_check = True
test_criteria["UpperCheck"] = upp_check

num_check = False
for i in password:
    if i.isdigit():
        num_check=True
test_criteria["NumCheck"] = num_check

print(test_criteria)
if all(test_criteria.values()):
    print("Strong Password")
else:
    print("Weak Password")
