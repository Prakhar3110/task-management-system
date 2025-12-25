def print_cmds():
    print('1. Add task\n' \
    '2. List tasks\n' \
    '3. Delete task\n' \
    '4. Exit\n')

def add_task(tasks):
    task=input('Enter task: ')
    tasks.append(task)
    print('Task added')
    print()

def list_task(tasks):
    if not tasks:
        print('No tasks TODO\n')
        return
    for i in range(len(tasks)):
        print(f'{i+1}.',tasks[i])
    print()
    
    
def delete_task(tasks):
    if not tasks:
        print('No tasks can be deleted. Task list empty\n')
        return
    list_task(tasks)
    print('\nEnter the task number to be deleted ')
    while True:
        try:
            task_no=int(input())
            if task_no>len(tasks) or task_no<1:
                print('Enter valid task number\n')
                continue
        except ValueError:
            print('Enter task number\n')
            continue
        
        break
    tasks.remove(tasks[task_no-1])
    print('task successfully deleted \n')
    print()


def CLI_APP():
    choice=0
    tasks=[]
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