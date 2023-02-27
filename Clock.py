#libs
from tkinter import *
from tkinter.ttk import *
from time import strftime

#tkinter into win
win = Tk()
win.title("Clock")

#time function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#sytle
label = Label(win, font=('Times New Roman', 60), background='black',foreground='cyan')
label.pack(anchor='center')

#loop
if __name__ == "__main__":
    time()
    mainloop()