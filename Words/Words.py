#function for the word 'book'
def function_words(random_num):
    "This is used when the word 'book' is used as the random word"
    #variables
    word = words[random_num]
    word_incomplete = blanks[random_num]
    turns_remain = turns[random_num]
    turns_provided = turns_remain
    turns_used = 0
    count = 0
    cont = True
    #display hint
    print("Hint :",hints[random_num])
    print()
    while cont == True:
        #check whether the turns are over or word is complete to proceed
        if "_" in word_incomplete and turns_remain !=0:
            if count == 0:
                print("Word :",blanks[random_num])
                print(turns_remain,"Turns remain")
                count +=1
            else:
                letter = str(input("Letter : "))
                word_incomplete = list(word_incomplete)

                #assigning the character to the relevant blank space
                #word 'Book'
                if random_num == 1 :
                    if letter.lower() == "b":
                        word_incomplete[0] = "b"
                    elif letter.lower() == "o":
                        word_incomplete[2] = "o"
                        word_incomplete[4] = "o"
                    elif letter.lower() == "k":
                        word_incomplete[6] = "k"
                    else:                    
                        turns_remain -= 1
                #word 'Bottle'
                elif random_num == 2 :
                    if letter.lower() == "b":
                        word_incomplete[0] = "b"
                    elif letter.lower() == "o":
                        word_incomplete[2] = "o"
                    elif letter.lower() == "t":
                        word_incomplete[4] = "t"
                        word_incomplete[6] = "t"                    
                    elif letter.lower() == "l":
                        word_incomplete[8] = "l"
                    elif letter.lower() == "e":
                        word_incomplete[10] = "e"                    
                    else:                    
                        turns_remain -= 1
                #word 'Camera'
                elif random_num == 3 :
                    if letter.lower() == "c":
                        word_incomplete[0] = "c"        
                    elif letter.lower() == "a":
                        word_incomplete[2] = "a"
                        word_incomplete[10] = "a"
                    elif letter.lower() == "m":
                        word_incomplete[4] = "m"
                    elif letter.lower() == "e":
                        word_incomplete[6] = "e"
                    elif letter.lower() == "r":
                        word_incomplete[8] = "r"
                    else:                    
                        turns_remain -= 1
                #word 'Cricket'
                elif random_num == 4 :
                    if letter.lower() == "c":
                        word_incomplete[0] = "c"
                        word_incomplete[6] = "c"
                    elif letter.lower() == "r":
                        word_incomplete[2] = "r"
                    elif letter.lower() == "i":
                        word_incomplete[4] = "i"
                    elif letter.lower() == "k":
                        word_incomplete[8] = "k"
                    elif letter.lower() == "e":
                        word_incomplete[10] = "e"    
                    elif letter.lower() == "t":
                        word_incomplete[12] = "t"
                    else:                    
                        turns_remain -= 1
                #word 'Cupboard'
                elif random_num == 5 :
                    if letter.lower() == "c":
                        word_incomplete[0] = "c"
                    elif letter.lower() == "u":
                        word_incomplete[2] = "u"
                    elif letter.lower() == "p":
                        word_incomplete[4] = "p"
                    elif letter.lower() == "b":
                        word_incomplete[6] = "b"
                    elif letter.lower() == "o":
                        word_incomplete[8] = "o"
                    elif letter.lower() == "a":
                        word_incomplete[10] = "a"
                    elif letter.lower() == "r":
                        word_incomplete[12] = "r"
                    elif letter.lower() == "d":
                        word_incomplete[14] = "d"
                    else:                    
                        turns_remain -= 1
                #word 'Eagle'
                elif random_num == 6 :
                    if letter.lower() == "e":
                        word_incomplete[0] = "e"
                        word_incomplete[8] = "e"
                    elif letter.lower() == "a":
                        word_incomplete[2] = "a"
                    elif letter.lower() == "g":
                        word_incomplete[4] = "g"
                    elif letter.lower() == "l":
                        word_incomplete[6] = "l"
                    else:                    
                        turns_remain -= 1
                #word 'Football'
                elif random_num == 7 :
                    if letter.lower() == "f":
                        word_incomplete[0] = "f"
                    elif letter.lower() == "o":
                        word_incomplete[2] = "o"
                        word_incomplete[4] = "o"
                    elif letter.lower() == "t":
                        word_incomplete[6] = "t"
                    elif letter.lower() == "b":
                        word_incomplete[8] = "b"
                    elif letter.lower() == "a":
                        word_incomplete[10] = "a"
                    elif letter.lower() == "l":
                        word_incomplete[12] = "l"
                        word_incomplete[14] = "l"
                    else:                    
                        turns_remain -= 1
                #word 'Keyboard'
                elif random_num == 8 :
                    if letter.lower() == "k":
                        word_incomplete[0] = "k"
                    elif letter.lower() == "e":
                        word_incomplete[2] = "e"
                    elif letter.lower() == "y":
                        word_incomplete[4] = "y"
                    elif letter.lower() == "b":
                        word_incomplete[6] = "b"
                    elif letter.lower() == "o":
                        word_incomplete[8] = "o"
                    elif letter.lower() == "a":
                        word_incomplete[10] = "a"
                    elif letter.lower() == "r":
                        word_incomplete[12] = "r"
                    elif letter.lower() == "d":
                        word_incomplete[14] = "d"
                    else:                    
                        turns_remain -= 1
                #word 'Kiwi'
                elif random_num == 9 :
                    if letter.lower() == "k":
                        word_incomplete[0] = "k"
                    elif letter.lower() == "i":
                        word_incomplete[2] = "i"
                        word_incomplete[6] = "i"
                    elif letter.lower() == "w":
                        word_incomplete[4] = "w"
                    else:                    
                        turns_remain -= 1
                #word 'Lion'
                elif random_num == 10 :
                    if letter.lower() == "l":
                        word_incomplete[0] = "l"
                    elif letter.lower() == "i":
                        word_incomplete[2] = "i"
                    elif letter.lower() == "o":
                        word_incomplete[4] = "o"
                    elif letter.lower() == "n":
                        word_incomplete[6] = "n"
                    else:                    
                        turns_remain -= 1
                #word 'Ostrich'
                elif random_num == 11 :
                    if letter.lower() == "o":
                        word_incomplete[0] = "o"
                    elif letter.lower() == "s":
                        word_incomplete[2] = "s"
                    elif letter.lower() == "t":
                        word_incomplete[4] = "t"
                    elif letter.lower() == "r":
                        word_incomplete[6] = "r"
                    elif letter.lower() == "i":
                        word_incomplete[8] = "i"
                    elif letter.lower() == "c":
                        word_incomplete[10] = "c"
                    elif letter.lower() == "h":
                        word_incomplete[12] = "h"
                    else:                    
                        turns_remain -= 1
                #word 'Parrot'
                elif random_num == 12 :
                    if letter.lower() == "p":
                        word_incomplete[0] = "p"
                    elif letter.lower() == "a":
                        word_incomplete[2] = "a"
                    elif letter.lower() == "r":
                        word_incomplete[4] = "r"
                        word_incomplete[6] = "r"
                    elif letter.lower() == "o":
                        word_incomplete[8] = "o"
                    elif letter.lower() == "t":
                        word_incomplete[10] = "t"
                    else:                    
                        turns_remain -= 1
                #word 'Pen'
                elif random_num == 13 :
                    if letter.lower() == "p":
                        word_incomplete[0] = "p"
                    elif letter.lower() == "e":
                        word_incomplete[2] = "e"
                    elif letter.lower() == "n":
                        word_incomplete[4] = "n"
                    else:                    
                        turns_remain -= 1
                #word 'Rabbit'
                elif random_num == 14 :
                    if letter.lower() == "r":
                        word_incomplete[0] = "r"
                    elif letter.lower() == "a":
                        word_incomplete[2] = "a"
                    elif letter.lower() == "b":
                        word_incomplete[4] = "b"
                        word_incomplete[6] = "b"                
                    elif letter.lower() == "i":
                        word_incomplete[8] = "i"
                    elif letter.lower() == "t":
                        word_incomplete[10] = "t"
                    else:                    
                        turns_remain -= 1
                #word 'School'
                elif random_num == 15 :
                    if letter.lower() == "s":
                        word_incomplete[0] = "s"
                    elif letter.lower() == "c":
                            word_incomplete[2] = "c"
                    elif letter.lower() == "h":
                        word_incomplete[4] = "h"
                    elif letter.lower() == "o":
                        word_incomplete[6] = "o"
                        word_incomplete[8] = "o"                    
                    elif letter.lower() == "l":
                        word_incomplete[10] = "l"
                    else:                    
                        turns_remain -= 1
                #word 'Shoe'
                elif random_num == 16 :
                    if letter.lower() == "s":
                        word_incomplete[0] = "s"
                    elif letter.lower() == "h":
                        word_incomplete[2] = "h"
                    elif letter.lower() == "o":
                        word_incomplete[4] = "o"
                    elif letter.lower() == "e":
                        word_incomplete[6] = "e"
                    else:                    
                        turns_remain -= 1
                #word 'Speaker'
                elif random_num == 17 :
                    if letter.lower() == "s":
                        word_incomplete[0] = "s"
                    elif letter.lower() == "p":
                        word_incomplete[2] = "p"
                    elif letter.lower() == "e":
                        word_incomplete[4] = "e"
                        word_incomplete[10] = "e"
                    elif letter.lower() == "a":
                        word_incomplete[6] = "a"
                    elif letter.lower() == "k":
                        word_incomplete[8] = "k"
                    elif letter.lower() == "r":
                        word_incomplete[12] = "r"
                    else:                    
                        turns_remain -= 1
                #word 'Table'
                elif random_num == 18 :
                    if letter.lower() == "t":
                        word_incomplete[0] = "t"
                    elif letter.lower() == "a":
                        word_incomplete[2] = "a"
                    elif letter.lower() == "b":
                        word_incomplete[4] = "b"
                    elif letter.lower() == "l":
                        word_incomplete[6] = "l"
                    elif letter.lower() == "e":
                        word_incomplete[8] = "e"                
                    else:                    
                        turns_remain -= 1
                #word 'Television'
                elif random_num == 19 :
                    if letter.lower() == "t":
                        word_incomplete[0] = "t"
                    elif letter.lower() == "e":
                        word_incomplete[2] = "e"
                        word_incomplete[6] = "e"
                    elif letter.lower() == "l":
                        word_incomplete[4] = "l"
                    elif letter.lower() == "v":
                        word_incomplete[8] = "v"
                    elif letter.lower() == "i":
                        word_incomplete[10] = "i"
                        word_incomplete[14] = "i"
                    elif letter.lower() == "s":
                        word_incomplete[12] = "s"
                    elif letter.lower() == "o":
                        word_incomplete[16] = "o"
                    elif letter.lower() == "n":
                        word_incomplete[18] = "n"
                    else:                    
                        turns_remain -= 1
                #word 'Zebra'
                elif random_num == 20 :
                    if letter.lower() == "z":
                        word_incomplete[0] = "z"
                    elif letter.lower() == "e":
                        word_incomplete[2] = "e"
                    elif letter.lower() == "b":
                        word_incomplete[4] = "b"
                    elif letter.lower() == "r":
                        word_incomplete[6] = "r"
                    elif letter.lower() == "a":
                        word_incomplete[8] = "a"
                    else:                    
                        turns_remain -= 1
                    
                #displaying the updated results according to the current data
                if "_" in word_incomplete :
                    if turns_remain == 0:    
                        pass
                    else:
                        print("Word : ",end="")
                        for count1 in word_incomplete:
                            print(count1,end = "")
                        print()
                        print(turns_remain,"turns remain")
                elif "_" not in word_incomplete:
                    print("Word : ",end="")
                    for count1 in word_incomplete:
                        print(count1,end = "")
                    print()
                    pass
            turns_used = turns_provided-turns_remain
        elif "_" not in word_incomplete and turns_remain>0:
            status = "won"
            print()
            print("You won!")
            print('Word is "%s"'%word)
            cont = False
        else:
            status = "lost"
            print()
            print("You lost!")
            print('Word is "%s"'%word)
            cont = False
    return word, turns_provided, turns_used, status

