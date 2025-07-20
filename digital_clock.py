from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('calibri', 50, 'bold'),
              background='black', foreground='cyan')
label.pack(anchor='center')

time()
root.mainloop()
