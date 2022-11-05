import login as log
import signup
run = True


def main():
    while run:
        request = input("Would you like to sign up or login: ")
        if request == "login":
            log.login_credentials()
            break
        elif request == "sign up":
            signup.add_user(log.database)
            break
        else:
            print("Please enter a valid option ('login' or 'sign up').")
            break


if __name__ == "__main__":
    main()
