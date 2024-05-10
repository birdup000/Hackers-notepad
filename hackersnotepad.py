import os
import sys
import time
import random
from colorama import init, Fore, Back, Style, AnsiToWin32

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, speed=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def matrix_rain(font_color):
    clear_screen()
    columns = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines
    drops = [0 for i in range(int(columns))]

    title = "HACKER'S NOTEPAD"
    title_length = len(title)
    title_index = 0

    start_time = time.time()
    while time.time() - start_time < 4:
        clear_screen()
        for i in range(rows):
            for j in range(int(columns)):
                if drops[j] <= i and random.random() > 0.95:
                    if j < title_length:
                        sys.stdout.write(font_color + title[j] + Style.RESET_ALL)
                    else:
                        sys.stdout.write(font_color + chr(random.randint(33, 126)) + Style.RESET_ALL)
                else:
                    sys.stdout.write(" ")
            sys.stdout.write("\n")
        for j in range(int(columns)):
            drops[j] += 1
            if drops[j] >= rows:
                drops[j] = 0
                title_index = (title_index + 1) % title_length
        time.sleep(0.1)

def hacker_notepad(filename, font):
    init(wrap=False)  # Initialize colorama
    font_styles = {"bold": Style.BRIGHT, "underline": "\033[4m", "dim": Style.DIM}
    font_colors = {"red": Fore.RED, "green": Fore.GREEN, "blue": Fore.BLUE, "yellow": Fore.YELLOW, "cyan": Fore.CYAN, "magenta": Fore.MAGENTA}
    font_style = font_styles.get(font, Style.NORMAL)
    font_color = font_colors.get(font, Fore.WHITE)

    clear_screen()
    matrix_rain(font_color)
    time.sleep(4)

    clear_screen()
    title = "HACKER'S NOTEPAD"
    for char in title:
        sys.stdout.write(font_style + font_color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n\n")
    time.sleep(1)

    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            clear_screen()
            type_text(font_style + font_color + "FILE CONTENTS:\n\n" + Style.RESET_ALL)
            type_text(file.read(), speed=0.02)
            time.sleep(1)
    else:
        try:
            with open(filename, 'w') as file:
                pass
        except FileNotFoundError:
            clear_screen()
            type_text(font_style + Fore.RED + "ERROR: FILE NOT FOUND.\n" + Style.RESET_ALL)
            return

    while True:
        clear_screen()
        type_text(font_style + font_color + "HACKER'S NOTEPAD\n\n" + Style.RESET_ALL)
        with open(filename, 'r') as file:
            type_text(file.read(), speed=0.02)
        text = input("\n> ")
        with open(filename, 'a') as file:
            file.write(text + "\n")
        type_text(font_style + font_color + "TEXT APPENDED TO FILE.\n" + Style.RESET_ALL)
        time.sleep(0.5)
        
        if random.random() < 0.05:
            clear_screen()
            type_text(font_style + font_color + "HACKING INTO MAINFRAME...\n" + Style.RESET_ALL)
            time.sleep(2)

        if random.random() < 0.05:
            clear_screen()
            type_text(font_style + font_color + "UPDATING VIRUS DATABASE...\n" + Style.RESET_ALL)
            time.sleep(2)

        if random.random() < 0.05:
            clear_screen()
            type_text(font_style + font_color + "LAUNCHING CYBER ATTACK...\n" + Style.RESET_ALL)
            time.sleep(2)

        if random.random() < 0.05:
            clear_screen()
            type_text(font_style + font_color + "ENCRYPTING DATA...\n" + Style.RESET_ALL)
            time.sleep(2)

def enter_file():
    clear_screen()
    matrix_rain(Fore.GREEN)
    time.sleep(4)

    clear_screen()
    type_text(Style.BRIGHT + Fore.GREEN + "ENTER FILE NAME:\n" + Style.RESET_ALL, speed=0.05)
    filename = input("> ")
    try:
        if os.path.splitext(filename)[1] not in {".txt", ".log", ".md"}:
            raise ValueError("Invalid file type.")
    except ValueError as e:
        clear_screen()
        type_text(Style.BRIGHT + Fore.RED + str(e) + "\n" + Style.RESET_ALL)
    else:
        font = random.choice(["bold", "underline", "dim", "red", "green", "blue", "yellow", "cyan", "magenta"])
        hacker_notepad(filename, font)

enter_file()