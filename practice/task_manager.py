
#### code for task manager
from task_repository import TaskRepository 
from task import Task
class TaskService:
    
    
    def __init__(self):
        self.repo=TaskRepository()
        self.task_list=self.repo.load_tasks()

        
    def get_tasks(self):
        return self.task_list
        #return self.task_list
    
    def generate_newid(self):
        if not self.task_list:
            return 1
        return max(item.id for item in self.task_list)+1


    
    def add_task_logic(self,title):
        #create id, right now len(task_list)
        if not title.strip():
            return False
        new_id=self.generate_newid()
        task=Task(new_id,title)
        self.task_list.append(task)
        self.repo.save_tasks(self.task_list)
        return True
    
        
    
    def delete_task_logic(self,id):
        try:
            id=int(id)
        except ValueError:
            return False

        for i in range(len(self.task_list)):
            if self.task_list[i].id==id:
                break
        else:
            return False
        self.task_list.pop(i)
        self.repo.save_tasks(self.task_list)
        return True
        


