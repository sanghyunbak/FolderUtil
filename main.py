# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import shutil
from typing import Iterator, AnyStr
from termcolor import colored
from glob import glob


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


ROOT_DIR = "E:\토렌트\Complete"


def get_dir_list(dir: str) -> Iterator[tuple[AnyStr, list[AnyStr], list[AnyStr]]]:
    return os.walk(dir)


def get_dir_using_grob(dir):
    return glob(os.path.join(dir, "*", ""))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir_list = get_dir_list(ROOT_DIR)

    for dir in dir_list:
        print(colored(f"{dir}", "green"))

    print(colored(f"{get_dir_using_grob(ROOT_DIR)}", "yellow"))
    dir_list_using_glob = get_dir_using_grob(ROOT_DIR)

    for dir in dir_list_using_glob:
        print(colored(f"{dir}", "magenta"))
        files = os.listdir(dir)
        print(colored(f"files in {dir}", "yellow"))
        for file in files:
            print(colored(f"{file}", "green"))
            before = os.path.join(dir, file)
            after = os.path.join(ROOT_DIR, file)
            print(colored(f"file will move from ({before}) to ({after})", "green"))
            shutil.move(before, after)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
