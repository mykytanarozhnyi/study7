import os


def print_directory_tree(root, indent=""):

    items = os.listdir(root)

    for item in items:

        path = os.path.join(root, item)

        if os.path.isdir(path):
            print(f"{indent}[DIR] {item}")
            print_directory_tree(path, indent + "    ")
        else:
            print(f"{indent}[FILE] {item}")


current_directory = os.getcwd()


print_directory_tree(current_directory)