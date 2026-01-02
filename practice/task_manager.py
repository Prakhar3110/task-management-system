
#### code for task manager

from task import Task
class TaskService:
    
    
    def __init__(self):
        self.task_list=[]


    
    def get_tasks(self):
        return self.task_list
    

    
    def add_task_logic(self,title):
        #create id, right now len(task_list)
        if not title.strip():
            return False
        task=Task(len(self.task_list)+1,title)
        self.task_list.append(task)
        return True
    
        
    
    def delete_task_logic(self,id):
        try:
            id=int(id)
            if id>len(self.task_list) or id<1:
                return False
        except ValueError:
            return False

        self.task_list.remove(self.task_list[id-1])
        return True
        


