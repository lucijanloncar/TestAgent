#!/usr/bin/env python3
"""
Simple CLI Todo App
====================
A command-line interface to manage todos with add, list, and done commands.
Uses JSON file persistence for data storage.
"""

import argparse
import json
import os
from datetime import datetime


# Constants
TODOS_FILE = "todos.json"


def load_todos():
    """Load todos from the JSON file."""
    if not os.path.exists(TODOS_FILE):
        return {"todos": []}
    
    try:
        with open(TODOS_FILE, 'r') as f:
            data = json.load(f)
            return data
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not load todos.json. Starting fresh.")
        return {"todos": []}


def save_todos(data):
    """Save todos to the JSON file."""
    try:
        with open(TODOS_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except IOError as e:
        print(f"Error saving todos: {e}")
        return False


def add_todo(task):
    """Add a new todo item."""
    todos = load_todos()
    
    # Create new todo with unique ID and timestamp
    new_todo = {
        "id": len(todos["todos"]) + 1,
        "task": task,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    todos["todos"].append(new_todo)
    save_todos(todos)
    
    print(f"\n✓ Todo added: '{task}' (ID: {new_todo['id']})")
    return new_todo


def list_todos():
    """List all todo items in a formatted table."""
    todos = load_todos()
    tasks = todos["todos"]
    
    if not tasks:
        print("\n📝 No todos found. Add some with 'python todo_app.py add <task>'")
        return
    
    # Print header
    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Task':<40} {'Status':<10} {'Created':<20}")
    print("=" * 70)
    
    # Print each todo
    for todo in tasks:
        status = "✓ Done" if todo["completed"] else "⏳ Pending"
        created = todo.get("created_at", "N/A")[:19]
        print(f"{todo['id']:<5} {todo['task']:<40} {status:<10} {created:<20}")
    
    print("=" * 70)
    print(f"Total: {len(tasks)} task(s)")
    
    # Count completed
    completed_count = sum(1 for t in tasks if t["completed"])
    print(f"Completed: {completed_count}/{len(tasks)}")


def done_todo(arg=None):
    """Mark a todo item as completed. Accepts either a task ID (number) or partial task name."""
    todos = load_todos()
    
    if not todos["todos"]:
        print("\n📝 No todos found.")
        return
    
    # Find the todo by ID or partial task name match
    found_todo = None
    
    for todo in todos["todos"]:
        # First, try to match by ID (if arg is numeric)
        if arg is not None:
            try:
                if int(arg) == todo["id"]:
                    found_todo = todo
                    break
            except ValueError:
                pass
        
        # If no ID match, try partial task name match
        if found_todo is None and arg is not None:
            if arg.lower() in todo["task"].lower():
                found_todo = todo
                break
    
    if found_todo is None:
        print(f"\n❌ No todo found with ID '{arg}' or matching task name")
        return
    
    # Mark as completed
    found_todo["completed"] = True
    found_todo["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    save_todos(todos)
    
    print(f"\n✓ Todo marked as done: '{found_todo['task']}' (ID: {found_todo['id']})")


def main():
    """Main entry point with argparse setup."""
    parser = argparse.ArgumentParser(
        description="Simple CLI Todo App - Manage your tasks from the command line.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python todo_app.py add "Buy groceries"
  python todo_app.py list
  python todo_app.py done 1
  python todo_app.py done "Buy groceries"
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo item")
    add_parser.add_argument("task", help="The task description")
    add_parser.set_defaults(func=add_todo)
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all todo items")
    list_parser.set_defaults(func=list_todos)
    
    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a todo item as completed")
    done_parser.add_argument("id_or_name", nargs="?", help="Todo ID or partial task name")
    done_parser.set_defaults(func=done_todo)
    
    args = parser.parse_args()
    
    if hasattr(args, "func"):
        if hasattr(args, 'task'):
            args.func(args.task)
        elif hasattr(args, 'id_or_name'):
            args.func(args.id_or_name)
        else:
            args.func()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
