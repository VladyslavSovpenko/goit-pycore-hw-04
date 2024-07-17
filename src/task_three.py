import os
import sys
from colorama import Fore, Style, init
from pathlib import Path


def is_hidden_or_system(entity):
    system_files = ['__pycache__']
    return entity.startswith('.') or entity in system_files


def visualize_dir_structure(path, depth=1):
    if not os.path.exists(path):
        print(f"{Fore.RED}Error: {path} does not exist{Style.RESET_ALL}")
        return
    if not os.path.isdir(path):
        print(f"{Fore.RED}Error: {path} is not a directory{Style.RESET_ALL}")
        return

    entities = os.listdir(path)
    for item in entities:
        if is_hidden_or_system(item):
            continue
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{'    ' * (depth if depth else 0)}{Fore.YELLOW}{item}:{Style.RESET_ALL}")
            visualize_dir_structure(item_path, depth + 1)
        elif os.path.isfile(item_path):
            print(f"{'    ' * (depth if depth else 0)}{Fore.CYAN}{item}{Style.RESET_ALL}")


if __name__ == "__main__":
    init()
    if len(sys.argv) < 2:
        print("Usage: python script.py <path>")
        sys.exit(1)
    directory_path = sys.argv[1]
    print(f"{Fore.BLUE}{Path(directory_path).name}/{Style.RESET_ALL}")
    visualize_dir_structure(directory_path)
