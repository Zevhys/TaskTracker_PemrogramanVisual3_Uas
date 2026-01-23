# 📝 Task Tracker System

A modern, modular desktop application designed to manage users, projects, and tasks efficiently. Built with **Python** and **PyQt5**, featuring a clean user interface and robust MySQL database integration.

## ✨ Features

- **User Management**: Create, edit, and manage user profiles.
- **Project Organization**: Group tasks into specific projects.
- **Task Tracking**: Track task status, due dates, and descriptions.
- **Sub-Tasks**: Break down complex tasks into smaller, manageable sub-tasks.
- **Tagging System**: Organize tasks with custom tags (Many-to-Many relationship).
- **Modern UI**: Clean, flat design using Qt Designer forms.
- **Modular Code**: Organized architecture (Separated Logic, UI, and Database).

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.x**
2. **MySQL Server** (XAMPP/WAMP)
3. **Python Libraries**:

```bash
pip install pymysql PyQt5
```

## 🚀 Installation & Setup

### 1. Database Setup

Create a new database named `task_tracker` in your MySQL server and import the necessary tables:

```sql
CREATE DATABASE task_tracker;

-- (Create tables for: users, projects, tasks, sub_tasks, tags, task_tags)
-- Ensure 'id' columns are set to AUTO_INCREMENT
```

### 2. Configure Connection

Open `koneksi.py` and update your database credentials:

```python
def create_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",        # Your MySQL Username
        password="",        # Your MySQL Password
        database="task_tracker",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection
```

### 3. Run the Application

Execute the main file to launch the dashboard:

```bash
python main.py
```
