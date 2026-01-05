import json
from task import Task
class TaskRepository:
    def __init__(self,filename="tasks.json"):
        self.filename=filename
    
    def load_tasks(self):
        ret_lst=[]
        try:
            with open(self.filename,'r') as f:
                data=json.load(f)
                for item in data:
                    ret_lst.append(Task(item['id'],item['title']))
        except FileNotFoundError:
            return ret_lst
        return ret_lst
    #store the tasks list into json file    
    def save_tasks(self,tasks):
        with open(self.filename,'w') as f:
            data=[]
            for item in tasks:
                data.append({"id":item.id,"title":item.title})
            json.dump(data,f,indent=4)