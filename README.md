# 🔍 PII Scanner

> A command-line tool that scans source code files to detect Personal Identifiable Information (PII) leaks — built to understand privacy engineering concepts used by companies like Privado AI.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 🚨 The Problem

Developers accidentally leak sensitive data in source code every day:
- Hardcoded passwords in config files
- API keys committed to GitHub
- Emails and phone numbers left in test files
- Credit card numbers in sample data

**PII Scanner detects all of this automatically.**

---

## ✅ What It Detects

| PII Type | Example |
|---|---|
| Email Address | `melody@gmail.com` |
| Phone Number | `+13207661354` |
| IP Address | `192.168.1.1` |
| Hardcoded Password | `password = "secret123"` |
| API Key / Token | `api_key = "sk-abc123..."` |
| Credit Card Number | `4111 1111 1111 1111` |

---

## 🛠️ Tech Stack

- Python 3.x (zero external dependencies)
- `re` — regex pattern matching
- `os` — file system traversal
- `argparse` — CLI argument parsing

---

## 📁 Project Structure
pii-scanner/
├── main.py          # Entry point, CLI arguments
├── scanner.py       # File reading and directory traversal
├── patterns.py      # PII regex detection rules
├── reporter.py      # Terminal + file report generation
└── test_files/      # Sample files with mock PII data

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/UtkarshaWaghmare101/pii-scanner.git
cd pii-scanner
```

**2. Scan a folder**
```bash
python main.py --path ./test_files
```

**3. Scan and save report**
```bash
python main.py --path ./test_files --output report.txt
```

---

## 📊 Sample Output
🔍 Scanning: ./test_files
Please wait...
============================================================
PII SCANNER — SCAN REPORT
Scan Time : 2026-05-28 18:14:55
Total Issues Found : 9
📄 FILE: test_files\sample_backend.py
Line    2  |  Email Address           |  email = "melody.doe@gmail.com"
Line    3  |  Hardcoded Password      |  password = "mysecret123"
Line    4  |  API Key / Token         |  api_key = "sk-abcdefghijklmnop..."
Line    5  |  Phone Number            |  phone = "13207661354"
Line    6  |  IP Address              |  ip = "192.168.1.1"
📄 FILE: test_files\sample_frontend.js
Line    2  |  Email Address           |  email: "jane.smith@company.com"
Line    3  |  Credit Card Number      |  credit_card: "4111 1111 1111 1111"
Line    5  |  IP Address              |  server: "192.168.0.105"
💾 Report saved to: report.txt

---

## 💡 How It Works

1. `main.py` accepts a folder path via CLI
2. `scanner.py` walks through every `.py`, `.js`, `.env`, `.json` file
3. `patterns.py` runs 6 regex rules against each line
4. `reporter.py` formats and prints the findings with file name + line number

---

## 🔗 Related

Built as part of learning **privacy engineering** — the same core concept behind tools like [Privado AI](https://privado.ai) which scans enterprise codebases for data flow and PII leaks at scale.

---

## 👩‍💻 Author

**Utkarsha Waghmare** — TY B.Tech CSE   
[GitHub](https://github.com/UtkarshaWaghmare101)