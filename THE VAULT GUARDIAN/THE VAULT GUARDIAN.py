import hashlib

data_base = {}

def create_hash(password):
    resulting_hash = hashlib.sha256(password.encode()).hexdigest()
    return resulting_hash

def create_user():
    user = input("Insert your username: ")
    password = input("Insert your password: ")
    data_base[user] = create_hash(password)
    print("User created.")

    
def login():
    try_max = 3
    tries = 0

    print("---LOGIN---")
    while True:
       
        insert_user = input("User: ")
        if insert_user in data_base:
            print("Correct username. ")
            break
        else:
            print("Incorrect user, please try again.")
            continue
    
    while tries < try_max:
        current_attempt = tries + 1
        insert_password = input(f"Password ({current_attempt}/{try_max}): ")

        new_hash = create_hash(insert_password)
        if new_hash == data_base[insert_user]:
            print("Access authorized.")
            break

        else:
            tries += 1
            remaining = try_max - tries
            if remaining > 0:
                print(f"Wrong password. You have {remaining} tries left.")
            else:
                print("Maximum attempts exceeded. Your account has been blocked for security reasons.")
                
                
while True:
    print("---MENU---")
    print("1. Create user & password")
    print("2. Login")
    print("3. Check database")
    print("4. Exit")

    option = input("Please, select one of the options (1-4): ")

    if option == "1":
        create_user()
    elif option =="2":
        login()
    elif option =="3":
        print(f"This is database: {data_base}")
    elif option =="4":
        print("See you next time !")
        exit()
    else:
        print("Wrong option, please try again.")
        break


