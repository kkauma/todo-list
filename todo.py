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
    print("*" * 30)
    user_input = input("Enter a command. Type 'h' for help:\n> ")
    todos.append(user_input)

    for todo in todos:
        print(f"{counter}) {todo}")
        counter += 1
    



