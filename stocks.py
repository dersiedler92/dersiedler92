from tkinter import *
import tkinter as tk

top = tk.Tk()
top.title("My Title")
btn_frame = tk.Frame(top)
btn_frame.pack()
btn_1 = tk.Checkbutton(master=btn_frame, text="Hello everynyan", width=30, height=5, relief=SUNKEN)
btn_1.grid(row=1, column=1)
btn_2 = tk.Checkbutton(master=btn_frame, text="Hello everynyan", width=30, height=5, relief=SUNKEN)
btn_2.grid(row=1, column=2)
btn_3 = tk.Checkbutton(master=btn_frame, text="Hello everynyan", width=30, height=5, relief=SUNKEN)
btn_3.grid(row=2, column=1)
btn_4 = tk.Checkbutton(master=btn_frame, text="Hello everynyan", width=30, height=5, relief=SUNKEN)
btn_4.grid(row=2, column=2)

top.mainloop()
