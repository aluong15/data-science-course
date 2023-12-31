import json
import os

class Task:
    def __init__(self, task_id, description, due_date, completed=False):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Due Date: {self.due_date}, Completed: {self.completed}"
        
class FileHandler:

    def __init__( self, filename ): 
        self.filename = filename

    def read_tasks_from_file( self ):
        try:
            with open( self.filename, 'r' ) as f:
                return [ Task( **json.loads( line.strip("," + os.linesep ) ) ) for line in f.readlines() ]
        except FileNotFoundError:
            print( "Error: File not found." )
        except json.JSONDecodeError:
            print( "Error: Invalid JSON format in the file." )
        return []

    def write_tasks_to_file(self, tasks):
        try:
            with open( self.filename, 'w' ) as wf:
                wf.write( ",\n".join( [ json.dumps( vars( task ) ) for task in tasks ] ) )
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the file.")

class TaskManager:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        self.tasks = self.file_handler.read_tasks_from_file()

    def save_tasks(self):
        self.file_handler.write_tasks_to_file( self.tasks )

    def add_task(self, description, due_date):
        self.tasks.append( Task(len(self.tasks) + 1, description, due_date) )

    def mark_task_completed(self, task_id):
        self.tasks[task_id - 1].completed = True

    def list_tasks(self):
        for task in self.tasks:
            print(task)


# Whoops i think i overwrote task_list
def main():
    # Implement a simple command-line interface for user interaction
    new_Task_Manager_1 = TaskManager(FileHandler("task_list.txt"))
    #new_Task_Manager_1.save_tasks()
    print("List of current tasks: ")
    new_Task_Manager_1.list_tasks()
    # breakpoint()
    new_Task_Manager_1.mark_task_completed(1)
    print("Updated list.")
    new_Task_Manager_1.list_tasks()
    new_Task_Manager_1.add_task("Buy groceries", "2024-01-02")
    print("Added task to list.")
    new_Task_Manager_1.list_tasks()
    new_Task_Manager_1.save_tasks()
    print("Saved task list.")
    new_Task_Manager_1.list_tasks()


if __name__ == "__main__":
    main()
