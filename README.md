# BookBot

![version‑badge (optional)](https://img.shields.io/badge/version‑0.1.0-blue)  

**BookBot** is a lightweight Python command‑line utility that analyzes a plain‑text book and reports:

- **Word count**
- **Frequency of every character** (sorted, including non‑ASCII characters)
- Character counts in the exact format `'<char>': N` (with quotes) to support automated test harnesses

---

## ⚡ Features

- Prints usage info if no `<path_to_book>` is provided → **exit code 1**
- On success, exits with **code 0** after printing results
- Designed to work with Bootdev; expected substrings like `'t': 29493`, `'p': 5952`, `'c': 9011` are matched verbatim
- Minimal dependencies — only the Python standard library

---

## 🚀 Installation

1. Clone or copy the repository
2. Ensure a Python 3 interpreter (3.8+) is available

No third‑party packages needed.

---

## 🧪 Usage

```bash
python3 main.py <path_to_book>

