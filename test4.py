tasks=[]
while True:
    user_action=input("add, show or exit?")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            add_task=input("input to add")
            tasks.append(add_task)
        case 'show':
            for item in tasks:
                print(item)
        case 'exit':
            break
print("All cases done")