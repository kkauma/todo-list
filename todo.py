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
skip_input = ["h", "q"]
completed_todos = []

while True:
    print("*" * 35)
    user_input = input("Enter a command. Type 'h' for help:\n> ").lower()
    if user_input == "h":
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")

    if user_input not in skip_input or user_input 
    todos.append(f"{counter}) {user_input}")
    counter += 1

    for todo in todos:
        print(todo)

    # Print out completed todos when user quits application
    if user_input == "q":
        print(f"Today you completed {len(completed_todos)} todos:\n")
        for todo in completed_todos:
            print(f"* {todo}")

        print("Nice work!")

    

    



