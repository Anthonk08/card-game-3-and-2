#Main menu class of the game.
import colorama 
from colorama import Fore
import sys, os
from game import Game
import time

#Function that cleans the console.
def cleanConsole():
    clear = lambda: os.system("cls")
    clear()

#Main class which runs the game and the main menu from here are called the other classes.
class main:
    def __init__(self):
        cleanConsole()
        print(Fore.RED + "\n\t\t\t" + " ♥  ♦  ♣  ♠  "*4 , Fore.WHITE)
        print(Fore.GREEN + """
        \t\t\t    C A R D  G A M E  3  &  2 
        """ +Fore.WHITE)
        print(Fore.RED + "\t\t\t" + " ♥  ♦  ♣  ♠  "*4 , Fore.WHITE)
        print ("""\n\t\t\t\tC h o o s e   A n   O p t i o n : \n\n\t\t\t\t\t1 -- START. \n\n\t\t\t\t\t2 -- HELP. \n\n\t\t\t\t\t3 -- CLOSE
        """)
    
        optionMenu = input("\t\t\t\tA N S W E R : ") 
        if optionMenu == "1":
            #Here you must start the game by calling the Players class.
            self.playGame = Game()
            sys.exit()


        if optionMenu == "2":
            #After reading must return to the top of the menu.
            cleanConsole() 
            print (Fore.GREEN + "\n\n\t\t\tH O W   T O   P L A Y   I T ?" + Fore.WHITE)
            print(Fore.YELLOW + "\n1- Enter your name.\n\n2- Enter your last name.\n\n3- Several options will appear to be chosen each time it is your turn.\n\n4- You will have the option to keep a card from the deck and exchange it for one of your hand or discard the card from the deck.\n\n5- If you choose to change the card in the deck to one in the hand, your hand will appear:\n\n\t[7 Black Peak, 6 Black Peak, A Red Diamond, 2 Black Peak, 4 Black Peak]\n\n6- You must choose between the 5 cards you have, which you want to change, by typing a position of one of the 0-4 cards.\n\n7- He who has two equal cards of one and three equal cards of another will win.\n" +Fore.WHITE)
            print("-----"*22)
            print("\n\t\t\t\t A -- You want to go back to the menu?\n\n\t\t\t\t B -- Close the game?\n")
            validationOption = True
            
            #Options to return to the main menu option to back
            while validationOption:
                optionSelected = input("\t\t\t\t -- A N S W E R : ").upper()
                if optionSelected == "A":
                    main()
                if optionSelected == "B":
                    cleanConsole()
                    print (Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
                    print("""
            ---- ||  T h e   g a m e   w i l l   c l o s e,   w a i t   a   m o m e n t,   p l e a s e.  ||----
            """)
                    print(Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
                    validationOption = False
                else:
                    print("You have entered an incorrect character.\nChoose an A OR B option.")
        if optionMenu == "3":
            #Just present the message that the game is closing and closing.
            cleanConsole()
            print (Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
            print("""
            ---- ||  T h e   g a m e   w i l l   c l o s e,   w a i t   a   m o m e n t,   p l e a s e.  ||----
            """)
            print(Fore.RED + "\t\t\t\t\t《  《  《  《  《  《  》  》  》  》  》  》  " + Fore.WHITE)
            sys.exit()

        else:
            print(Fore.RED +"Error, you’ve entered an incorrect number.\nChoose an option of 1-3." + Fore.WHITE)
            time.sleep(0.8)
            main()
        
main()