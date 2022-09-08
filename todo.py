# Todo List App

print("""
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
""")

todos = []
counter = 1
while True:
    print("*" * 35)
    user_input = input("Enter a command. Type 'h' for help:\n> ")
    todos.append(f"{counter}) {user_input}")
    counter += 1

    for todo in todos:
        print(todo)
    



