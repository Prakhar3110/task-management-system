from TaskRepositoryInterface import Repository
from task import Task 
import json
class JsonTaskRepository(Repository[Task]):
    def __init__(self,filename="tasks.json")->None:
        self.filename=filename
        self.task_list=[]
        
    
    def load(self):
        try:
            with open(self.filename,'r') as f:
                data=json.load(f)
                for item in data:
                    self.task_list.append(Task(item['id'],item['title']))
        except FileNotFoundError:
            return 0 
        return 1

    def get_all_tasks(self):
        return self.task_list
    
    def get_task_by_id(self):
        pass

    #store the tasks list into json file  
    def write_to_database(self):
        with open(self.filename,'w') as f:
            data=[]
            for item in self.task_list:
                data.append({"id":item.id,"title":item.title})
            json.dump(data,f,indent=4)

    def isempty(self):
        return not self.task_list

    def add_task(self,task:Task):
        self.task_list.append(task)
        self.write_to_database()

    def remove_task(self, id:int):
        for i in range(len(self.task_list)): #search in list
            if self.task_list[i].id==id:
                break
        else:
            return False
        self.task_list.pop(i)
        self.write_to_database()
        return True
        