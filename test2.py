tasks=[]
while True:
    user_action=input("add, show or exit?")
    match user_action:
        case 'add':
            add_task=input("input to add")
            tasks.append(add_task)
        case 'show':
            print(tasks)
        case 'exit':
            break
print("All cases done")