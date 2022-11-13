import signup
import users


def main():
    run = True

    print("Select one of the following options: \n" +
          "1. Sign Up\n" +
          "2. Login\n" +
          "3. Exit\n")

    while run:
        request = input("--> ")

        if request == "2":
            pass
        elif request == "1":
            signup.add_user(users.database)
        elif request == "3":
            run = False
        else:
            print("Enter a valid option.")

        print("Enter one of the following options to continue: \n" +
              "1. Sign Up\n" +
              "2. Login\n" +
              "3. Exit\n")


if __name__ == "__main__":
    print("Initializing Login System..\n")
    main()
    print("Thank you!")
