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