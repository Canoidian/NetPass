from cryptography.fernet import Fernet, InvalidToken

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key(master_pwd):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    key += master_pwd.encode()
    return key

master_pwd = input("What is the master password? \n")
write_key()
key = load_key(master_pwd)
fer = Fernet(key)

def add():
    name = input("Item Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            try:
                decrypted_passw = fer.decrypt(passw.encode())
                print("User:", user, "| Password:", str(decrypted_passw))
            except InvalidToken:
                print("User:", user, "| Password: Invalid token")


while True:
    mode = input("What are you here for? 1. Add new password 2. See all passwords (add, view) Press q to quit \n").lower()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "q":
        break
    elif mode == "clear":
        break
    else:
        print("Invalid input")
        continue
