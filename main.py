import sys
from storage import load_tasks, save_tasks
from tasks import add_task, list_tasks, done_task, delete_task

tasks = load_tasks()

if len(sys.argv) < 2:
    print("Использование: python main.py [команда] [аргументы]")
    print("Команды: add, list, done, delete")
    sys.exit()

if sys.argv[1] == 'add':
    if len(sys.argv) < 3: 
        print("Укажите текст задачи!")
        sys.exit()
    else:
        add_task(tasks, sys.argv[2])
        save_tasks(tasks)
        print('Добавлена новая задача!')

elif sys.argv[1] == 'list':
    print('Список задач:')
    list_tasks(tasks, show_all='--all' in sys.argv)

elif sys.argv[1] == 'done':
    if done_task(tasks,sys.argv[2]):
        save_tasks(tasks)
        print('Задача выполнена!')
    else:
        print('Задача с таким ID не найдена!')

elif sys.argv[1] == 'delete':
    if delete_task(tasks, sys.argv[2]):
        save_tasks(tasks)    
        print('Задача удалена!')
    else:
        print('Задача с таким ID не найдена!')

else:
    print(f'Неизвестная комманда: {sys.argv[1]}')
