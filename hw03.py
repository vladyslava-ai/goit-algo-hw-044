import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def show_directory(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f" {item.name}")
            show_directory(item, indent + "    ")
        elif item.is_file():
            print(indent + Fore.GREEN + f" {item.name}")

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print("Вказаний шлях не існує.")
        return

    if not path.is_dir():
        print("Вказаний шлях не є директорією.")
        return

    print(Fore.BLUE + f" {path.name}")
    show_directory(path)


if __name__ == "__main__":
    main()