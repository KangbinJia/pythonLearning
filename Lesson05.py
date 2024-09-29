### This is the dictionary for the board
game_board = {
  "square 1": " ",
  "square 2": " ",
  "square 3": " ",
  "square 4": " ",
  "square 5": " ",
  "square 6": " ",
  "square 7": " ",
  "square 8": " ",
  "square 9": " "
}

### This is the function to print the board
def print_board(game_board):
  print(game_board["square 1"] + "|" + game_board["square 2"] + "|" + game_board["square 3"])
  print("-+-+-")
  print(game_board["square 4"] + "|" + game_board["square 5"] + "|" + game_board["square 6"])
  print("-+-+-")
  print(game_board["square 7"] + "|" + game_board["square 8"] + "|" + game_board["square 9"])

print_board(game_board)


### This is initionalizaiotn of the game
player_1_name = input('Player 1 enter your name: ')
print()
print(player_1_name, 'Your peice is X')
print()
player_2_name = input('Player 2 enter your name: ')
print()
print(player_2_name, 'Your peice is O')
print()
print("""When it is your turn, select a number between 1 and 9 to move. The board below shows where your piece will appear depending on the number you choose.""")
print()

print('\n ok, lets start')
turn = player_1_name
piece = 'X'
count = 0

while True:
  print_board(game_board)
  move = input(turn + ', where would you like to move?' )
  if move in game_board:
    if board[move] == ' ':
      board[move] = piece
      count += 1
      print_board(game_board)
    else:
      print('That space is already taken.')
      continue
  else:
    print('invalid unput enter a number from 1 to 9')
    continue