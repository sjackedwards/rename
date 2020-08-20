import os
import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askdirectory()
print(file_path)

answer = input('Are you in the correct directory?? [y/n]:')
if not answer or answer[0].lower() != 'y':
    exit(1)

replaceV = input("Character value to be changed:  ")
newV = input("New character value:  ")

for directname, directnames, files in os.walk(file_path):
    for x in files:
        filename, ext = os.path.splitext(x)
        if replaceV in filename:
            new_name = filename.replace(replaceV, newV)
            os.rename(
                os.path.join(directname, x),
                os.path.join(directname, new_name + ext))

input("Done! Press Enter to exit.")
