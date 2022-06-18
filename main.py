#Main page, this is where we import from other files
#Import Packages
from game import run
from game import ctnGame

# Main menu with simple options. 
def menu():
    print("Welcome to Project Eden: A Text-Based Space Adventure")
    print("Type Help if you need any help")
    while True:
        print("Welcome to the main menu! \n")
        answer = input("Your Answer: ").lower()
        if answer == 'exit':
            quit()
        elif answer =='help':
            help_file = open("mainMenuHelp.txt")
            file_contents = help_file.read()
            print(file_contents)
        elif answer == 'start':
            run()
            pass
        elif answer == 'continue':
            ctnGame()
            pass
        else:
            print("Command not recognized")        

menu()

    
