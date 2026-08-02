# 📊 Text Analyzer & Word Counter

> A Python utility for processing text strings, generating word frequencies via dictionaries, and computing structural text metrics.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Text_Processing-FF6F00?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)

---

## ⚡ Overview

This script takes user-supplied paragraphs or sentences and generates an instant analytical summary covering total characters, word counts, and maximum frequency detection.

---

## 🛠️ Key Concepts Learned

* ✂️ **String Methods:** Using `.lower()`, `.split()`, and `.replace()` for normalization and tokenization.
* 📖 **Frequency Dictionaries:** Tracking word counts using key-value pair mapping (`dict.get(key, default)`).
* 🔝 **Max Key Lookup:** Finding dictionary extrema via `max(frequency, key=frequency.get)`.

---

## 💻 Output Preview

```text
📊 TEXT ANALYZER & WORD COUNTER 📊
Please enter or paste your sentence/paragraph:

Python is fast and Python is easy

-----------------------------------
📈 ANALYSIS REPORT
-----------------------------------
🔤 Total Characters (with spaces)   : 33
🔤 Total Characters (without spaces): 28
📝 Total Words                      : 6
🔥 Most Frequent Word              : 'python' (2 times)
-----------------------------------