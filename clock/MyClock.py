# Manas Mishra
# Clock using python.
import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

root = tk.Tk()
root.title('Clock')

label = tk.Label(root, font = ('calibri', 40, 'bold'),
                 background = 'cyan', foreground = 'black')

label.pack(anchor = 'center')

time()

root.mainloop()
