def player_name(): #function to take in player names
    name = input("Please enter your name: ")
    print("Welcome to Tic Tac Toe game.\n" + name)
    return(name) #return player name

def player_input(name): #function to ask for player_1 to be either 'X' or 'O'
    player_1 = input(f"{name} do you wish to be 'X' or 'O'?: ")
    print(player_1) #print the question and assign the character to variable
    if(player_1.upper() == "X" or player_1.upper() == "O"): #Check if player_1 entered the proper response.
        print("Let's Play!")
    else: #If proper response was not entered run the following
        while(player_1.upper() != "X" or player_1.upper() != "O"): #While loop to check fo the duration that player is entering wrong charater.
            print("Please enter valid input...")
            player_1 = input("Do you wish to be 'X' or 'O'?: ") #Need to be able to assign a new variable to player_1 each time they enter something wrong.
            print(player_1)
            if(player_1.upper() == "X" or player_1.upper() == "O"): #Check if they entered correctly after each time you ask.
                print("Let's Play!")
                break #break out of while loop as soon as they have entered the proper response.
    return(player_1.upper())

def player_turn(name): #function that takes in the player's name
    print(f"It is {name}'s turn.") #let's the player know whose turn it is
    position = int(input("Please enter a digit between 1 and 9: ")) #ask for an input between 1 and 9
    if position not in range(0,10): #check to make sure answer is within range
        while(position not in range(0,10)): #for as long as input is not in range, keep asking to enter a new value
            int(input("Please enter a digit between 1 and 9: "))
            continue
    else:
        return(position) #if the input is valid, return the number as it will be used to determine position on board

def check_winner(b_1, b_2, b_3): #check to see if anyone has won
    if(b_1 == ['| X |','| X |','| X |'] or b_1 == ['| O |','| O |','| O |']): #if they match the 1st row
        return(True)
    elif(b_2 == ['| X |','| X |','| X |'] or b_2 == ['| O |','| O |','| O |']): #if they match the 2nd row
        return(True)
    elif(b_3 == ['| X |','| X |','| X |'] or b_3 == ['| O |','| O |','| O |']): #if they match the 3rd row
        return(True)

name_1 = player_name() #run function to ask for name of player
name_2 = player_name()
player_1 = player_input(name_1) #Run the player_input function to assign a character 'X' or 'O' to player_1

print(f"{name_1} has decided to be: {player_1}") #Display which choice player_1 has made
if(player_1.upper() == 'X'):
    player_2 = 'O' #If player_1 chose 'X' assign 'O' to player_2
else:
    player_2 = 'X' #If player_2 chose 'O' assign 'X' to player_2

print(f"{name_2} will be: {player_2} \n")

#Creating an empty list to be able to store variables
board_1 = ["|___|"]
board_2 = ["|___|"]
board_3 = ["|___|"]

#Making the empty list into column of 3
board_1 *= 3
board_2 *= 3
board_3 *= 3

