from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Find & Replace")

efield1 = Entry(root, width=50)
efield1.grid(row=3, column=1)
efield1.insert(0, "Find?")

efield2 = Entry(root, width=50)
efield2.grid(row=4, column=1)
efield2.insert(0, "Replace with?")


# Button 1 function
def but1Click():
    file_path = filedialog.askdirectory()
    os.chdir(file_path)
    fral1label = Label(root, text="Current Directory:  " + os.getcwd())
    fral1label.grid(row=0, column=1)


# Button 2 function
def farfunc():
    file_path = os.getcwd()
    for directname, directnames, files in os.walk(file_path):
        for x in files:
            filename, ext = os.path.splitext(x)
            var1 = efield1.get()
            var2 = efield2.get()
            if var1 in filename:
                new_name = filename.replace(var1, var2)
                os.rename(
                    os.path.join(directname, x),
                    os.path.join(directname, new_name + ext))


# Button widgets
button1 = Button(root, text='Select directory', command=but1Click)
button1.grid(row=1, column=1)
button2 = Button(root, text='Execute', command=farfunc)
button2.grid(row=5, column=1)

root.mainloop()
