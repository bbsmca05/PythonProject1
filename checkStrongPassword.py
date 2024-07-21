password=input("Enter password")
test_criteria=[]
if len(password)>=8:
    test_criteria.append(True)

upp_check=False
for i in password:
    if i.isupper():
        upp_check=True
test_criteria.append(upp_check)

num_check=False
for i in password:
    if i.isdigit():
        num_check=True
test_criteria.append(num_check)

if all(test_criteria):
    print("Strong Password")
else:
    print("Weak Password")
