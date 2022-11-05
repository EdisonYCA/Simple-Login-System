import login as log
import signup
import users


def main():
    request = input("Would you like to sign up or login: ")
    if request == "login":
        log.login_credentials()
    elif request == "sign up":
        signup.add_user(users.database)
    else:
        print("Please enter a valid option ('login' or 'sign up').")


if __name__ == "__main__":
    users.store_users()
    main()
