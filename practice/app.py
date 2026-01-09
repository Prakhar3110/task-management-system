from task_manager import TaskService
import cli
import TaskRepositoryInterface
from JSONTaskRepository import JsonTaskRepository
repo=JsonTaskRepository()
success=repo.load() #to load from database to repository
if not success:
    print('Failed Database operation')
else:
    service=TaskService(repo)
    cli.CLI_APP(service)