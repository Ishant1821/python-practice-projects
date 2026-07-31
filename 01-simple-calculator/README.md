# 🧮 Simple Python Calculator

> A clean, interactive command-line calculator performing essential arithmetic and custom operations in Python.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-CLI_Application-FF6F00?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

---

## ⚡ Overview

This project is a beginner-friendly command-line utility that prompts users for two numbers and an operation code (1–7), executing calculations via Python's standard arithmetic operators and conditional control structures.

---

## 🧩 Supported Operations

| Menu Option | Operation Name | Syntax / Symbol | Description |
| :---: | :--- | :---: | :--- |
| **1** | Addition | `+` | Sums two numerical values |
| **2** | Subtraction | `-` | Subtracts second number from first |
| **3** | Multiplication | `*` | Multiplies two numbers |
| **4** | Division | `/` | Standard floating-point division |
| **5** | Floor Division | `//` | Division rounded down to nearest integer |
| **6** | Exponentiation | `**` | Raises first number to the power of second |
| **7** | Modulus / Remainder | `%` | Computes the remainder of division |

---

## 🛠️ Key Concepts Learned

* 📥 **User Input Handling:** Reading input using `input()` and casting string data into numerical types (`int()` / `float()`).
* 🔀 **Control Flow:** Evaluating multi-branch user selections using `if-elif-else` blocks.
* ➕ **Arithmetic Operators:** Practical application of standard Python mathematical expressions.

---

## 💻 Code Snippet

```python
# Multi-branch conditional selection for menu choices
if c == "1":
    print("YOUR ANSWER IS-->", a + b)
elif c == "4":
    print("YOUR ANSWER IS-->", a / b)
elif c == "6":
    print("YOUR ANSWER IS-->", a ** b)
