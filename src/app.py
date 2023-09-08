import importlib.util
import sys

# from todoist_api_python.api import TodoistAPI
import re

from tkinter import *
from tkinter.ttk import *


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

    print(events)

    return events


def clicked(event=Event):
    event.show()


calendar = open(
    "C:/Users/rober/OneDrive/Documents/codes/todoist_import_tasks/todoist_import_tasks/src/test.txt",
    "r+",
)
calendar = icsToString(calendar)
events = stringToEvents(calendar)


class Root(Tk):
    def __init__(self):
        self.button = []
        super(Root, self).__init__()

        self.title("Python Tkinter")
        self.minsize(500, 400)

        for i in range(len(events)):
            self.button.append(
                Button(
                    self,
                    text=str(i + 1) + events[i].getTitle(),
                    command=lambda i=i: self.clicked(i),
                )
            )
            self.button[i].grid(column=2, row=i + 1, sticky=W)


root = Root()
root.mainloop()
