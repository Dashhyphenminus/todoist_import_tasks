import tkinter as tk

import requests

import importlib.util
import sys

# from todoist_api_python.api import TodoistAPI
import re


header = {"Authorization": "Bearer 9eb747d74cc4d5ad6c5a9b506bc4761b6e6005d6"}

# print(
#     requests.get(
#         "https://api.todoist.com/rest/v2/projects",
#         headers=header
#         # params={"Authorization: Bearer 9eb747d74cc4d5ad6c5a9b506bc4761b6e6005d6"},
#     )
# )


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
    # events.append(Event("title", 100, 100, "description", "url"))

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


#######################################################

url = "https://api.todoist.com/rest/v2/projects"
dat = {"content": "Buy Milk"}
header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 9eb747d74cc4d5ad6c5a9b506bc4761b6e6005d6",
}
requests.post(url, data=dat, headers=header)


root = tk.Tk()

# Tkinter widgets needed for scrolling.  The only native scrollable container that Tkinter provides is a canvas.
# A Frame is needed inside the Canvas so that widgets can be added to the Frame and the Canvas makes it scrollable.
cTableContainer = tk.Canvas(root)
fTable = tk.Frame(cTableContainer)
sbHorizontalScrollBar = tk.Scrollbar(root)
sbVerticalScrollBar = tk.Scrollbar(root)


# Updates the scrollable region of the Canvas to encompass all the widgets in the Frame
def updateScrollRegion():
    cTableContainer.update_idletasks()
    cTableContainer.config(scrollregion=fTable.bbox())


# Sets up the Canvas, Frame, and scrollbars for scrolling
def createScrollableContainer():
    cTableContainer.config(
        xscrollcommand=sbHorizontalScrollBar.set,
        yscrollcommand=sbVerticalScrollBar.set,
        highlightthickness=0,
    )
    sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=cTableContainer.xview)
    sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

    sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
    cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
    cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)


# Adds labels diagonally across the screen to demonstrate the scrollbar adapting to the increasing size
i = 0

for i in range(len(events)):
    tk.Button(
        fTable,
        text=str(i + 1) + " " + events[i].getTitle(),
        command=lambda e=events[i]: e.show(),
    ).grid(column=1, row=i)

    updateScrollRegion()


def addNewLabel():
    global i
    tk.Button(fTable, text="Hello World", command=lambda i=i: print(i)).grid(
        row=i, column=i
    )
    i += 1

    # Update the scroll region after new widgets are added
    updateScrollRegion()

    if i < 15:
        root.after(20, addNewLabel)


createScrollableContainer()
# addNewLabel()

root.mainloop()
