# 🎯 Word Replacement Game (FizzBuzz Variant)

> A custom variation of the classic "FizzBuzz" algorithmic problem evaluating modulo arithmetic and conditional precedence in Python.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Algorithms_&_Logic-FF6F00?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

---

## ⚡ Problem Logic

For numbers from **1 to 20**:
* If divisible by **both 4 and 5** (e.g., `20`), print **`"HOW ARE YOU"`**.
* Else if divisible by **4** (e.g., `4, 8, 12, 16`), print **`"HI"`**.
* Else if divisible by **5** (e.g., `5, 10, 15`), print **`"HELLO"`**.
* Otherwise, print the **number itself**.

---

## 🛠️ Key Concepts Learned

1. **Modulo Operator (`%`):** Used to check remainder after division. `num % 4 == 0` evaluates to `True` when `num` is a multiple of 4.
2. **Conditional Order Precedence:** The combined condition (`4 and 5`) **must** be evaluated first; otherwise, numbers like `20` would be caught by the single divisibility check earlier.
3. **`range()` Function:** Generates sequences from start to stop (exclusive end limit).

---

## 💻 Output Preview

```text
 1 --> 1
...
 4 --> HI
 5 --> HELLO
...
20 --> HOW ARE YOU