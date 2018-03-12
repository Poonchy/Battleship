from random import randint
board = [] #Create an empty board
for x in range(0, 5): #Loop that runs 5 times
  board.append(["O"] * 5) #Appends the empty board with 5 O's
def print_board(board): #Define print_board function
  for row in board: #For every O in board
    print " ".join(row) #Add empty space between the O's
print_board(board) #Prints the board
def random_row(board): #Define random_row function
  return randint(0, len(board) - 1) #Returns an integer in the range of the board spaces
def random_col(board): #Define random_col function
  return randint(0, len(board[0]) - 1) #Returns an integer in the range of the board's spaces
ship_row = random_row(board) #ship_row's value is equal to a random integer between 0 and 4
ship_col = random_col(board) #ship_col's value is equal to a random integer between 0 and 4
for turn in range(4): #Gives the user 4 turns
  print "Turn", turn + 1 #Prints what turn it is
  guess_row = int(raw_input("Guess Row: ")) #Allows user to guess the row
  guess_col = int(raw_input("Guess Col: ")) #Allows user to guess the collumn
  guess_row = guess_row - 1 #Make guess user friendly (1-5 instead of 0-4)
  guess_col = guess_col - 1 #Make guess user friendly (1-5 instead of 0-4)
  print "" #Makes the printing more user friendly by adding empty space
  if guess_row == ship_row and guess_col == ship_col: #Check if the guesses were right
    print "Congratulations! You sank my battleship!" #Outputs a congratulation to user 
    break; #Breaks loop; ends game.
  else: #If coordinates did not match
    if guess_row not in range(5) or \
      guess_col not in range(5): #Checks if the guess was off the board
      print "Oops, that's not even in the ocean." #Tells user he missed the entire ocean (stupid user)
    elif board[guess_row][guess_col] == "X": #Checks if user already guessed that spot
      print( "You guessed that one already." ) #Tells user that he already guessed that spot (silly user)
    else: #If user just normally misses within the boundaries of the board
      print "You missed my battleship!" #Tells user he missed the ship
      board[guess_row][guess_col] = "X" #Print an X over the point of the guess
    if (turn == 3): #If the user guesses 4 times
      print "Game Over" #Tells user he lost
      board[ship_row][ship_col] = "B" #Replace an O with a B for the boat
    print_board(board)#Show the user where the boat was.
    print "" #Makes the printing more user friendly by adding empty space