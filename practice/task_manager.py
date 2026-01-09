
#### code for task manager

from TaskRepositoryInterface import Repository
from task import Task
import JSONTaskRepository
class TaskService:

    def __init__(self,repo:Repository):
        self.repo=repo

        
    def get_tasks(self):
        return self.repo.get_all_tasks()
    
    def generate_newid(self):
        if self.repo.isempty():
            return 1
        tasks=self.repo.get_all_tasks()
        return max(item.id for item in tasks)+1


    
    def add_task_logic(self,title):
        #create id, right now len(task_list)
        if not title.strip():
            return False
        new_id=self.generate_newid()
        task=Task(new_id,title)
        # self.task_list.append(task)
        # self.repo.save_tasks(self.task_list)
        self.repo.add_task(task)
        return True
    
        
    
    def delete_task_logic(self,id):
        try:
            id=int(id)
        except ValueError:
            return False

        # for i in range(len(self.task_list)): #search in list
        #     if self.task_list[i].id==id:
        #         break
        # else:
        #     return False
        # self.task_list.pop(i)
        # self.repo.save_tasks(self.task_list)
        # return True
        return self.repo.remove_task(id)
        


