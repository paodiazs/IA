# -*- coding: utf-8 -*-
"""tictactoe_minmax.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aFmZT33J5T83YDcvZakRVJ4g0FWkVu5k
"""

def display_board(board):
    """
    Display the current state of the Tic-Tac-Toe board.

    Parameters:
    - board (list): A 2D list representing the Tic-Tac-Toe board.

    Each cell of the board is displayed, separated by '|' for columns,
    and rows are separated by a line of dashes ('-----').

    Example:
    If the board is [['X', 'O', ' '], [' ', 'X', 'O'], ['O', ' ', 'X']],
    the output will be:
    X|O|
    -----
     |X|O
    -----
    O| |X
    """
    for i, row in enumerate(board):
        # Display the cells of the current row, separated by '|'
        print('|'.join(row))

        # Display a line of dashes to separate rows, but not after the last row
        if i < len(board) - 1:
            print('-' * 5)

#create a 3x3 grid to represent the board
board = [[' ' for _ in range(3)] for _ in range(3)]

#call the display_board function to print the current state of the board
display_board(board)

#Helper functions
#Check if the specified winner has won the tic tac toe, by rows,columns and diagonals
"""
board(list):a 2d list representing the tictactoe board
player(str): the player to check for a win ('X' or 'O')
return bool: true if the specifid player has won, false if not
"""
def check_win(board,player):
  #Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True

  #Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
    return True

  return False

"""
check if the tictactoe game is a draw(empate): no more empty spaces on the board
returns bool: True if the game is empate, false otherwise
"""

def is_draw(board):
  return all(cell != ' ' for row in board for cell in row)

"""
This function is to get the player´s move, form the input
returns tuple: the selected row and column coordinates
"""
def player_move(board):
  while True:
    try:
      #Get input for row and column for the player
      row = int(input("Enter row(0,1,2): "))
      col = int(input("Enter column(0,1,2): "))

      #check if the input is within a valid range and the selected cell is empty
      if 0 <= row <= 2 and 0<= col <= 2 and board[row][col] == ' ':
        return row, col
      else:
        print("Movimiento invalido, Intenta de nuevo")
    except ValueError:
      #to handle the cases where the input is not a valid integer
      print("Invalid input. Enter a number between 0 and 2")

"""
implement minmax
board(list): representing the tictactoe board
depth(int): the current depth in the recursive search of the game tree
is_maximizing(bool): indicates wether the current player is maximizing TRUE or minimizing FALSE
max_depth(int): the maximum depth to explore in the game tree

returns:
int: the calculated score for the current state of the board
"""


def minmax(board, depth, is_maximizing, max_depth):
  #check if the game is won by X or O or if its a draw
  if check_win(board, 'X'):
    return -1
  elif check_win(board, 'O'):
    return 1
  elif is_draw(board) or depth == max_depth:
    return 0

  if is_maximizing:
    #if maximazing, initialize the maximum evaluation score to negative infinity
    max_eval = -float('inf')
    for i in range(3):
      for j in range(3):
        if board[i][j] == ' ':
          #simula el movimiento para el maximizing player('O')
          board[i][j] = 'O'
          #recursively call minmax for the next level with the minimizing players turn
          eval = minmax(board, depth + 1, False, max_depth)
          #undo the move
          board[i][j] = ' '
          #update the maximum evaluation score
          max_eval = max(max_eval, eval)
    return max_eval

  else:
    #if minimizing, initialize the minimum evaluation score to positive infinity
    min_eval = float('inf')
    for i in range(3):
      for j in range(3):
        if board[i][j] == ' ':
          #simulate the move for the minimizing player('X)
          board[i][j] = 'X'
          #recursively call minmax for the next level with the maximizing players turn
          eval = minmax(board, depth + 1, True, max_depth)
          #undo the move
          board[i][j] = ' '
          #update the minimum evaluation score
          min_eval=min(min_eval, eval)
    return min_eval

"""
determine the optimal move for the AI player
return tuple: the coordinates(row, column) of the optimal move for the AI player
This function iterates through each empty space on the board, simulates placing an 'O' in that space,
    and evaluates the move using the Minimax algorithm. The AI player chooses the move with the highest
    evaluation score.
"""
def ai_move(board, max_depth):
  best_eval = -float('inf')
  best_move = None

  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        board[i][j] = 'O'
        eval = minmax(board, 0 , False, max_depth)
        board[i][j] = ' '
        if eval > best_eval:
          best_eval = eval
          best_move = (i,j)
  return best_move

def main():
    """
    Run the main game loop for a simple Tic-Tac-Toe game.

    The game loop alternates between player and AI turns, displaying the current state of the board after each move.
    The loop continues until there is a winner ('X' or 'O'), a draw, or the player chooses to exit the game.

    This function uses the display_board, player_move, ai_move, check_win, and is_draw functions to implement the game logic.

    Example:
    Calling main() starts and runs the Tic-Tac-Toe game until a winner is declared or the game ends in a draw.
    """

    # Reset the game board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    player_turn = True

    while True:
        display_board(board)

        if player_turn:
          print("\n")
          print("Your turn:")
          row, col = player_move(board)
          print("\n")
          board[row][col] = 'X'
        else:
            print("\n")
            input("Press Enter for the Ai player to go...")
            """
            Change the depth explored by the AI player by changing the number in
            parentheses in the next line of code. The default value is 0.
            """
            row, col = ai_move(board, 8)    # TODO: Adjust the depth explored here!
            print("\n")
            board[row][col] = 'O'

        if check_win(board, 'X'):
            display_board(board)
            print("You win!")
            break
        elif check_win(board, 'O'):
            display_board(board)
            print("AI wins!")
            break
        elif is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    main()