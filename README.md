# Mouse cursor coordinates
<p>This simple Python script displays the coordinates of your mouse cursor. It can be used for automation purposes, allowing you to move with your mouse cursor to identify the necessary coordinates. Additionally, the program can be utilized as a screen resolution detector by running the program and then pointing the cursor into the right bottom corner. To obtain the resolution, simply add +1 to each number. For instance, 1919 1019 is 1920x1080.</p>

# Packages
<p>It makes use of just two Python packages, one of which is <a href="https://pypi.org/project/PyAutoGUI/">pyautogui</a>, which is used to detect the coordinates of the mouse cursor. This package is employed to control the mouse and keyboard, and one of its functions is to read the coordinates of the mouse cursor. The other package is <a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a>, which is used for GUI.</p>

# Source code
```py
import tkinter as tk
import pyautogui as g

def cords():
    print(g.position())
    return g.position()
    cords()

def update_label():
    label.config(text=cords())
    root.after(100, update_label)

root = tk.Tk()
root.geometry('300x50')
root.title("Souřadnice kurzoru")

label = tk.Label(root, text=cords())
label.pack()

root.after(100, update_label)

root.mainloop()
```
