#Main page, this is where we import from other files
#Import Packages
from game import run
from game import ctnGame

# Main menu with simple options. 
def menu():
    print("Welcome to Project Eden, A space Colony Text Adventure Simulator")
    print("Type Help if you need any help")
    while True:
        print("Welcome to the main menu! \n")
        val = input("Your Answer: ").lower()
        if val == 'exit':
            quit()
        elif val =='help':
            help_file = open("mainMenuHelp.txt")
            file_contents = help_file.read()
            print(file_contents)
        elif val =='story':
            story_file = open("story.txt")
            file_contents1 = story_file.read()
            print(file_contents1)
        elif val == 'start':
            run()
            pass
        elif val == 'continue':
            ctnGame()
            pass
        else:
            print("Command not recognized")        

menu()

    
