tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
def uncompleted_tasks(task_list):
    for task in task_list:
        if task['completed']==False:
            print(task['description'])

def completed_tasks(task_list):
    for task in task_list:
        if task['completed']==True:
            print(task['description'])


def print_descriptions(task_list):
    for task in task_list:
        print(task['description']) 

def time_taken(task_list):
    for task in task_list:
        if task['time_taken']>10 and task['completed']==True:
            print(task['description'])

def find_description(task_list):
    user_input=input("Please enter a task description\n")
    print(' ')
    for task in task_list:
        if user_input==task['description']:
            print(f"There is a task with that description:\n")
            print(task['description'])
            print(f"Task has been done: {task['completed']}")
            print(f"Time taken: {task['time_taken']} minutes")
        
            
         

print("Tasks Uncompleted:\n")
tasks_uncompleted=uncompleted_tasks(tasks)
print(' ')
print("Tasks completed:\n")
tasks_completed=completed_tasks(tasks)
print(' ')
print('Task descriptions:\n')
desc=print_descriptions(tasks)
print(' ')
print('Task completed within 10 minutes:\n')
time_taken(tasks)
print(' ')
print('Find task by description:\n')
find_description(tasks)
print(' ')
print('Extension:\n')

#Extension
# Given a description update that task to mark it as complete.
def mark_complete(task_list):
    user_input=input("Please enter a task description\n")
    print(' ')
    for task in task_list:
        if user_input==task['description']:
            task['completed']=True
            print(f"Task {task['description']} has been completed")
            
        


mark_complete(tasks)

# Add a task to the list
def add_tasks(task_list):
    task_list.append({
        'description':'Make Bed',
        'completed':True,
        'time_taken':20
    })

add_tasks(tasks)
print(tasks[5])

#Advanced Extension
def menu(tasks):
    print('')
    print('Advanced Extension')
    print('')
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
    user_input=''
    choice=1

    while choice==1:
        print('')
        user_input=input('Select an item on the menu(ie. "1")\n')

        if user_input=="1":
            print_descriptions(tasks)
        elif user_input=="2":
            uncompleted_tasks(tasks)
        elif user_input=="3":
            completed_tasks(tasks)
        elif user_input=="4":
            mark_complete(tasks)
        elif user_input=="5":
            time_taken(tasks)
        elif user_input=="6":
            find_description(tasks)
        elif user_input=="7":
            add_tasks(tasks)
        elif user_input=="M" or user_input=="m":
            choice=0
            menu(tasks)
        elif user_input=="Q" or user_input=="q":
            choice=0
            break
        else:
            print('That was not an option on the menu, please try again')
            
menu(tasks)




# print('')
# print('Advanced Extension')
# print('')
# print("Menu:")
# print("1: Display All Tasks")
# print("2: Display Uncompleted Tasks")
# print("3: Display Completed Tasks")
# print("4: Mark Task as Complete")
# print("5: Get Tasks Which Take Longer Than a Given Time")
# print("6: Find Task by Description")
# print("7: Add a new Task to list")
# print("M or m: Display this menu")
# print("Q or q: Quit")
# user_input=''

# while user_input=='':
#     user_input=input('Select an item on the menu(ie. "1")')

#     if user_input=="1":
#         print_descriptions(tasks)
#     elif user_input=="2":
#         uncompleted_tasks(tasks)
#     elif user_input=="3":
#         completed_tasks(tasks)
#     elif user_input=="4":
#         mark_complete(tasks)
#     elif user_input=="5":
#         time_taken(tasks)
#     elif user_input=="6":
#         find_description(tasks)
#     elif user_input=="7":
#         add_tasks(tasks)
