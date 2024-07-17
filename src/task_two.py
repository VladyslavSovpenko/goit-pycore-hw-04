import pprint
from pathlib import Path


def get_cats_info(path: str) -> []:
    try:
        with Path(path).open('r', encoding="utf-8") as fh:
            dict_cats = []
            for line in fh:
                id, name, age = line.strip().split(',')
                dict_cats.append({'id': id, 'name': name, 'age': int(age)})
            return dict_cats
    except (FileNotFoundError, OSError):
        print(f"File {path} Not Found")
        return None


if __name__ == "__main__":
    while True:
        user_input = input("Print path or exit:")
        if user_input == "exit":
            break
        else:
            pprint.pprint(get_cats_info(user_input))
