# import importlib.util
# import sys
from todoist_api_python.api import TodoistAPI
import re


# # For illustrative purposes.
# name = 'todoist-api-python.api'

# if name in sys.modules:
#     print(f"{name!r} already in sys.modules")
# elif (spec := importlib.util.find_spec(name)) is not None:
#     # If you choose to perform the actual import ...
#     module = importlib.util.module_from_spec(spec)
#     sys.modules[name] = module
#     spec.loader.exec_module(module)
#     print(f"{name!r} has been imported")
# else:
#     print(f"can't find the {name!r} module")


class Event:
    def __init__(self, title, date, time, description, url):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.url = url

    def show(self):
        pass
        #print(self.title)


def icsToString(file):
    thing = file.read()
    thing = re.sub("\n ", "", thing)

    return thing


def stringToEvents(string):
    events = []
    events.append(Event("title", 100, 100, "description", "url"))

    i = 0
    while (i < len(string)):
        #print ("a")
        i = string.find("BEGIN:VEVENT", i)
        if (i == -1):
            break
        dtStamp = string[string.find("DTSTAMP:", i) + 8 : string.find("\n", string.find("DTSTAMP:", i) + 8)]
        uId = string[string.find("UID:", i) + 8 : string.find("\n", string.find("UID:", i) + 4)]
        dTStart = string[string.find("DTSTART:", i) + 8 : string.find("\n", string.find("DTSTART:", i) + 8)]
        dTEnd = string[string.find("DTEND:", i) + 8 : string.find("\n", string.find("DTEND:", i) + 6)]
        description = string[string.find("DESCRIPTION:", i) + 8 : string.find("\n", string.find("DTSTAMP:", i) + 12)]
        location = string[string.find("LOCATION:", i) + 8 : string.find("\n", string.find("LOCATION:", i) + 9)]
        summary = string[string.find("SUMMARY:", i) + 8 : string.find("\n", string.find("SUMMARY:", i) + 8)]
        url = string[string.find("URL:", i) + 8 : string.find("\n", string.find("URL:", i) + 4)]



        thing = Event(summary, dtStamp, dTStart, description, url)
        events.append (thing)
        
        i += 1

    print (events)
        
        

    events[0].show()


calendar = open("C:/Users/rober/OneDrive/Documents/codes/todoist_import_tasks/todoist_import_tasks/src/test.txt", "r+")
#print(icsToString(calendar))
calendar = icsToString(calendar)

stringToEvents(calendar)
