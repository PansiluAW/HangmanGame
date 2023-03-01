#import modules
import random
import Words.Words
import Database.DatabaseMods
import HTMLDisplay.HTMLDisplay
import mysql.connector

#create variables
random_num = 0
name = ""
word = ""
turns_provided = 0
turns_used = 0
status = "" 
play_again = True
try_again = ""
delete = ""

#get player name from the user
name = str(input("Enter your name : "))

#display game title
print("_"*52)
print("\n","!! Let's Play the Hangman Game !!".center(50,"_"),"\n")

#choose a random word stored in the packages created
while play_again == True:
    random_num = random.randint(1,20)

    word_output = Words.Words.function_words(random_num)

    #store game data into relevant variables
    word = word_output[0]
    turns_provided = word_output[1]
    turns_used = word_output[2]
    status = word_output[3]

    #database (modifications)
    #store player records
    while True:
        try:
            Database.DatabaseMods.store(name,word,turns_provided,turns_used,status)
        except mysql.connector.Error :
            print()
            print("XAMP Server with the PHPMyAdmin has not started yet...\nPlease check if the XAMP Server is up with the PHPMyAdmin running.")
            print()
        else:
            break

    #ask user whether to display the recorded game history
    print()
    display = str(input("Do you want to see the recorded game history ? (Yes/No) : "))
    if display.lower() == 'yes':
        while True:
            try:
                Database.DatabaseMods.display()
            except mysql.connector.Error :
                print()
                print("XAMP Server with the PHPMyAdmin has not started yet...\nPlease check if the XAMP Server is up with the PHPMyAdmin running.")
                print()
            else:
                break
    elif display.lower() == 'no':
        pass
    else:
        print(" Invalid response given !! \n Response recorded as 'No'")

    #ask user whether needs to display the records of play history
    print()
    records_display = str(input("Do you want to see the detailed record history ? (Yes/No) :"))
    if records_display.lower() == "yes":
            while True:
                try:
                    HTMLDisplay.HTMLDisplay.html()
                except mysql.connector.Error :
                    print()
                    print("XAMP Server with the PHPMyAdmin has not started yet...\nPlease check if the XAMP Server is up with the PHPMyAdmin running.")
                    print()
                else:
                    break
            print("_____Opening Web Browser to show the Result Sheet_____")
    elif records_display.lower() == "no":
        pass
    else:
        print(" Invalid response given !! \n Response recorded as 'No'")
    
    #ask user whether the game needs to played again
    print()
    try_again = str(input("Do you want to try again ? (Yes/No) : "))
    #process accordingly
    if try_again.lower() == 'yes':
        play_again = True
        print("_"*52)
        print("\n","!! Let's Play Again !!".center(50,"_"),"\n")
    elif try_again.lower() == 'no':
        print("_"*52)        
        print("\n","!! Thank You For Playing !!".center(50,"^"),"\n")
        print("-"*52)        
        play_again = False
        
    else:
        print()
        print(" Invalid response given !! \n Response recorded as 'No'")
        print("_"*52)        
        print("\n","!! Thank You For Playing !!".center(50,"^"),"\n")
        print("-"*52)
        play_again = False
        
        
