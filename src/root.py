from src.appRunner import appOpenner
from src.settings import *

from tkinter import *

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Root
root.title('Work Manager')
root.geometry('300x300')
root.configure(background=backgroundColor)

# Layout configuration
topBar = Frame(root, width=screen_width, height=40, bg=leftBarColor)
topBar.grid(row=0, column=0, columnspan=100, sticky='n')

leftBar = Frame(root, width=75, height=screen_height, bg=leftBarColor)
leftBar.grid(row=1, column=0, sticky='w')

mainView = Frame(root, width=screen_width, height=screen_height, bg=backgroundColor)
mainView.grid(row=1, column=1, rowspan=100, columnspan=100, sticky='nw')

# Item configuration
appOpenner(mainView)
