
#from todoist_api_python.api import TodoistAPI





class Event:

    def __init__(self, title, date, time, description, url):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.url = url

    # def addEvent(tag, self):
    #     api = TodoistAPI("9eb747d74cc4d5ad6c5a9b506bc4761b6e6005d6")
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
