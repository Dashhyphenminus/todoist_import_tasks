
#from todoist_api_python.api import TodoistAPI





class Event:

    def __init__(self, title, date, time, description, url):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.url = url

    def show(self):
        print (self.title)


    # def addEvent(tag, self):
    #     api = TodoistAPI("")
    #     try:
    #         task = api.add_task(
    #             content = self.title,
    #             description = self.description,
    #             priority = 2,
    #             due = self.date
    #         )
    #         print(task)
    #     except Exception as error:
    #         print(error)
