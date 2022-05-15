from src.settings import *
from src.commands import *
import os
import subprocess
from tkinter import *

appList = {
    0: apps[0],
    1: apps[1],
    2: apps[2],
    3: apps[3],
    4: apps[4]
}

checkedApps = {
    appList[0]: 0,
    appList[1]: 0,
    appList[2]: 0,
    appList[3]: 0,
    appList[4]: 0
}


def startApps():
    for app in checkedApps:
        checked = checkedApps[app].get()
        if checked:
            match app:
                case 'Neptune Board':
                    os.system(openNeptuneBoard)
                case 'Spotify':
                    os.system(openSpotify)
                case _:
                    print('Not implemented')


def appOpenner(mainView):
    i = 0
    for app in checkedApps:
        checkedApps[app] = IntVar()
        cbApp = Checkbutton(mainView, text=app, font=mainFont, pady=4, anchor="w", variable=checkedApps[app],
                            bg=backgroundColor, activebackground=backgroundColor, activeforeground=textColor,
                            fg=textColor, selectcolor=selectionColor)

        cbApp.grid(row=i, column=0, sticky='w')
        i += 1

    butRun = Button(mainView, text="Run", font=buttonFont,
                    fg=textColor, bg=itemColor, command=startApps)

    butRun.grid(row=10, column=0, sticky="e")
