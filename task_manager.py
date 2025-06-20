# -*- coding: utf-8 -*-
"""Task_manager.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-9Bm_Yi_2aZ_d95Nix5HHZ-4nojjwUN2

## **Buggy Code**
"""

Here is some buggy Python code for a task manager. Can you identify the errors using only techniques from a beginner course (like print debugging)? Do not use any advanced tools.

# broken_task_manager.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    if index < len(tas):  # Error 1
        removed = tasks[index]
        del tasks[index]
        print(f"Removed: {removed}")
    else:
        print("Invalid index!")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, t in enumerate(task):  # Error 2
            print(f"{i+1}: {t}")

def main():
    add_task("Buy milk")
    add_task("Pay bills")
    add_task("Walk dog")
    list_tasks()
    remove_task(1)
    list_task()  # Error 3

if __name__ == "__main__":
    main()

"""# **Errors To Fix**"""

1. Line: `if index < len(tas):` → `tas` is undefined (should be `tasks`)
2. Line: `for i, t in enumerate(task):` → `task` is undefined (should be `tasks`)
3. Line: `list_task()` → Typo, function is called `list_tasks()`

"""# **Corrected Script**"""

# Section 2.2Corrected Task Manager Script

tasks = []  # list to store tasks

def add_task(task):
    """
    Add a task to the task list.

    >>> tasks.clear()
    >>> add_task("Test task")
    Added: Test task
    """
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    """
    Remove a task by its index in the list.

    >>> tasks[:] = ['A', 'B', 'C']
    >>> remove_task(1)
    Removed: B
    >>> remove_task(5)
    Invalid index!
    """
    if 0 <= index < len(tasks):
        removed = tasks[index]
        del tasks[index]
        print(f"Removed: {removed}")
    else:
        print("Invalid index!")

def list_tasks():
    """
    List all tasks currently in memory.

    >>> tasks[:] = ['X', 'Y']
    >>> list_tasks() # doctest: +SKIP
    1: X
    2: Y
    """
    if not tasks:
        print("No tasks available.")
    else:
        for i, t in enumerate(tasks):
            print(f"{i+1}: {t}")

def main():
    add_task("Buy milk")
    add_task("Pay bills")
    add_task("Walk dog")
    list_tasks()
    remove_task(1)
    list_tasks()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()

"""# **add_task()**"""

def add_task(task):
    """
    Adds a task to the global tasks list.

    >>> tasks.clear()
    >>> add_task("Finish homework")
    Added: Finish homework
    >>> tasks
    ['Finish homework']
    """
    tasks.append(task)
    print(f"Added: {task}")

"""## **remove_task()**"""

def remove_task(index):
    """
    Removes a task by index from the tasks list.

    >>> tasks[:] = ["A", "B", "C"]
    >>> remove_task(1)
    Removed: B
    >>> tasks
    ['A', 'C']

    >>> remove_task(5)
    Invalid index!
    """
    if 0 <= index < len(tasks):
        removed = tasks[index]
        del tasks[index]
        print(f"Removed: {removed}")
    else:
        print("Invalid index!")

"""## **list_tasks()**"""

def list_tasks():
    """
    Lists all tasks in the global list.

    >>> tasks[:] = ["Task 1", "Task 2"]
    >>> list_tasks() # doctest: +SKIP
    1: Task 1
    2: Task 2
    """
    if not tasks:
        print("No tasks available.")
    else:
        for i, t in enumerate(tasks):
            print(f"{i+1}: {t}")

"""## **display_menu()**"""

def display_menu():
    """
    Displays menu options to the user.

    >>> display_menu() # doctest: +SKIP
    1. Add Task
    2. List Tasks
    ...
    """
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")

"""## **get_user_choice()**"""

def get_user_choice():
    """
    Gets the user's menu choice.

    >>> get_user_choice() # doctest: +SKIP
    """
    choice = input("Enter choice: ").strip()
    return choice

"""## **main()**"""

def main():
    """
    Main loop for the Task Manager.

    >>> main() # doctest: +SKIP
    """
    # logic...

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()