counter_turn = 0
while(counter_turn < 10):
    if(counter_turn == 9): #if counter reaches the 9th turn, no one was able to win
        print("Sorry the game ended in a tie..")
        answer = input("Do you wish to play again (yes or no)? ")
        if(answer.upper() == "YES"): #asked if they wanted to play again, if they did we will return counter to 0 and they will have a new board.
            counter_turn = 0
            board_1 = ["|___|"]
            board_2 = ["|___|"]
            board_3 = ["|___|"]
            board_1 *= 3
            board_2 *= 3
            board_3 *= 3
            continue
        else: #if they don't want to play, end game.
            print("Thanks for playing! Let's play again some other time!")
            break
    elif(check_winner(board_1, board_2, board_3) == True): #run check_winner() function to see if there has been a winner or not
        if (counter_turn % 2 == 0):
            print(f"Congrats! {name_1} has won the GAME!") #if player 1 wins, congratulate them and break loop
            break
        else:
            print(f"Congrats! {name_2} has won the GAME!") #if player 2 wins, congratulate them and break loop
            break
    else:
        if (counter_turn % 2 == 0):
            position = player_turn(name_1)
            if(player_1.upper() == 'X'):
                if((position in range (0,4) and board_1[position-1] != "|___|") or (position in range(3,7) and board_2[position-4] != "|___|") or (position in range(6,10) and board_3[position-7] != "|___|")):
                    print(f"Someone already placed a mark on the {position} position.") #the above if will check if the list has already been occupied, if it has, it will ask for a new input.
                    print("Please enter a new position: ")
                    position = player_turn(name_1)
                    continue
                elif(position == 1):
                    del board_1[0]
                    board_1.insert(0, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 2):
                    del board_1[1]
                    board_1.insert(1, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 3):
                    del board_1[2]
                    board_1.insert(2, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 4):
                    del board_2[0]
                    board_2.insert(0, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 5):
                    del board_2[1]
                    board_2.insert(1, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 6):
                    del board_2[2]
                    board_2.insert(2, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 7):
                    del board_3[0]
                    board_3.insert(0, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 8):
                    del board_3[1]
                    board_3.insert(1, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                else:
                    del board_3[2]
                    board_3.insert(2, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
            elif(player_1.upper() == 'O'):
                if((position in range (0,4) and board_1[position-1] != "|___|") or (position in range(3,7) and board_2[position-4] != "|___|") or (position in range(6,10) and board_3[position-7] != "|___|")):
                    print("Someone already placed a mark on that position.")
                    print("Please enter a new position: ")
                    position = player_turn(name_1)
                    continue
                elif(position == 1):
                    del board_1[0]
                    board_1.insert(0, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 2):
                    del board_1[1]
                    board_1.insert(1, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 3):
                    del board_1[2]
                    board_1.insert(2, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 4):
                    del board_2[0]
                    board_2.insert(0, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 5):
                    del board_2[1]
                    board_2.insert(1, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 6):
                    del board_2[2]
                    board_2.insert(2, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 7):
                    del board_3[0]
                    board_3.insert(0, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 8):
                    del board_3[1]
                    board_3.insert(1, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 9):
                    del board_3[2]
                    board_3.insert(2, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
        else:
            position = player_turn(name_2)
            if(player_2.upper() == 'X'):
                if((position in range (0,4) and board_1[position-1] != "|___|") or (position in range(3,7) and board_2[position-4] != "|___|") or (position in range(6,10) and board_3[position-7] != "|___|")):
                    print("Someone already placed a mark on that position.")
                    print("Please enter a new position: ")
                    position = player_turn(name_2)
                    continue
                elif(position == 1):
                    del board_1[0]
                    board_1.insert(0, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 2):
                    del board_1[1]
                    board_1.insert(1, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 3):
                    del board_1[2]
                    board_1.insert(2, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 4):
                    del board_2[0]
                    board_2.insert(0, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 5):
                    del board_2[1]
                    board_2.insert(1, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 6):
                    del board_2[2]
                    board_2.insert(2, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 7):
                    del board_3[0]
                    board_3.insert(0, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 8):
                    del board_3[1]
                    board_3.insert(1, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                else:
                    del board_3[2]
                    board_3.insert(2, '| X |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
            elif(player_2.upper() == 'O'):
                if((position in range (0,4) and board_1[position-1] != "|___|") or (position in range(3,7) and board_2[position-4] != "|___|") or (position in range(6,10) and board_3[position-7] != "|___|")):
                    print("Someone already placed a mark on that position.")
                    print("Please enter a new position: ")
                    position = player_turn(name_2)
                    continue
                elif(position == 1):
                    del board_1[0]
                    board_1.insert(0, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 2):
                    del board_1[1]
                    board_1.insert(1, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 3):
                    del board_1[2]
                    board_1.insert(2, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 4):
                    del board_2[0]
                    board_2.insert(0, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 5):
                    del board_2[1]
                    board_2.insert(1, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 6):
                    del board_2[2]
                    board_2.insert(2, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 7):
                    del board_3[0]
                    board_3.insert(0, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 8):
                    del board_3[1]
                    board_3.insert(1, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
                elif(position == 9):
                    del board_3[2]
                    board_3.insert(2, '| O |')
                    print("".join(board_1))
                    print("".join(board_2))
                    print("".join(board_3))
    counter_turn += 1
