import win32clipboard
import json
from tkinter import *


def create_gui():
    root = Tk()
    root.minsize(300, 100)
    root.title("Skill Plan Converter")
    btn_convert = Button(root, text="Convert", command=main_function)
    btn_convert.pack()
    btn_quit = Button(root, text="Close", command=quit)
    btn_quit.pack()
    root.mainloop()


def main_function():
    data = get_from_clipboard()
    data = convert_data(data)
    paste_to_clipboard(str(data))


def get_from_clipboard():
    win32clipboard.OpenClipboard()
    content = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return content


def convert_data(content):
    skills: dict = {}  # create new empty dictionary
    temp = ""
    if '\n' in content:
        temp = content.split('\n')  # split input string at linebreak character
    try:
        for t in temp:  # iterate over each element
            if t != "":  # check for empty lines that would create an empty key
                l = len(t)  # get length of the line
                key = t[0:l-2]  # generate key
                val = str(int(t[-2:]))  # generate value
                if key in skills:  # check if key already in dict
                    if int(val) > int(skills[key]):  # check if value needs update
                        skills[key] = val  # update value
                else:
                    skills[key] = val  # insert skill and value as new entry
    except NameError:
        pass
    result = json.dumps(skills, indent=1)  # convert dictionary into json format
    return result


def paste_to_clipboard(content):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(content)
    win32clipboard.CloseClipboard()


if __name__ == '__main__':
    create_gui()
