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

        if username and email  and password :
            print("\nLogin successful!")
            GUI(username)
            break
        elif not username.isalnum():
            print("\nUsername must be alphanumeric. Try again.\n")
        elif len(username) < 3:
            print("\nUsername must be at least 3 characters long. Try again.\n")
        elif len(password) < 6:
            print("\nPassword must be at least 6 characters long. Try again.\n")
        elif "@" not in email or "." not in email:
            print("\nInvalid email format. Try again.\n")
        elif not username or not email or not password:
            print("\nPlease fill in all fields. Try again.\n")
        else:
            print("\nInvalid credentials. Try again.\n")


check_email()