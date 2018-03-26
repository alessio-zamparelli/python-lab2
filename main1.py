tasks_list = list()

def todo_manager:
    while(1):
        ch=int(input())
        if(ch==1):
            insert_task()
        elif (ch==2):
            remove_task()
        elif (ch==3):
            show_tasks()
        elif (ch==4):
            exit(0)
        else:
            print("error in input command! retry again")


def insert_task():
    print("What?")
    new_task = input();
    tasks_list.append(new_task)

def remove_task():
    print("Write the item to delete")
    to_be_deleted=input()
    try
        tasks_list.remove(to_be_deleted)
        catch
def show_tasks():


