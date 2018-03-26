tasks_list = list()

def todo_manager():
    while(1):
        try:
            print("cosa vuoi fare?\n1 inserisci\n2 remove\n3 show\n4 exit")
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
        except ValueError:
            print("Valore inserito non riconosciuto, le possibilità sono 1,2,3,4")


def insert_task():
    print("What?")
    new_task = input();
    tasks_list.append(new_task)

def remove_task():
    print("Write the item to delete")
    to_be_deleted=input()
    try:
        tasks_list.remove(to_be_deleted)
    except ValueError:
        print("element not found!")
def show_tasks():
    if len(tasks_list) == 0:
        print("no tasks memorized yet")
        return
    tasks_list.sort()
    print(*tasks_list, sep='\n')



def main():
    todo_manager()
    return 0

if __name__ == "__main__":
    main()
