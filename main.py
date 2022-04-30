#Main page, this is where we import from other files
#Import Packages



##########################################################
#Objects

##########################################################


#Query text line
exit == False
val = ""
def intro():
    print("Welcome to Project Eden, A space Colony Text ADventure Simulator")
    while True:
        val = input("Welcome to the main menu!" )
        print("\n")
        if val == 'Exit' or val == 'exit':
            quit()
        elif val =='help' or val =='Help':
            help_file = open("help.txt")
            file_contents = help_file.read()
            print(file_contents)
        # elif val == 'Start' or val == 'start':
        #     startGame()
        else:
            print("Command not recognized")        

intro()

    