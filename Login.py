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
        elif not username or not email or not password:
            print("\nPlease fill in all fields. Try again.\n")
        else:
            print("\nInvalid credentials. Try again.\n")


check_email()