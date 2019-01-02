import win10toast
import keyboard
from tkinter import *
from tkinter import Menu

def EXITME():
    exit(0)  # crashed prog so it closes
    # strtoint("crashmE!")
def Spam():
    running = True
    while running:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("Spam", "Spam", duration=1, threaded=True)

window = Tk()
window.title("NOTIFICATION SPAMMER")
window.geometry('310x50')
lbl = Label(window, text="Press Start \n to Spam")
lbl.grid(column=0, row=0)
btn = Button(window, text="Start",fg='green', command = Spam)
btn1 = Button(window, text="Stop",fg='red', command = EXITME)
btn.grid(column=1, row=0)
btn1.grid(column=2, row=0)
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='START', command=Spam)
new_item.add_separator()
new_item.add_command(label='Exit', command=EXITME)
menu.add_cascade(label='Menu', menu=new_item)
window.config(menu=menu)
window.resizable(False, False)
window.iconbitmap('favicon.ico')  # Set icon
window.mainloop()
#Close The Script to stop
