#Main page, this is where we import from other files
#Import Packages
from game import run


##########################################################
#Objects

##########################################################


#Query text line

def menu():
    print("Welcome to Project Eden, A space Colony Text Adventure Simulator")
    print("Type Help if you need any help")
    while True:
        print("Welcome to the main menu! \n")
        val = input("Your Answer: ")
        if val == 'Exit' or val == 'exit':
            quit()
        elif val =='help' or val =='Help':
            help_file = open("help.txt")
            file_contents = help_file.read()
            print(file_contents)
        elif val =='story' or val =='Story':
            help_file = open("story.txt")
            file_contents = help_file.read()
            print(file_contents)
        elif val == 'Start' or val == 'start':
            run()
            pass
        else:
            print("Command not recognized")        

menu()

    