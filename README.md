# CLI Todo App 📝

A simple command-line interface to manage your daily tasks. Built with Python and argparse, using JSON for data persistence.

## Features ✨

- ✅ Add new tasks
- ✅ List all tasks in a formatted table
- ✅ Mark tasks as completed (by ID or task name)
- ✅ Persistent storage (todos.json)
- ✅ No external dependencies required

## Installation 🚀

1. Clone or download this repository
2. Ensure Python 3.6+ is installed
3. Run: `python todo_app.py --help`

No installation needed - just run the script!

## Usage 💻

### Add a new task
```bash
python todo_app.py add "Buy groceries"
```

### List all tasks
```bash
python todo_app.py list
```

### Mark a task as done (by ID)
```bash
python todo_app.py done 1
```

### Mark a task as done (by partial name)
```bash
python todo_app.py done "Buy groceries"
```

## Commands Reference 📚

| Command | Description | Example |
|---------|-------------|---------|
| `add <task>` | Add a new todo item | `python todo_app.py add "Walk the dog"` |
| `list` | Display all todos in table format | `python todo_app.py list` |
| `done [id\|name]` | Mark task as completed | `python todo_app.py done 1` |

## File Structure 📁

```
TestAgent/
├── todo_app.py      # Main application
├── todos.json       # Data file (auto-created)
├── requirements.txt # Dependencies (empty - stdlib only)
└── README.md        # This file
```

## How It Works 🔧

- **todo_app.py**: Main script with argparse CLI
- **todos.json**: Stores all tasks in JSON format
- Each task has: `id`, `task`, `completed`, `created_at`, `completed_at`

## License 📄

MIT License - Feel free to use and modify!
