# 🤖 AI Command Tool (Python CLI Project)

## 📌 Overview
This is a simple but functional **Python-based AI Command Line Tool** that allows users to interact with text, generate summaries, and fetch real-time quotes using external APIs.

It demonstrates:
- Python fundamentals in a real system
- API integration using `requests`
- Error handling and fallback mechanisms
- CLI-based interaction flow

---

## ⚙️ Features

- Accepts user input text
- Stores and displays data
- Generates simple text summaries
- Fetches real-time quotes from APIs
- Handles API failures gracefully
- Runs in continuous command mode (CLI)

---

## 🧠 Commands Available

When you run the tool:

```
input     → Enter your text
summarize → Generate a short summary
quote     → Get a random quote (API-based)
show      → Display stored data
exit      → Close the tool
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install requests
```

### 2. Run the program
```bash
python ai_command_tool.py
```

---

## 📦 Dependencies

- requests

(Other libraries are auto-handled by pip)

---

## 🧪 Example Usage

```
Enter command: input
Enter your text: I am learning Python for internships
Text saved!

Enter command: summarize
Summary: I am learning Python...

Enter command: quote
"Discipline beats motivation."
```

---

## 🧠 What I Learned

- Working with Python functions and loops
- Handling JSON APIs
- Building CLI-based applications
- Error handling in real-world conditions
- Creating fallback systems for unstable APIs

---

## 📌 Future Improvements

- Add FastAPI backend version
- Add database storage (MongoDB / SQLite)
- Add authentication system
- Convert into web-based tool

---

## 👨‍💻 Author

Built as part of a 30-day internship preparation challenge focused on Python and backend development.