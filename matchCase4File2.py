while True:
    user_action=input("Enter task as add, show, edit or exit")
    user_action=user_action.strip()

    match user_action:
        case 'add':
            todo=input("Enter Item Name")+"\n"
            filer = open(r'D:\PythonProjects\ExternalFiles\text.txt', 'r')
            todos = filer.readlines()
            filer.close()
            todos.append(todo)
            file=open(r'D:\PythonProjects\ExternalFiles\text.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            #todo=input("Enter todo item")
            #print(todos)
            filer = open(r'D:\PythonProjects\ExternalFiles\text.txt', 'r')
            todos = filer.readlines()
            filer.close()
            for (index,item) in enumerate(todos):
                string_to_print=f"{index}-{item}"
                print(string_to_print)
        case 'edit':
            item_to_edit=int(input("Which item you would like to edit?"))
            item_to_edit=item_to_edit-1
            print(item_to_edit)
            todos[item_to_edit]=input("New Item")
        case 'exit':
            break
print("Your program is done")