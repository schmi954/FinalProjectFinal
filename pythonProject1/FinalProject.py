#initial dialogue
print("House music player")
print("\n")
print("Please select which option you would like")

logindic = {}

#This is the function for creating the dictionary username and password association
def making_dictionary(lgdic, username, password):
    lgdic[username] = password


#Create username and password function
def create_psswd():
    #Here is where user enters desired username and a password is created
    usernme = input("Please enter your desired username: ")
    y = usernme[0:2]
    t = usernme[3:]

    psswdfst = t + y
    psswdfst = psswdfst.replace("e", "z")
    psswdfst = psswdfst.replace("o", "f")

    #Here is where it write to the designated safe file to give you your password
    infile = input("What file would you like to receive your password in: ")
    f = open(infile, "w")
    f.write("Your password is: ")
    f.write("\n")
    f.write(psswdfst)
    f.close()
    #Here is where I will call the username and password association function
    #and store the users given username and password values in the dictionary
    updated_dic = {usernme: psswdfst}
    logindic.update(updated_dic)


def menu_structure():
    print("MENU-------------")
    print("1. Login")
    print("2. Create")
    print("3. Exit")

menu_structure()
choice = int(input("Please select an option:   "))

while choice != 3:
    if choice == 1:
        print("Choice 1")
    elif choice == 2:
        create_psswd()
    else:
        print("Please select one of the options")

    menu_structure()
    choice = int(input("Please select an option:   "))

print("Now exiting program goodbye !")
