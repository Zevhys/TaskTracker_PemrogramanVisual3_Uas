# 📝 Task Tracker System

[![Author](http://img.shields.io/badge/author-@Zevhys-blue.svg)](https://www.linkedin.com/in/rakha-djauhari/) ![Created](https://img.shields.io/badge/Created-23--Jan--2026-blue.svg) ![GitHub repo size](https://img.shields.io/github/repo-size/Zevhys/TaskTracker_PemrogramanVisual3_Uas) [![GitHub license](https://img.shields.io/github/license/Zevhys/quickCart-client)](https://github.com/Zevhys/TaskTracker_PemrogramanVisual3_Uas/blob/main/LICENSE) [![Issues Welcome](https://img.shields.io/badge/issues-welcome-brightgreen.svg)](https://github.com/Zevhys/TaskTracker_PemrogramanVisual3_Uas/issues) [![Pull Requests Welcome](https://img.shields.io/badge/pull%20requests-welcome-brightgreen.svg)](https://github.com/Zevhys/TaskTracker_PemrogramanVisual3_Uas/pulls)

A modern, modular desktop application designed to manage users, projects, and tasks efficiently. Built with **Python** and **PyQt5**, featuring a clean user interface and robust MySQL database integration.

## ✨ Features

- **User Management**: Create, edit, and manage user profiles.
- **Project Organization**: Group tasks into specific projects.
- **Task Tracking**: Track task status, due dates, and descriptions.
- **Sub-Tasks**: Break down complex tasks into smaller, manageable sub-tasks.
- **Tagging System**: Organize tasks with custom tags (Many-to-Many relationship).
- **PDF Reporting**: Generate and export data reports to PDF format with a single click.
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

### 1. Clone Repository

```bash
git clone https://github.com/Zevhys/TaskTracker_PemrogramanVisual3_Uas .
```

### 2. Database Setup

Create a new database named `task_tracker` in your MySQL server and import the necessary tables:

```sql
CREATE DATABASE task_tracker;

-- (Create tables for: users, projects, tasks, sub_tasks, tags, task_tags)
-- Ensure 'id' columns are set to AUTO_INCREMENT
```

### 3. Configure Connection

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

### 4. Run the Application

Execute the main file to launch the dashboard:

```bash
python main.py
```

# 📥 Contribution

Contributions are welcome! If you have suggestions for improvements or want to report an issue, feel free to open a pull request or create an issue. Thank you for helping to make this project better!

