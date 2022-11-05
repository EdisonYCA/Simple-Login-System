import users as us
import pickle


# ask user to enter credentials and validate credentials
def login_credentials():
    # Ask the user to login in using username AND password
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    validate_username(user_username, user_password)


# Search Dictionary for user credentials
def validate_username(username, password):
    # read current values in database
    users = us.read_users()

    for usernames in users:
        if usernames == username:  # if users username matches a value in database
            if password == users[username]:  # check if password matches the password for that username
                print("Login granted.")
                break
        else:  # if username or password did not match
            print("Invalid credentials.")
            break
