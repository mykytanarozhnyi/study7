import os

def print_directory_tree(startpath, indent=''):
    for item in os.listdir(startpath):
        item_path = os.path.join(startpath, item)
        if os.path.isdir(item_path):
            print(f"{indent}{item}/")
            print_directory_tree(item_path, indent + '  ')
        else:
            print(f"{indent}{item}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"tree for {current_dir}:\n")
    print_directory_tree(current_dir)