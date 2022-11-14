import signup
import users
import login


def main():
    run = True

    print("Select one of the following options: \n" +
          "1. Sign Up\n" +
          "2. Login\n" +
          "3. Exit\n")

    while run:
        request = input("--> ")

        if request == "2":
            login_successful = login.validate_credentials(users.database)
            if login_successful:
                print("Login in successful.")
            else:
                print("Invalid credentials.")
        elif request == "1":
            signup.add_user(users.database)
        elif request == "3":
            users.store_users()
            run = False
        else:
            print("Enter a valid option.")

        print("\nEnter one of the following options to continue: \n" +
              "1. Sign Up\n" +
              "2. Login\n" +
              "3. Exit\n")


if __name__ == "__main__":
    print("Initializing Login System..\n")
    users.database = users.read_users()
    main()
    print("Thank you!")
