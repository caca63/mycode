userdata = ["", ""]


def login(username_data, passwords_data, username_):
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
        username_ = input("This username doesn't exist, please try again : ")
        login(username_data, passwords_data, username_)

    userdata[0] = username_

    password = passwords_data[username_idx - 1]
    print("---------Login---------")
    password_input = input("Enter your password : ") + "\n"

    if password_input == password:
        print("Correct password, guaranteed access.")
    else:
        while password_input != password:
            password_input = input("Wrong password, please try again : ") + "\n"
        print("Correct password, guaranteed access.")

    userdata[1] = password_input


def register(un, ulines, plines, data_):
    twin = 0
    for l in data_:
        line = ""
        for i in range(len(l) - 1):
            line += l[i]

        if un == line:
            twin += 1

    if twin > 0:
        username_ = input("This username already exist, please try again : ")
        while username_ == "":
            username_ = input("Invalid username, please try again : ")
        register(username_.lower(), ulines, plines, data_)
    else:
        print("---------Register---------")
        password = input("Enter a new password : ")
        while len(password) < 4:
            password = input("Your password needs to be at least 4 character long ! Please try again :")

        with open('usernames', 'a') as u:
            u.write(un + "\n")
        with open('passwords', 'a') as p:
            p.write(password + "\n")
        print("Username + password successfully added to username.txt.")


def text_system():
    # to do
    pass


def engine():
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

    f = open("usernames")
    usernames_data = f.readlines()
    f.close()

    f = open("passwords")
    passwords_data = f.readlines()
    f.close()

    with open(r"usernames", 'r') as fp:
        ulines = len(fp.readlines())
    with open(r"passwords", 'r') as fp:
        plines = len(fp.readlines())

    print("Type a command : \n--- l = login (connect to an account)\n--- r = register (create a new account)")
    command = input("\n")
    while command != "l" and command != "r":
        print("Invalid command, please try again : ")
        command = input("\n")

    if command == "l":
        print("---------Login---------")
        username = input("Enter your username : ")
        login(usernames_data, passwords_data, username)
    else:
        print("---------Register---------")
        username = input("Create your new username : ")
        while username == "":
            username = input("Invalid username, please try again : ")
        register(username.lower(), ulines, plines, usernames_data)
        engine()

    text_system()


engine()
