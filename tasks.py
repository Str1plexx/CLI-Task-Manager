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
