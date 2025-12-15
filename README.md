## Simple Python Console Login App 🧮✨

This project is a small **Python** script in a single file, `Login.py`, that simulates a **console-based login system**
and prints a text-based “GUI-style” welcome screen containing the username after a successful login.

It is ideal for:
- **Python beginners** who want to practice user input and basic validation.
- **Students** who need a clear, minimal example for teaching input validation.
- **Anyone** looking for a simple starting point before building a more advanced authentication system.

---

### 🌟 Features

- **User input handling**: prompts the user to enter:
  - Username
  - Email
  - Password
- **Basic validation rules** before accepting the login:
  - Username must be alphanumeric (`isalnum`).
  - Username must be at least **3 characters** long.
  - Password must be at least **6 characters** long.
  - Email must contain both `@` and `.` (simple format check).
  - No field can be left empty.
- **Automatic retry**: if any validation fails, an appropriate error message is shown and the user is asked to try again.
- **Custom welcome screen**: after a successful login, the `GUI(NAME)` function prints a nice text “frame” containing the username.

> Note: there are **no fixed credentials** (like a hardcoded username/password) in the code.  
> Any input is accepted as long as it passes the validation rules above.

---

### 🛠 Requirements

- **Python 3.x** installed on your system (Windows is assumed in the examples).

To check if Python is installed:

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
2. Navigate to the project directory (adjust the path to where you saved the file):

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

4. The program will ask you to enter:
   - Username  
   - Email  
   - Password  

5. If all validation rules are satisfied, you will see:
   - The message **"Login successful!"**
   - A styled text-based welcome “GUI” that includes the username you entered.

6. If something is wrong, you will see a specific error message such as:
   - `Username must be alphanumeric`
   - `Password must be at least 6 characters long`
   - `Invalid email format`
   - Or a reminder not to leave fields empty  
   and the program will prompt you to enter the data again.

---

### 🧩 Project Structure

- `Login.py`
  - `GUI(NAME)`: prints a text-based frame with a welcome message and the username.
  - `check_email()`: contains an input loop that asks for user credentials and applies all validation rules.
  - A call to `check_email()` at the bottom of the file so the script starts immediately when executed.

---

### 💡 Ideas for Improvement

You can use this project as a starting point and extend it by:
- Connecting it to a real **user database** (e.g., SQLite, PostgreSQL, or MySQL).
- **Hashing passwords** instead of handling them as plain text.
- Building a graphical user interface (GUI) using **`tkinter`**, **`PyQt`**, or another GUI toolkit.
- Moving the validation logic into a separate module (e.g., `auth.py`) for better structure and reuse.
- Adding **unit tests** to verify the validation logic.

---

### 📌 Final Notes

This repository is mainly intended as a **learning and teaching example** for basic input validation in Python.
Feel free to modify, refactor, and expand it into a more realistic authentication system.

