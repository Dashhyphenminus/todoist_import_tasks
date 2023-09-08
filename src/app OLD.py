import importlib.util
import sys

# from todoist_api_python.api import TodoistAPI
import re

from tkinter import *
from tkinter.ttk import *

import tkinter as tk


class Event:
    def __init__(self, title, date, time, description, url):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.url = url

    def show(self):
        print(self.title)

    def getTitle(self):
        return self.title


def icsToString(file):
    thing = file.read()
    thing = re.sub("\n ", "", thing)

    return thing


def stringToEvents(string):
    events = []
    events.append(Event("title", 100, 100, "description", "url"))

    i = 0
    while i < len(string):
        if len(events) > 100:
            break
        # print ("a")
        i = string.find("BEGIN:VEVENT", i)
        if i == -1:
            break
        dtStamp = string[
            string.find("DTSTAMP:", i)
            + 8 : string.find("\n", string.find("DTSTAMP:", i) + 8)
        ]
        uId = string[
            string.find("UID:", i) + 8 : string.find("\n", string.find("UID:", i) + 4)
        ]
        dTStart = string[
            string.find("DTSTART:", i)
            + 8 : string.find("\n", string.find("DTSTART:", i) + 8)
        ]
        dTEnd = string[
            string.find("DTEND:", i)
            + 8 : string.find("\n", string.find("DTEND:", i) + 6)
        ]
        description = string[
            string.find("DESCRIPTION:", i)
            + 8 : string.find("\n", string.find("DTSTAMP:", i) + 12)
        ]
        location = string[
            string.find("LOCATION:", i)
            + 8 : string.find("\n", string.find("LOCATION:", i) + 9)
        ]
        summary = string[
            string.find("SUMMARY:", i)
            + 8 : string.find("\n", string.find("SUMMARY:", i) + 8)
        ]
        url = string[
            string.find("URL:", i) + 8 : string.find("\n", string.find("URL:", i) + 4)
        ]

        thing = Event(summary, dtStamp, dTStart, description, url)
        events.append(thing)

        i += 1
    (len(events))
    return events


calendar = open(
    "C:/Users/rober/OneDrive/Documents/codes/todoist_import_tasks/todoist_import_tasks/src/user_iyklUxW0TVScRN41qVL0lyh6ZGMhRkitpMX708L2.ics",
    "r+",
    encoding="utf-8",
)
calendar = icsToString(calendar)
events = stringToEvents(calendar)


class Root(Tk):
    def __init__(self):
        self.button = []
        super(Root, self).__init__()

        self.title("Python Tkinter")
        self.minsize(500, 400)

    def clicked(a, i):
        events[i].show()


root = Root()

cTableContainer = tk.Canvas(root)
fTable = tk.Frame(cTableContainer)
# sbHorizontalScrollBar = tk.Scrollbar(root)
sbVerticalScrollBar = tk.Scrollbar(root)


def updateScrollRegion():
    cTableContainer.update_idletasks()
    cTableContainer.config(scrollregion=fTable.bbox())


def createScrollableContainer():
    cTableContainer.config(
        # xscrollcommand=sbHorizontalScrollBar.set,
        yscrollcommand=sbVerticalScrollBar.set,
        highlightthickness=0,
    )
    # sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
    sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

    # sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    sbVerticalScrollBar.grid(column=1, row=0, sticky="NS")
    # cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
    # cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)


for i in range(len(events)):
    tk.Button(
        fTable,
        text=str(i + 1) + " " + events[i].getTitle(),
        command=lambda i=i: root.clicked(i),
    ).grid(column=2, row=i + 1)

    updateScrollRegion()

    # root.button.append(
    #     Button(
    #         fTable,
    #         text=str(i + 1) + " " + events[i].getTitle(),
    #         command=lambda i=i: root.clicked(i),
    #     )
    # )
    # root.button[i].grid(column=2, row=i + 1, sticky=W)


createScrollableContainer()


root.mainloop()
