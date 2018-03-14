from random import randint

#Creating the board
board = []
for x in range(0, 7):
  board.append(["O"] * 7)
def print_board(board):
  for row in board:
    print " ".join(row)
print_board(board)

#Computer places it's ships
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)

#Horizontal 3 ship
threeHorRow = random_row(board)
threeHorColTwo = randint(0, len(board[0]) - 3) + 1
threeHorColOne = threeHorColTwo - 1
threeHorColThree = threeHorColTwo + 1
board[threeHorRow][threeHorColOne] = "H"
board[threeHorRow][threeHorColTwo] = "H"
board[threeHorRow][threeHorColThree] = "H"
threeVerCol = random_col(board)
threeVerRowTwo = random_row(board)
threeVerRowOne = threeVerRowTwo - 1
threeVerRowThree = threeVerRowTwo + 1

#Vertical 3 ship
while threeVerRowOne < 0 or threeVerRowThree > 10 or threeVerRowOne or board[threeVerRowOne][threeVerCol] == "H" or board[threeVerRowTwo][threeVerCol] == "H" or board[threeVerRowThree][threeVerCol] == "H":
  threeVerCol = random_col(board)
  threeVerRowTwo = randint(0, len(board) - 2) + 1
  threeVerRowOne = threeVerRowTwo - 1
  threeVerRowThree = threeVerRowTwo + 1
board[threeVerRowOne][threeVerCol] = "V"
board[threeVerRowTwo][threeVerCol] = "V"
board[threeVerRowThree][threeVerCol] = "V"

#5 Horizontal ship
fiveHorRow = random_row(board)
fiveHorColMid = randint(0, len(board[0]) - 5) + 2
fiveHorColOne = fiveHorColMid - 1
fiveHorColTwo = fiveHorColMid - 2
fiveHorColThree = fiveHorColMid + 1
fiveHorColFour = fiveHorColMid + 2
while board[fiveHorRow][fiveHorColMid] == "H" or board[fiveHorRow][fiveHorColOne] == "H" or board[fiveHorRow][fiveHorColTwo] == "H" or board[fiveHorRow][fiveHorColThree] == "H" or board[fiveHorRow][fiveHorColFour] == "H" or board[fiveHorRow][fiveHorColMid] == "V" or board[fiveHorRow][fiveHorColOne] == "V" or board[fiveHorRow][fiveHorColTwo] == "V" or board[fiveHorRow][fiveHorColThree] == "V" or board[fiveHorRow][fiveHorColFour] == "V":
  fiveHorRow = random_row(board)
  fiveHorColMid = randint(0, len(board[0]) - 5) + 2
  fiveHorColOne = fiveHorColMid - 1
  fiveHorColTwo = fiveHorColMid - 2
  fiveHorColThree = fiveHorColMid + 1
  fiveHorColFour = fiveHorColMid + 2
board[fiveHorRow][fiveHorColMid] = "F"
board[fiveHorRow][fiveHorColOne] = "F"
board[fiveHorRow][fiveHorColTwo] = "F"
board[fiveHorRow][fiveHorColThree] = "F"
board[fiveHorRow][fiveHorColFour] = "F"

#Hiding all the ships
board[threeHorRow][threeHorColOne] = "O"
board[threeHorRow][threeHorColTwo] = "O"
board[threeHorRow][threeHorColThree] = "O"
board[fiveHorRow][fiveHorColMid] = "O"
board[fiveHorRow][fiveHorColOne] = "O"
board[fiveHorRow][fiveHorColTwo] = "O"
board[fiveHorRow][fiveHorColThree] = "O"
board[fiveHorRow][fiveHorColFour] = "O"
board[threeVerRowOne][threeVerCol] = "O"
board[threeVerRowTwo][threeVerCol] = "O"
board[threeVerRowThree][threeVerCol] = "O"

#Defining strikes and hits
hit = 0
strike = 0

#Game loop begins here
for turn in range(20):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  guess_row = guess_row - 1
  guess_col = guess_col - 1
  print ""
  
  #If user hits
  if (guess_row == fiveHorRow and guess_col == fiveHorColMid) or (guess_row == fiveHorRow and guess_col == fiveHorColOne) or (guess_row == fiveHorRow and guess_col == fiveHorColTwo) or (guess_row == fiveHorRow and guess_col == fiveHorColThree) or (guess_row == fiveHorRow and guess_col == fiveHorColFour) or (guess_row == threeHorRow and guess_col == threeHorColOne) or (guess_row == threeHorRow and guess_col == threeHorColTwo) or (guess_row == threeHorRow and guess_col == threeHorColThree) or (guess_row == threeVerRowOne and guess_col == threeVerCol) or (guess_row == threeVerRowTwo and guess_col == threeVerCol) or (guess_row == threeVerRowThree and guess_col == threeVerCol): 
    print "A hit!"
    hit = hit + 1
    board[guess_row][guess_col] = "X"
    print "You've hit", hit, "cannonballs!"
    
    #If he hits sinks all 3 ships
    if (hit == 11):
      print "Congratulations, you sunk all my ships!"
      break;
      
      #If user misses
  else:
    if guess_row not in range(len(board)) or \
      guess_col not in range(len(board)):
      print "Oops, that's not even in the ocean."
      strike += 1
      print "Strike: ", strike, "!"
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
      strike += 1
      print "Strike: ", strike, "!"
    else:
      print "You missed my battleship!"
      strike += 1
      print "Strike: ", strike, "!"
      board[guess_row][guess_col] = "X"
      
      #If user misses 5 times show ships end game
    if (strike == 5):
      board[threeHorRow][threeHorColOne] = "S"
      board[threeHorRow][threeHorColTwo] = "S"
      board[threeHorRow][threeHorColThree] = "S"
      board[fiveHorRow][fiveHorColMid] = "S"
      board[fiveHorRow][fiveHorColOne] = "S"
      board[fiveHorRow][fiveHorColTwo] = "S"
      board[fiveHorRow][fiveHorColThree] = "S"
      board[fiveHorRow][fiveHorColFour] = "S"
      board[threeVerRowOne][threeVerCol] = "S"
      board[threeVerRowTwo][threeVerCol] = "S"
      board[threeVerRowThree][threeVerCol] = "S"
      print "Game Over"
      print ""
      print_board(board)
      break;
  print_board(board)
  print ""