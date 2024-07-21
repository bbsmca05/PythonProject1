todos=[]
while True:
    user_action=input("Enter task as add, show, edit or exit")
    user_action=user_action.strip()

    match user_action:
        case 'add':
            todo=input("Enter Item Name")
            todos.append(todo)
        case 'show':
            #todo=input("Enter todo item")
            #print(todos)
            for (index,item) in enumerate(todos):
                print(index,"-",item)
        case 'edit':
            item_to_edit=int(input("Which item you would like to edit?"))
            item_to_edit=item_to_edit-1
            print(item_to_edit)
            todos[item_to_edit]=input("New Item")
        case 'exit':
            break
print("Your program is done")