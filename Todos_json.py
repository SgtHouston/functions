# Import json to save content of 
# \todos file after quitting program
import json


# Open a list of todos
with open('Todos.json','r') as todos_json:
    todos = json.load(todos_json)

def print_todos():
    print('----------ToDos----------')
    count = 1
    for todo in todos:
        print(f"[{count}]: {todo}")
        count += 1
        print('-----------------------')
    return todos

while True:
    print("""\n Choose an option:
    
    1. Print Todos
    2. Add Todos
    3. Remove Todos
    0. Quit 
    """)
    user_choice = input('')
    print ('\n')

    if user_choice == '1':
        
        # print current todos
        print_todos()
        print("\n")
        
    elif user_choice == '2':
        # Add new item
        
        new_todo = input("What do you want to add to your 'To-Do' List?: ")

        todos.append(new_todo)

        print_todos()

    elif user_choice == '3':
        # Delete a todo
        
        index = 0
        for todo in todos:
            print(f"{index}: {todo}")
            index += 1
        delete_index = int(input("Which item do you want to delete?: "))
        del todos[delete_index]

        print_todos()

    elif user_choice == '0':
        # exit the program
        with open('Todos.json', 'w') as todos_json:
            json.dump(todos, todos_json)
        break
       
      

with open('Todos.json', 'w') as todos_json:
    json.dump(todos, todos_json)








