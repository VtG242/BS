#!/usr/bin/python
from random import randint

debug = False

#vizualizace boardu
board = [
["5", "O", "O", "O", "O", "O"],
["4", "O", "O", "O", "O", "O"],
["3", "O", "O", "O", "O", "O"],
["2", "O", "O", "O", "O", "O"],
["1", "O", "O", "O", "O", "O"],
["-", "A", "B", "C", "D", "E"],
]
x_map = {
"A": 1,
"B": 2,
"C": 3,
"D": 4,
"E": 5,
}
y_map = {
"1": 4,
"2": 3,
"3": 2,
"4": 1,
"5": 0,
}

def print_board(board):
    for row in board:
        print " ".join(row)

# umisteni lode - funkce
def random_row(board):
    #dostupne hodnoty 0,1,2,3,4 (y_map)
    return randint(0, len(board) - 2)
def random_col(board):
    #dostupne hodnoty 1,2,3,4,5 (x_map)
    return randint(1, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#debug:
if debug == True:
    print("Radky:" + str(len(board)))
    print("Sloupce:" + str(len(board[0])))
    print "Ship in - Row: " + str(ship_row) + " Col: " + str(ship_col)
    board[ship_row][ship_col] = "S"
        
#zobrazeni boardu
print_board(board)
    
#main game
for turn in range(4):
    
    print "Turns remain: ", 4 - turn 

    #user data
    while True:
        try:
            guess_row = int(raw_input("Guess Row (number): "))
            #radka v poli odpovidajici vizualizaci
            guess_row = y_map[str(guess_row)]
            if debug:
                print guess_row    
            break            
        except:
            ValueError
            KeyError
            print("That's not an integer or it's out of range!")
                
    while True:
        guess_col = raw_input("Guess Col (letter): ")
        try:
            #skutecny sloupec v poli
            guess_col = x_map[guess_col]
            if debug:
                print guess_col
            break
        except KeyError:
            print("That's not a letter in range 'A - F'")

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    
    if turn == 3:
        print "Game Over"
        
        question = raw_input("Do you want to reveal a ship position? (Y/N)")
        if question == "Y":
            board[ship_row][ship_col] = "S"
            print_board(board)
        else:
            print("Bye!")




