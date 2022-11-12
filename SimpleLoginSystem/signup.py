import users


def add_user(database):
    # ask the user to enter new credentials
    new_username = input("Enter a username: ")
    new_password = input("Enter a password: ")
    # save database
    users.store_users()
    # stores user in database
    current_database = users.read_users()
    current_database[new_username] = new_password
