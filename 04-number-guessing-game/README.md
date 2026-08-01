# 🎯 Number Guessing Game

> An interactive CLI mini-game leveraging Python's `random` module, dynamic loop control, and input validation.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-CLI_Game-FF6F00?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

---

## ⚡ Overview

The program generates a pseudo-random integer between **1 and 100**. The user repeatedly submits guesses, receiving real-time feedback (`Too High`, `Too Low`, or `Out of Bounds`) until they identify the target number.

---

## 🛠️ Key Concepts Learned

* 🎲 **Randomization:** Utilizing `random.randint(a, b)` for dynamic value generation.
* 🔁 **Infinite Loops & State Tracking:** Keeping a `while True` loop open while accumulating an `attempts` counter.
* 🛡️ **Exception Handling:** Guarding against program crashes via `try-except ValueError` blocks.
* 🔀 **Condition Precedence:** Structuring bound checks prior to relative magnitude evaluations.

---

## 💻 Output Preview

```text
🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯
I'm thinking of a number between 1 and 100.

Enter your guess -> 50
📈 Too high! Try guessing a lower number.

Enter your guess -> 25
🎉 CONGRATULATIONS! You guessed it right in 2 attempt(s)!