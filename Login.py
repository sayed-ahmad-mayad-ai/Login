def GUI(NAME):
    print(f"""
      ||#################################||
      ||                                 ||
      ||        Welcome to the GUI       ||
      ||        Calculator {NAME}        ||
      ||                                 ||
      ||#################################||
    """)


def check_email():
    while True:
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if not username or not email or not password:
            print("\nPlease fill in all fields. Try again.\n")

        elif not username.isalnum():
            print("\nUsername must be alphanumeric. Try again.\n")

        elif len(username) < 3:
            print("\nUsername must be at least 3 characters long. Try again.\n")

        elif len(email) > 10:
            print("\nEmail must not exceed 10 characters. Try again.\n")

        elif len(password) < 6:
            print("\nPassword must be at least 6 characters long. Try again.\n")

        elif "@" not in email and "." not in email:
            print("\nInvalid email format. Try again.\n")

        else:
            print("\nLogin successful!\n\n")
            GUI(username)
            break


check_email()
