from cryptography.fernet import Fernet

master_pwd = input("What is the master password? \n")



def add():
    name = input("Item Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            date = line.rstrip()
            user, passw = date.split("|")
            print("User:", user, "| Password:", passw)

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