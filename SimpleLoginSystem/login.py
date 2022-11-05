# Dictionary containing a list of user information
database = {"edison1278": "123", "micheal1278": "124", "jeremy1278": "125"}


# ask user to enter credentials and validate credentials
def login_credentials():
    # Ask the user to login in using username AND password
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")
    validate_username(user_username, user_password)


# Search Dictionary for user credentials
def validate_username(username, password):
    for usernames in database:
        if usernames == username:  # if users username matches a value in database
            if password == database[username]:  # check if password matches the password for that username
                print("Login granted.")
                break
        else:  # if username or password did not match
            print("Invalid credentials.")
            break
