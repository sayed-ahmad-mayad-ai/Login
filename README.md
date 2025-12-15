## Simple Python Login App 🧮✨

This project is a small Python script called `Login.py` that simulates a **login system** and shows a text-based welcome “GUI” with the username after a successful login.

It is ideal for:
- **Python beginners** who want to understand basic credential checking (username / email / password).
- **Developers** who want a minimal starting point before building a more advanced authentication system.

---

### 🌟 Features

- **User credential validation**: prompts for username, email, and password.
- **Custom welcome screen**: uses the `GUI(NAME)` function to display a neat text “frame” with the logged-in username.
- **Automatic retry on failure**: keeps asking for credentials until they are correct.
- **Clean and readable code**: easy to modify, extend, or use as a teaching example.

> Default login credentials in the code:
> - **Username**: `admin`  
> - **Email**: `admin@example.com`  
> - **Password**: `password`

You can change these values directly in `Login.py`.

---

### 🛠 Requirements

- **Python 3.x** installed on your system (Windows)

To confirm Python is installed:

```bash
python --version
```

If that doesn’t work, try:

```bash
py --version
```

---

### ▶️ How to Run on Windows

1. Open **PowerShell** or **Command Prompt**.
2. Navigate to the project directory:

```bash
cd "C:\Users\Glitc\OneDrive\Desktop\py"
```

3. Run the script:

```bash
python Login.py
```

If `python` doesn’t work, try:

```bash
py Login.py
```

The program will ask you to enter:
- **Username**
- **Email**
- **Password**

If the credentials are correct, you will see:
- **"Login successful!"**
- A styled welcome “GUI” that includes your username.

If the credentials are incorrect, you will see:
- **"Invalid credentials. Try again."**
- And the program will prompt you again.

---

### 🧩 Project Structure

- `Login.py`  
  Contains:
  - `GUI(NAME)`: displays a text-based welcome frame with the username.
  - `check_email()`: handles the login input loop and credential validation.
  - `check_email()` call at the bottom so the script runs immediately when executed.

---

### 💡 Ideas for Improvement

To make this project more advanced and production-like, you could:
- Connect it to a **database** of users.
- **Hash and salt passwords** instead of storing them as plain text.
- Build a graphical UI using **`tkinter`** or **`PyQt`**.
- Load credentials or settings from a config file such as `config.json`.

---

### 📌 Final Notes

- This is a great starting point for learning **user authentication basics** in Python.
- Feel free to modify the code, add new features, and update this `README.md` as your project grows.

