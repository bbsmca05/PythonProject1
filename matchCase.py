todos=[]
while True:
    user_action=input("Enter task as add, show, edit or exit")
    user_action=user_action.strip()

    match user_action:
        case 'add':
            todo=input("Enter todo item")
            todos.append(todo)
        case 'show':
            #todo=input("Enter todo item")
            #print(todos)
            for item in todos:
                print(item)
        case 'exit':
            break
print("Your program is done")