import users as us
import pickle


# ask user to enter credentials and validate credentials
def login_credentials():
    # Ask the user to login in using username AND password
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    validate_username(user_username, user_password, us.database)


# Search Dictionary for user credentials
def validate_username(username, password, database):
    # read current values in database
    for usernames in database:
        print(f"Trying to match: {usernames} with {username}")
        if usernames == username:  # if users username matches a value in database
            print(f"Found a match: {usernames} with {username}")
            if password == database[username]:  # check if password matches the password for that username
                print(f"Found a match: {password} with {database[username]}")
                return True
    return False
