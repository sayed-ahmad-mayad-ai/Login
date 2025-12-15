def GUI(NAME):
    print(f"""
          |---------------------------------|
          |                                 |
          |        Welcome to the GUI       |
          |        Calculator {NAME}        |
          |                                 |
          |---------------------------------|
          """)


def check_email():
    while True:
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if username == "admin" and email == "admin@example.com" and password == "password":
            print("\nLogin successful!")
            GUI(username)
            break
        else:
            print("\nInvalid credentials. Try again.\n")


check_email()