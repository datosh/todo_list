import sys

todos = []

def read_verb():
    verbs = ["add", "list", "complete", "exit"]
    user_input = input("What do you want to do? " + str(verbs) + "\n")
    if user_input not in verbs:
        sys.exit("This verb is not supported: " + user_input)
    return user_input

def add_todo():
    user_input = input("What do you need to do?\n")
    todos.append(user_input)
    print("Your do to was added!")

def print_todos():
    for i in range(len(todos)):
        print(str(i) + ":" + todos[i])

def list_todos():
    print("You need to do:")
    print_todos()

def complete_todo():
    print_todos()
    user_input = input("Which todo has been completed? (put the ID)\n")
    todo_id = int(user_input)
    # https://docs.python.org/3/tutorial/datastructures.html
    todos.pop(todo_id)

def main():
    while True:
        verb = read_verb()
        if verb == "add":
            add_todo()
        if verb == "list":
            list_todos()
        if verb == "complete":
            complete_todo()
        if verb == "exit":
            return
        # Separate each command visually
        print("\n")

main()