from task_manager import TaskService
import cli

service=TaskService()
cli.CLI_APP(service)