

# 🔐 Password Strength Analyzer & Wordlist Generator

## 📌 Overview

This project is a **Password Strength Analyzer** and **Custom Wordlist Generator** built with Python.

It allows users to:

* ✅ Check password strength using entropy & classification
* ✅ Detect weaknesses (too short, sequences, repetitions, etc.)
* ✅ Get **suggestions** for stronger passwords
* ✅ Generate **custom wordlists** for testing
* ✅ Save results as **JSON** and wordlists to text files

---

## ⚙️ Installation

1. Clone the repository:

   ```
   git clone https://github.com/Karthik0779/password-strength-analyzer.git
   cd password-strength-analyzer
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv .venv
   .\.venv\Scripts\activate   # On Windows
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 🔎 Analyze Password Strength

Analyze directly:

```
python -m password_tool.cli analyze -p "P@ssw0rd123!"
```

Secure hidden input:

```
python -m password_tool.cli analyze --stdin
```

Detailed breakdown:

python -m password_tool.cli analyze -p "StrongPass!2025" --detailed
```

Save results as JSON:

python -m password_tool.cli analyze -p "StrongPass!2025" --json result.json
```

---

### 📝 Generate Custom Wordlist

Print to screen:

python -m password_tool.cli wordlist --seeds demo project security --max 20
```

Save to file:

```
python -m password_tool.cli wordlist --seeds demo project security --max 50 -o wordlist.txt
```

---

## 📊 Example Output

```
Password Analysis Result:
  Password: 12345
  Length: 5
  Entropy: 16.61 bits
  Strength: Very Weak
  Issues: Too short, Contains sequence

Suggestions:
  - Use at least 12 characters.
  - Avoid predictable sequences like 1234 or abcd.
  - Mix uppercase, lowercase, numbers, and symbols.

Detailed Report:
  Contains Uppercase: False
  Contains Lowercase: False
  Contains Digits: True
  Contains Special: False
```

---

## 📂 Project Structure

```
password-strength-analyzer/
│── password_tool/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── wordlist.py
│   ├── cli.py
│── README.md
│── requirements.txt
```

---

## ✅ Features

* Strength levels: **Very Weak → Very Strong**
* Entropy calculation
* Weakness detection (length, sequences, repetition)
* Suggestions for improvement
* JSON export option
* Wordlist generator with file saving

---

## 🛠️ Tools Used

* **Python 3.10+**
* **argparse** – CLI parsing
* **getpass** – Secure password input
* **colorama** – Colored output

---

## 📌 License

This project is for **educational and internship purposes only**.
Not intended for malicious use.

---
