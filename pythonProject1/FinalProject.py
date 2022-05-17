import webbrowser

#initial dialogue
print("House music player")
print("\n")
print("Please select which option you would like")

#Initial Dictionary
logindic = {}

#Here is my class where I store the video the user is able to watch if they are a member using the webbrowser library
class VideoClass:
    def __init__(self, url, urlfile):
        self.url = url
        self.urlfile = urlfile
#Here I am taking the users desired url and file to write to the file and then read from it using the url from the file
    def user_Video(self):
        z = open(self.urlfile, "w")
        z.write(self.url)
        z.close()
        j = open(self.urlfile, "r")
        videoselection = j.readline()
        webbrowser.open_new(videoselection)







#This is the function for creating the dictionary username and password association
def making_dictionary(lgdic, username, password):
    lgdic[username] = password



#Create username and password function
def create_psswd():
    #Here is where user enters desired username and a password is created
    usernme = input("Please enter your desired username: ")
    y = usernme[0:2]
    t = usernme[3:]

    #Here I mix up the letters a bit so that passwords are different from username
    psswdfst = t + y
    psswdfst = psswdfst.replace("e", "z")
    psswdfst = psswdfst.replace("o", "f")

    #Here is where it write to the designated safe file to give you your password
    infile = input("What file would you like to receive your password in:  ")
    f = open(infile, "w")
    f.write("Your password is: ")
    f.write("\n")
    f.write(psswdfst)
    f.close()
    #Here is where I will call the username and password association function
    #and store the users given username and password values in the dictionary
    updated_dic = {usernme: psswdfst}
    logindic.update(updated_dic)


#Here is where I check to see if the username and password exist in the dictionary
def login_structure():
    username = input("What is your username:  ")
    password = input("What is your password:  ")

    if username in logindic and logindic[username] == password:
        print("succesfully loged in")
    else:
        print("User does not exist")






#Here I print the opening menu structure
def menu_structure():
    print("MENU-------------")
    print("1. Login")
    print("2. Create")
    print("3. Exit")

#Here I call the menu structure and the first value for the user to select an option
menu_structure()
choice = int(input("Please select an option:   "))

#This is my decision structure that takes the users input from menu
while choice != 3:
    if choice == 1:
        login_structure()
        firsturl = input("Please enter in the Youtube Url you would like to play:  ")
        secondoutfile = input("Please enter in the file you would like to store the url in:  ")
        garfield = VideoClass(firsturl, secondoutfile)
        garfield.user_Video()


#If user selects choice 2 they create a new username and password
    elif choice == 2:
        create_psswd()
    else:
        print("Please select one of the options")

#Here I allow for the user to do the program again if they want to
    menu_structure()
    choice = int(input("Please select an option:   "))

print("Now exiting program goodbye !")
