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

def hacker_notepad(filename, font):
    init(wrap=False)  # Initialize colorama
    font_styles = {"bold": Style.BRIGHT, "underline": "\033[4m", "dim": Style.DIM}
    font_colors = {"red": Fore.RED, "green": Fore.GREEN, "blue": Fore.BLUE}
    font_style = font_styles.get(font, Style.NORMAL)
    font_color = font_colors.get(font, Fore.WHITE)

    clear_screen()
    type_text(font_style + font_color + "ACCESS GRANTED\n" + Style.RESET_ALL)
    time.sleep(1)

    clear_screen()
    type_text(font_style + font_color + "WELCOME TO HACKER'S NOTEPAD\n" + Style.RESET_ALL)
    time.sleep(1)

    clear_screen()
    type_text(font_style + font_color + "LOADING FILES...\n" + Style.RESET_ALL)
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

filename = input("Enter a filename to create or open: ")
try:
    if os.path.splitext(filename)[1] not in {".txt", ".log", ".md"}:
        raise ValueError("Invalid file type.")
except ValueError as e:
    clear_screen()
    type_text(Style.BRIGHT + Fore.RED + str(e) + "\n" + Style.RESET_ALL)
else:
    font = random.choice(["bold", "underline", "dim", "red", "green", "blue"])
    hacker_notepad(filename, font)