#lists
#list of words
words = ("","book","bottle","camera","cricket","cupboard","eagle","football","keyboard","kiwi","lion","ostrich","parrot","pen","rabbit","school","shoe","speaker","table","television","zebra")
#list of hints
hints = ("","Used to take notes","Used to store any liquid","Used to capture beatiful moments","A sport played using the bat and ball","Used to store books and other stuff on the shelves in it","A bird with sharp eyesight","A sport played between two teams consisting of 11 players each, by using one ball","Device used to pass letters into the computer machine","An animal with the name of a fruit","An animal with lot of hair around it's neck","A bird with strong fast legs","A green coloured bird","Used to write notes using it","A animal that can move faster but small","A place we used to spend most of the time when we were young","Used to wear for our own comfort","Used to play music or any audio","A surface that holds things on it","We use it to watch the programs that we love","An animal with a black and white coloured texture all over the body")
#list of blanks for each word
blanks = ("","_ _ _ _","_ _ _ _ _ _","_ _ _ _ _ _","_ _ _ _ _ _ _","_ _ _ _ _ _ _ _","_ _ _ _ _","_ _ _ _ _ _ _ _","_ _ _ _ _ _ _ _","_ _ _ _","_ _ _ _","_ _ _ _ _ _ _","_ _ _ _ _ _","_ _ _","_ _ _ _ _ _","_ _ _ _ _ _","_ _ _ _","_ _ _ _ _ _ _","_ _ _ _ _","_ _ _ _ _ _ _ _ _ _","_ _ _ _ _")
#list turns
turns = (0,4,6,6,7,8,5,8,8,4,4,7,6,3,6,6,4,7,5,10,5)



