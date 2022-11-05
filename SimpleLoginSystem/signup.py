def add_user(database):
    # ask the user to enter new credentials
    new_username = input("Enter a username: ")
    new_password = input("Enter a password: ")

    database[new_username] = new_password
