# 📝 To-Do List Manager

A simple command-line To-Do List application built using Python.  
This app allows you to manage tasks directly from the terminal.

---

## 🚀 Features

- ➕ Add a new task
- 📋 View all tasks
- ✅ Mark a task as completed
- 🗑 Delete a task
- ⚠️ Error handling for invalid input

---

## 📁 Project Structure
To-do-list-manager/
│
├── main.py # Entry point (menu + user interaction)
├── manager.py # Core logic (TaskManager class)
├── utils.py # Helper functions
└── storage/
├── init.py
└── file_handler.py # Handles task storage (in-memory)


---

## 🪜 Code Flow (How it works)

1. `main.py` shows menu and takes user input  
2. `TaskManager` (manager.py) processes actions  
3. `utils.py` helps with formatting, IDs, time  
4. `file_handler.py` manages task storage  

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py

