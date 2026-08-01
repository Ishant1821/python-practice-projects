# 📋 Simple To-Do List Manager

> An interactive CLI task manager demonstrating list CRUD operations, enumerate indexing, and error handling in Python.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Data_Structures-FF6F00?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

---

## ⚡ Overview

A command-line task management utility that allows users to maintain an active list of items. Supports viewing formatted tasks, dynamically appending new tasks, and safely removing tasks by index with input validation.

---

## 🛠️ Key Concepts Learned

* 📜 **Dynamic Sequences:** Using Python `list` to store and manage collection items.
* ➕ **List Append:** Adding elements using `tasks.append()`.
* 🔢 **Enumeration:** Generating 1-based display indices using `enumerate(tasks, start=1)`.
* 🗑️ **Index Removal:** Popping items with `tasks.pop(index - 1)` while maintaining bounds checking.
* 🛡️ **Exception Handling:** Guarding input conversion with `try-except ValueError`.

---

## 💻 Output Preview

```text
📋 TO-DO LIST MANAGER
1. View Tasks
2. Add Task
3. Remove Task
4. Exit

Select an option (1-4) --> 2
Enter the new task --> Push code to GitHub
✅ Added: 'Push code to GitHub'