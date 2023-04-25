FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of ToDo items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the To Do list in a text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# allows the code block to be called only when this program is run as the main file
# if this is imported, the code block will not run
if __name__ == "__main__":
    print("Hello from function")
