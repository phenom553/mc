#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()


canvas = tk.Canvas(root, height=700, width=700,bg="#263D48")
canvas.pack()



frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


openFile = tk.Button(root, text="Open file", padx=10, pady=5, fg="darkgrey", bg="grey")
openFile.pack()

runApp = tk.Button(root, text="Run App", padx=10, pady=5, fg="darkgrey", bg="grey")
runApp.pack()

root.mainloop()



