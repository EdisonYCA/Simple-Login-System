import users
import users as us
import pickle


# Search database for user credentials and validate those credentials
def validate_credentials(database):
    # Ask the user to login in using username AND password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # read current values in database
    for usernames in database:
        if usernames == username:  # if users username matches a value in database
            if password == database[username]:  # check if password matches the password for that username
                return True
    return False
