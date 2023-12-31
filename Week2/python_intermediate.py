import json
import os 
from datetime import datetime
import pdb

class Task:
    def __init__(self, task_id, description, due_date, completed=False):
        # Implement Task class attributes and constructor
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Due Date: {self.due_date}, Completed: {self.completed}"
        
class FileHandler:

    @staticmethod
    def read_tasks_from_file(filename):
        # list function
        task_list = []
        # Implement method to read tasks from a file
        try:
            with open(filename, 'r') as f:
                task_list_json = f.read().split(",\n")
                # print(task_list_json)
                task_list = map(json.loads,task_list_json)
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the file.")
        return task_list

    @staticmethod
    def write_tasks_to_file(filename, tasks):
        # Implement method to write tasks to a file

        try:
            with open(filename,'w') as wf:
                wf.write( ",\n".join( map( lambda x: json.dumps( vars( x ) ), tasks ) ) )              

        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the file.")

class TaskManager:
    def __init__(self, file_handler):
        # Implement TaskManager constructor
        self.file_handler = file_handler
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # Implement method to load tasks from a file using file_handler
        
        tasks = []
        task_jsons = FileHandler.read_tasks_from_file("task_list.txt")
        for task_json in task_jsons:
            task = Task(task_json['task_id'], task_json['description'], task_json['due_date'], task_json['completed'])
            tasks.append(task)
        
        return tasks

        # return map( lambda task_json: Task( task_json['task_id'], task_json['description'], task_json['due_date'], task_json['completed']), task_jsons )

    def save_tasks(self):
        # Implement method to save tasks to a file using file_handler
        FileHandler.write_tasks_to_file("task_list.txt", self.tasks)

    def add_task(self, description, due_date):
        # Implement method to add a new task to the task list
        # assign a task_id to the new task being added
        task = Task(len(self.tasks) + 1, description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_id):
        # Implement method to mark a task as completed
        self.tasks[task_id - 1].completed = True

    def list_tasks(self):
        # Implement method to display a list of tasks
        # print the tasks       
        for task in self.tasks:
            print(task)


def main():
    # Implement a simple command-line interface for user interaction
    new_Task_Manager_1 = TaskManager(FileHandler())
    new_Task_Manager_1.save_tasks()
    print("List of current tasks: ")
    new_Task_Manager_1.list_tasks()
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
