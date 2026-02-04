#tkinter tutorial
import tkinter as tk
import random
import csv
def window():
	root = tk.Tk()

	root.title("My first gui window")
	root.geometry("400x300")

	label = tk.Label(root, text= "Hello, Tkinter!")
	label.pack(pady = 50)
	
	btn = tk.Button(root, text = "Close", command = root.destroy)
	btn.pack()
	root.mainloop()

