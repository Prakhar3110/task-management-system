from task import Task
from abc import ABC,abstractmethod
from dataclasses import dataclass
from typing import TypeVar
class Repository[T](ABC):
    @abstractmethod
    def load(self):
        raise NotImplementedError
    @abstractmethod
    def isempty(self):
        raise NotImplementedError
    @abstractmethod
    def get_all_tasks(self):
        raise NotImplementedError
    
    @abstractmethod
    def add_task(self,task:Task):
        raise NotImplementedError
    
    @abstractmethod
    def remove_task(self,id:int|None):
        raise NotImplementedError