import users


def add_user(database):
    # ask the user to enter new credentials
    new_username = input("Enter a username: ")
    new_password = input("Enter a password: ")
    # save new credentials in database
    database[new_username] = new_password
    print("Successfully signed up.\n")

