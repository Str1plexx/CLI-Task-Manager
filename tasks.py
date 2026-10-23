from datetime import date

def add_task(tasks, title):
    # check len dict tasks, if tasks is empty, new ID = 1
    if not tasks:
        new_id = 1
    else:
        new_id = max(int(k) for k in tasks) + 1
    # create new task
    new_task = {
    'id': new_id,
    'title': title,
    'created_at': str(date.today()),
    'is_done': False
    }
    # add in tasks
    tasks[str(new_id)] = new_task
    
    return new_task 

def done_task(tasks, task_id):
    key = str(task_id)
    if key in tasks:
        tasks[key]['is_done'] = True
        return True
    else:
        return False

def delete_task(tasks, task_id):
    key = str(task_id)
    if key in tasks:
        del tasks[key]
        return True
    else:
        return False

def list_tasks(tasks, show_all = False):
    if not tasks:
        print("Список задач пуст!")
        return

    for task in tasks.values():
        if show_all or not task['is_done']:
            if task['is_done']:
                print(f'{task['id']}. [x] {task['title']} ({task['created_at']})')
            else:
                print(f'{task['id']}. [ ] {task['title']} ({task['created_at']})')
