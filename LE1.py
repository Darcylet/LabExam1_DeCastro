movielib = {
    "Everything, Everywhere, All at Once": {"Quantity": 5, "Cost": 3},
    "Fight Club": {"Quantity": 6, "Cost": 4},
    "Past Lives": {"Quantity": 3, "Cost": 3},
    "Oppenheimer": {"Quantity": 5, "Cost": 4},
    "Barbie": {"Quantity": 6, "Cost": 4},
}
user_account = {"ale": {"password": "a", "balance": 0, "points": 0},
                "username": {"password": 'opa'}}

admin_username = "admin"
admin_password = "password"


def menu():
    while True:
        try:
            print("Welcome to the Movie Store!\n\n")
            print("1. Log in\n2. Sign up\n3. Admin Log in\n4. See available games\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                login()
            elif choice == 2:
                signup()
            elif choice == 3:
                admin()
            elif choice == 4:
                avgames()
            elif choice == 5:
                print("Thank you!")
        except ValueError as e:
            print("Invalid input")


def login():
    while True:
        try:
            print("Log in")
            username = input("Username: ")
            password = input("Password: ")
            if not username:
                menu()
            if user_account.get(username) and user_account[username]['password'] == password:
                print("Logged in successfully!")
                login_menu(username)
            else:
                print("Invalid username or password")

        except ValueError as e:
            print("Invalid input")


def signup():
    while True:
        try:
            balances = 0
            points = 0
            username = input("Create a username: ")
            if not username:
                menu()
            if username in user_account:
                print("Username already exists")
            password = input("Create a password: ")
            if len(password) < 8:
                print("Password must me at least 8 characters")
            if len(password) > 7:
                user_account[username] = {"password": password, "balance": balances, "points": points}
                print("Account created!")
                login_menu(username)
        except ValueError as e:
            print("Invalid input")


def admin():
    while True:
        try:
            print("Admin log in")
            username = input("Username: ")
            password = input("Password: ")
            if username == admin_username and password == admin_password:
                print("Logged in successfully!")
                admin_menu()
            else:
                print("Invalid username or password")
        except ValueError as e:

            print("Invalid input")


def avgames():
    print("Here is the catalog")
    print(movielib)
    a = input("press Enter to go back")
    if not a:
        menu()
    else:
        menu()


def login_menu(username):
    while True:
        try:
            print(f"Welcome {username}")
            print("1. Rent a movie\n2. Buy a Movie\n3. Check Balance\n4. Log-out")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                rentmovie(username)
            elif choice == 2:
                buymovie(username)
            elif choice == 3:
                balance(username)
            elif choice == 4:
                menu()
        except ValueError as e:
            print("Invalid input")


def balance(username):
    while True:
        try:
            print(f"Available Balance: {user_account[username]['balance']}")
            choice = str(input("Do you want to top up?(yes or no): "))
            if choice.lower() == "yes":
                topup(username)
            if choice.lower() == "no":
                login_menu(username)
        except ValueError as e:
            print("Invalid input")


def rentmovie(username):
    while True:
        try:
            print("Movie catalog:")
            print(f"{movielib}")
            choice = input(
                "Choose a movie\n 1. Everything, Everywhere, All at Once\n 2. Fight Club\n 3. Past Lives\n 4. Oppenheimer\n 5. Barbie\n(Type the name of the movie, Case sensitive): ")
            if choice not in movielib:
                print("movie not available")
            if not choice:
                rentmovie()
            if movielib[choice]['Quantity'] <= 0:
                print("Movie not available")
            if movielib[choice]['Quantity'] > 0:
                print("1. Pay using balance\n"
                      "2. Pay using points")
                payment = int(input("Enter your choice: "))
                if payment == 1:
                    if user_account[username]['balance'] <= movielib[choice]['Cost']:
                        print("not enough balance")
                    if user_account[username]['balance'] >= movielib[choice]['Cost']:
                        user_account[username]['balance'] -= movielib[choice]['Cost']
                        user_account[username]['points'] += 1
                        print(f"Movie successfully rented!\n Your new balance is {user_account[username]['balance']}\n"
                              f"1 point added to your account! Current account points is {user_account[username]['points']}\n"
                              "Please return the movie in 1 week!")
                        o = input("Press Enter to go back to menu")
                        if not o:
                            login_menu(username)
                        else:
                            login_menu(username)
                            continue
                if payment == 2:
                    print("You can rent any movie with 7 account points!")
                    if user_account[username]['points'] <= 7:
                        print("not enough points")
                    if user_account[username]['points'] >= 7:
                        user_account[username]['points'] -= 7
                        print(f"Movie successfully rented!\n Your new balance is {user_account[username]['balance']}\n"
                              f"Current account points is {user_account[username]['points']}\n"
                              "Enjoy your movie!")
                        o = input("Press Enter to go back to menu")
                        if not o:
                            login_menu(username)
                        else:
                            login_menu(username)

        except ValueError as e:
            print("Invalid input")


def topup(username):
    while True:
        try:
            print("Top up")
            print(f"Balance of {username} is: {user_account[username]['balance']}")
            topup_amt = float(input("how much do you want to top up?: "))
            user_account[username]['balance'] += topup_amt
            print(f"your new balance is {user_account[username]['balance']} ")
            c = input("Press enter to go back")
            if not c:
                login_menu(username)
            else:
                login_menu(username)

        except ValueError as e:
            print("Invalid input")


def buymovie(username):
    while True:
        try:
            print("Movie catalog:")
            print("to buy movies you have to pay an extra $3")
            print(f"{movielib}")
            choice = input(
                "Choose a movie\n 1. Everything, Everywhere, All at Once\n 2. Fight Club\n 3. Past Lives\n 4. Oppenheimer\n 5. Barbie\n(Type the name of the movie, Case sensitive): ")
            if choice not in movielib:
                print("movie not available")
            if not choice:
                rentmovie()
            if movielib[choice]['Quantity'] <= 0:
                print("Movie not available")
            if movielib[choice]['Quantity'] > 0:
                print("1. Pay using balance\n"
                      "2. Pay using points")
                payment = int(input("Enter your choice: "))
                if payment == 1:
                    if user_account[username]['balance'] <= movielib[choice]['Cost']:
                        print("not enough balance")
                    if user_account[username]['balance'] >= (movielib[choice]['Cost'] + 3):
                        user_account[username]['balance'] -= movielib[choice]['Cost']
                        user_account[username]['points'] += 3
                        print(f"Movie successfully bought!\n Your new balance is {user_account[username]['balance']}\n"
                              f"1 point added to your account! Current account points is {user_account[username]['points']}\n"
                              "Enjoy your movie!")
                        o = input("Press Enter to go back to menu")
                        if not o:
                            login_menu(username)
                        else:
                            login_menu(username)
                            continue
                if payment == 2:
                    print("You can buy any movie with 10 account points!")
                    if user_account[username]['points'] <= 10:
                        print("not enough points")
                    if user_account[username]['points'] >= 10:
                        user_account[username]['points'] -= 10
                        print(f"Movie successfully bought!\n Your new balance is {user_account[username]['balance']}\n"
                              f"Current account points is {user_account[username]['points']}\n"
                              "Enjoy your movie!")
                        o = input("Press Enter to go back to menu")
                        if not o:
                            login_menu(username)
                        else:
                            login_menu(username)
        except ValueError as e:
            print("Invalid input")


def admin_menu():
    while True:
        try:
            print("Welcome Admin!")
            print(
                "1. View movie catalog\n2. Add a new movie\n3. Add quantity of movie\n4. Change movie price\n5. Log out")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                adminavgames()
            if choice == 2:
                addmovie()
            if choice == 3:
                quantity_movie()
            if choice == 4:
                movie_price()
            if choice == 5:
                menu()
        except ValueError as e:
            print("Invalid input")


def adminavgames():
    print("Here is the catalog")
    print(movielib)
    a = input("press Enter to go back")
    if not a:
        admin_menu()
    else:
        admin_menu()


def addmovie():
    while True:
        try:
            admov = input("What movie do you want to add?: ")
            cost = int(input("How much is the movie?: "))
            quantity = int(input("How many copies?: "))
            if not admov:
                addmovie()
            else:
                movielib[admov] = {'Quantity': quantity, 'Cost': cost}
                print(f"Movie successfully added!\n {movielib}")
                a = input("press Enter to go back")
                if not a:
                    admin_menu()
                else:
                    admin_menu()
        except ValueError as e:
            print("Invalid input")


def quantity_movie():
    while True:
        try:
            add = input("Which movie do you want to add a copy to: ")
            if add not in movielib:
                print("Movie not in catalog")
            else:
                hm = int(input("How manu copies do you wish to add?: "))
                if hm <= 0:
                    print("Invalid number")
                if hm >= 0:
                    movielib[add]['Quantity'] += hm
                    print("Quantity successfully changed!")
                    a = input("Press Enter to go back")
                    if not a:
                        admin_menu()
                    else:
                        admin_menu()
        except ValueError as e:
            print("Invalid input")


def movie_price():
    while True:
        try:
            add = input("Which movie do you want to change price: ")
            if add not in movielib:
                print("Movie not in catalog")
            else:
                c = int(input("1. Increase price\n2. Decrease price\n Choice: "))
                if c == 1:
                    inc = int(input("By how much do you want to increase the price?: "))
                    movielib[add]['Cost'] += inc
                    print("Price successfully Changed!")
                    a = input("Press Enter to go back")
                    if not a:
                        admin_menu()
                    else:
                        admin_menu()
                if c == 2:
                    dec = int(input("By how much do you want to decrease the price?: "))
                    movielib[add]['Cost'] += dec
                    print("Price successfully Changed!")
                    a = input("Press Enter to go back")
                    if not a:
                        admin_menu()
                    else:
                        admin_menu()
        except ValueError as e:
            print("Invalid input")


menu()

#    while True:
#        try:

#        except ValueError as e:
#            print("Invalid input")
