
############ code for CLI/API
import task_manager

def print_cmds():
    print('1. Add task\n' \
    '2. List tasks\n' \
    '3. Delete task\n' \
    '4. Exit\n')

def add_task(service):
    task=input('Enter task: ')
    success=service.add_task_logic(task)
    if success:
        print('Task added')
    else:
        print('Operation failed ')
    print()


def list_task(service):
    
    lst=service.get_tasks()
    if not lst:
        print('No tasks TODO\n')
        return
    
    for i in range(len(lst)):
        print(f'{lst[i].id}.',lst[i].title)
    print()
    
    
def delete_task(service):
    lst=service.get_tasks()
    if not lst:
        print('No tasks can be deleted. Task list empty\n')
        return
    for i in range(len(lst)):
        print(f'{lst[i].id}.',lst[i].title)
    print()
    
    print('\nEnter the task number to be deleted ')
    success=False
    while not success:
            task_no=input()
            success=service.delete_task_logic(task_no)
            if not success:
                print('Enter correct task number')
    print('task successfully deleted \n')
    print()

def CLI_APP(service):
    choice=0
    while True:
        print_cmds()
        choice=input('Enter choice ')
        if choice=='1':
            add_task(service)
        elif choice=='2':
            list_task(service)
        elif choice=='3':
            delete_task(service)
        elif choice=='4':
            print('Thanks for using App. Have a nice day!!')
            break
        else:
            print('Invalid choice!!!')
            print()

