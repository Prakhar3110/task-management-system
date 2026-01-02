##### Data model layer
tasks=[]


##### Service layer functions
def add_task_logic(tasks,task):
     tasks.append(task)

def isempty_logic(tasks):
    return len(tasks)==0

def delete_task_logic(tasks,task_no):
    try:
        task_no=int(task_no)
        if task_no>len(tasks) or task_no<1:
            return False
    except ValueError:
            return False
            
    tasks.remove(tasks[task_no-1])
    return True
    

##### CLI/Interface
def print_cmds():
    print('1. Add task\n' \
    '2. List tasks\n' \
    '3. Delete task\n' \
    '4. Exit\n')

def add_task(tasks):
    task=input('Enter task: ')
    add_task_logic(tasks,task)
    print('Task added')
    print()


def list_task(tasks):
    
    if isempty_logic(tasks):
        print('No tasks TODO\n')
        return
    
    for i in range(len(tasks)):
        print(f'{i+1}.',tasks[i])
    print()
    
    
def delete_task(tasks):
    if isempty_logic(tasks):
        print('No tasks can be deleted. Task list empty\n')
        return
    list_task(tasks)
    print('\nEnter the task number to be deleted ')
    success=False
    while not success:
            task_no=input()
            success=delete_task_logic(tasks,task_no)

   
    print('task successfully deleted \n')
    print()

def CLI_APP():
    choice=0
    while True:
        print_cmds()
        choice=input('Enter choice ')
        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            list_task(tasks)
        elif choice=='3':
            delete_task(tasks)
        elif choice=='4':
            print('Thanks for using App. Have a nice day!!')
            break
        else:
            print('Invalid choice!!!')
            print()

CLI_APP()