import sys

userdata = ["", ""]


def login(username_data, passwords_data, username_, t):
    username_found = False
    username_idx = 0
    for l in username_data:
        line = ""
        for i in range(len(l) - 1):
            line += l[i]
        if username_ == line:
            username_found = True
        username_idx += 1
    if not username_found:
        print("This username doesn't exist, please try again : ")
        username_ = input("-> ")
        login(username_data, passwords_data, username_, t)

    userdata[0] = username_

    password = passwords_data[username_idx - 1]
    print("---------Login---------")
    print("Enter your password : ")
    password_input = input("-> ") + "\n"

    if password_input == password:
        print("Correct password, guaranteed access.")
    else:
        while password_input != password:
            print("Wrong password, please try again : ")
            password_input = input("-> ") + "\n"
        print("Correct password, guaranteed access.")

    userdata[1] = password_input

    text_system(username_data, username_idx)


def register(un, ulines, plines, data_):
    twin = 0
    for l in data_:
        line = ""
        for i in range(len(l) - 1):
            line += l[i]

        if un == line:
            twin += 1

    if twin > 0:
        print("This username already exist, please try again : ")
        username_ = input("-> ")
        while username_ == "":
            print("Invalid username, please try again : ")
            username_ = input("-> ")
        register(username_.lower(), ulines, plines, data_)
    else:
        print("---------Register---------")
        print("Enter a new password : ")
        password = input("-> ")
        while len(password) < 4:
            print("Your password needs to be at least 4 character long ! Please try again :")
            password = input("-> ")

        with open('usernames', 'a') as u:
            u.write(un + "\n")
        with open('passwords', 'a') as p:
            p.write(password + "\n")
        print("Username + password successfully added to username.txt.")


def text_system(ud, i):
    i -= 1
    print("-----" + userdata[0] + "-----")
    print("--- What do you want to do :")
    print("--- Modify your line plot - m")
    print("--- Read someone's line plot - r")

    command_ = input("-> ")

    while command_ != "m" and command_ != "r":
        print("Invalid command, please try again : ")
        command_ = input("-> ")

    if command_ == "m":
        try:
            with open("text", "r") as file:
                data = file.readlines()
                print("Enter your text here : ")
                data[i] = input("-> ")
            with open("text", "w") as file:
                file.writelines(data)
        except:
            print(i)

    else:
        print("The line of text from whom do you want to read ?")
        user = input("-> ")
        username_error = True
        while username_error:
            username_idx = 0
            for l in ud:
                line = ""
                for i in range(len(l) - 1):
                    line += l[i]
                if user == line:
                    username_error = False
                username_idx += 1

            if username_error:
                print("Error, this username doesn't exist, please try again : ")
                user = input("-> ")

        with open("text", "r") as file:
            data = file.readlines()
            print(data[username_idx - 1])


def create_files():
    try:
        open("usernames", "r")
        print("File 'usernames' successfully opened.")
    except:
        open("usernames", "w")
        print("File 'usernames' doesn't exist, new file created.")
    try:
        open("passwords", "r")
        print("File 'passwords' successfully opened.")
    except:
        open("passwords", "w")
        print("File 'passwords' doesn't exist, new file created.")
    try:
        open("text", "r")
        print("File 'text' successfully opened.")
    except:
        open("text", "w")
        print("File 'text' doesn't exist, new file created.")


def engine():
    try:
        create_files()
    except:
        print("Can't create essentials files, please don't run this program on an online compiler, etc...")
        sys.exit()

    f = open("usernames")
    usernames_data = f.readlines()
    f.close()
    f = open("passwords")
    passwords_data = f.readlines()
    f.close()
    f = open("text")
    t = f.readlines()
    f.close()

    with open(r"usernames", 'r') as fp:
        ulines = len(fp.readlines())
    with open(r"passwords", 'r') as fp:
        plines = len(fp.readlines())

    print("Type a command : \n--- l = login (connect to an account)\n--- r = register (create a new account)\n")
    command = input("-> ")
    while command != "l" and command != "r":
        print("Invalid command, please try again : ")
        print("\n")
        command = input("-> ")

    if command == "l":
        print("---------Login---------")
        print("Enter your username : ")
        username = input("-> ")
        login(usernames_data, passwords_data, username, t)
    else:
        print("---------Register---------")
        print("Create your new username : ")
        username = input("-> ")
        while username == "":
            print("Invalid username, please try again : ")
            username = input("-> ")
        register(username.lower(), ulines, plines, usernames_data)
        engine()




engine()
