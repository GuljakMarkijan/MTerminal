import os
import time
import shutil
import zipfile
import subprocess
from colorama import init
from colorama import Fore, Back, Style

def create_file(namefile, text=None):
    try:
        with open(namefile, 'w', encoding='utf-8') as f:
            if text:
                f.write(text)
    except Exception as e:
        print(f"Помилка при створенні файлу: {e}")

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Ця папка вже існує')
    except Exception as e:
        print(f"Помилка при створенні папки: {e}")

def get_list(folders_only=False):
    try:
        result = os.listdir()
        if folders_only:
            result = [f for f in result if os.path.isdir(f)]
        print(result)
    except Exception as e:
        print(f"Помилка при отриманні списку файлів: {e}")

def change_directory(namedir):
    try:
        os.chdir(namedir)
    except FileNotFoundError:
        print(f"Папка {namedir} не знайдена.")
    except Exception as e:
        print(f"Помилка при зміні директорії: {e}")

def view_file_content(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

def edit_file_content(filename):
    try:
        print("Введіть новий вміст файлу. Введіть 'STOP' на новому рядку для завершення.")
        lines = []
        while True:
            line = input()
            if line == "STOP":
                break
            lines.append(line)
        new_content = "\n".join(lines)
        with open(filename, 'w') as file:
            file.write(new_content)
    except Exception as e:
        print(f"Помилка при редагуванні файлу: {e}")

def create_zip(zipname, files):
    try:
        with zipfile.ZipFile(zipname, 'w') as zipf:
            for file in files:
                zipf.write(file)
    except Exception as e:
        print(f"Помилка при створенні zip-архіву: {e}")

def extract_zip(zipname, path='.'):
    try:
        with zipfile.ZipFile(zipname, 'r') as zipf:
            zipf.extractall(path)
    except Exception as e:
        print(f"Помилка при розпакуванні zip-архіву: {e}")

def show_help():
    commands = {
        "dir": "Змінити директорію",
        "crfile": "Створити файл",
        "crdir": "Створити папку",
        "show": "Показати список файлів та папок",
        "delf": "Видалити файл",
        "deld": "Видалити папку",
        "ren": "Перейменувати файл або папку",
        "read": "Прочитати файл",
        "edit": "Редагувати файл",
        "zip": "Створити zip-архів",
        "unzip": "Розпакувати zip-архів",
        "copy": "Копіювати файл",
        "replase": "Перемістити файл",
        "search": "Пошук файлу",
        "chmod": "Змінити дозволи файлу",
        "size": "Отримати розмір файлу",
        "help": "Показати це повідомлення допомоги"
    }

    for command, description in commands.items():
        print(f"{command}: {description}")

init()

print()
time.sleep(1)
print(Fore.YELLOW+Back.BLUE+"MTerminal"+Fore.WHITE+Back.BLACK, "...")
time.sleep(2.5)
print()
print(Fore.YELLOW+Back.BLUE+"MTerminal"+Fore.WHITE+Back.BLACK, "version 1.4.0")
print("Copyright 2024,05,15 Guljak Markijan")
print()


while True:
    try:
        print(os.getcwd(), end="")
        print("~" + Fore.RED + "$", end="")
        print(Fore.CYAN, end=" ")
        command = input()
        print(Fore.WHITE)
        
        if command == "dir":
            name = input("Введіть назву папки> ")
            change_directory(name)
        
        elif command == "crfile":
            create_file(input('Введіть назву файлу> '))
        
        elif command == "crdir":
            ndir = input("Введіть назву папки> ")
            create_folder(ndir)
        
        elif command == "show":
            get_list()
        
        elif command == "delf":
            delf = input("Введіть назву файлу, який хочете видалити> ")
            print(Back.RED)
            print("Видалити цей файл? y/n:")
            print(Back.BLACK)
            y = input()
            if y == "y":
                os.remove(delf)
        
        elif command == "deld":
            deld = input("Введіть назву папки, яку хочете видалити> ")
            print("Видалити цю папку? y/n:")
            n = input()
            if n == "y":
                os.removedirs(deld)
        
        elif command == "ren":
            re = input("Який файл/папку перейменувати> ")
            n = input("Нова назва файлу/папки>")
            os.rename(re, n)
        
        elif command =="read":
            filename = input("Введіть назву файлу для читання> ")
            view_file_content(filename)
        
        elif command == "edit":
            filename = input("Введіть назву файлу для редагування> ")
            edit_file_content(filename)
        
        elif command == "zip":
            zipname = input("Введіть назву zip-архіву для створення> ")
            files = input("Введіть назви файлів для додавання, розділені пробілами> ").split()
            create_zip(zipname, files)
        
        elif command == "unzip":
            zipname = input("Введіть назву zip-архіву для розпакування> ")
            path = input("Введіть директорію для розпакування файлів> ")
            extract_zip(zipname, path)
        
        elif command == 'copy':
            source_file = input('Введіть назву файлу, який хочете копіювати> ')
            destination_folder = input('Куди хочете копіювати файл> ')
            shutil.copy(source_file, destination_folder)

        elif command == 'replase':
            source_file = input('Введіть назву файлу, який хочете перемістити> ')
            destination_folder = input('Куди хочете перемістити файл> ')
            shutil.move(source_file, destination_folder)
        
        elif command == "explorer":
            subprocess.Popen(['C:/Windows/explorer.exe'])
        
        elif command == "cmd":
            subprocess.Popen(['C:/Windows/system32/cmd.exe'])
        
        elif command == "doc-explorer":
            subprocess.Popen(['D:/Program Files/DOC-Explorer/build/exe.win-amd64-3.12/DOC-Explorer.exe'])

        elif command == "calc":
            subprocess.Popen(['C:/Windows/system32/calc.exe'])
        
        elif command == "aimp":
            subprocess.Popen(['C:/Program Files (x86)/AIMP/AIMP.exe'])

        elif command == 'control panel':
            subprocess.Popen(['C:/Windows/System32/control.exe'])
            '''
        elif command == 'is':
            subprocess.Popen(['D:/Program Files/Internet Surfer/main.py'])'''

        elif command == 'chrome':
            subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe'])
        
        elif command == 'exit':
            break

        elif command == "help":
            show_help()
        
        else:
            print("Error!")
    
    except Exception as e:
        print(f"Помилка: {e}")






        