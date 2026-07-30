# 🔄 Python Loop Control Statements

> Master Python execution flow with `break`, `continue`, `pass`, and infinite event loops.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Control_Flow-FF6F00?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

---

## ⚡ Overview

Loop control statements alter the default flow of execution in Python loops. This project provides clean, runnable examples demonstrating how to short-circuit, skip, or placehold execution paths during loop cycles.

---

## 🧩 Key Concepts Explained

| Keyword | Action | Common Use Case |
| :--- | :--- | :--- |
| 🛑 **`break`** | Exits the loop immediately | Stopping an infinite loop when a condition/target is met |
| ⏭️ **`continue`** | Skips the current iteration & jumps to next | Filtering out unwanted items or invalid inputs |
| 🚧 **`pass`** | Null operation (does nothing) | Syntactic placeholder for unwritten functions/blocks |
| 🔁 **`while True`** | Runs continuously until explicitly stopped | Interactive CLI menus and event listeners |

---

## 💻 Code Highlights

```python
# 1. BREAK Example
for i in range(5):
    if i == 3: 
        break  # Loops stops completely at 3
    print(i)   # Outputs: 0, 1, 2

# 2. CONTINUE Example
for i in range(5):
    if i == 2: 
        continue  # Skips 2 and keeps going
    print(i)      # Outputs: 0, 1, 3, 4
