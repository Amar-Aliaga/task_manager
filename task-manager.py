import json
import argparse
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_task ():
    """Load task from JSON file"""
    try:
        with open (TASK_FILE, 'r') as file:
            return json.load (file)
    except FileNotFoundError:
        return []

def save_task (task):
    """Save task to a JSON file"""
    with open (TASK_FILE, 'w') as file:
        return json.dump (task, file, indent = 4)
    
def add_task (description = 'Default', due_date = '2026-01-01', priority = 'Medium'):
    """Add a new task"""
    task = load_task ()
    description = input ("Description: ")
    while True:
        due_date = input ("Due Date (YYYY-MM-DD): ")
        try:
            datetime.strptime (due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    priority    = input ("Priority: ")

    new_task = {
        'description': description,
        'due_date'   : due_date,
        'priority'   : priority
    }

    task.append (new_task)
    save_task (task)
