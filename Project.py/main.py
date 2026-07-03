
# Creating an empty board using a list
board = [' '] * 9

# Function to display the board
def display_board():
    print()
    print(" ", board[0], "|", board[1], "|", board[2])
    print("----+---+----")
    print(" ", board[3], "|", board[4], "|", board[5])
    print("----+---+----")
    print(" ", board[6], "|", board[7], "|", board[8])
    print()

# Function to check win condition
def check_winner(player):
    # Checking rows
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player):
        return True

    # Checking columns
    if (board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player):
        return True

    # Checking diagonals
    if (board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True

    return False

# Function to check draw
def check_draw():
    for i in board:
        if i == " ":
            return False
    return True

# Main program
print("WELCOME TO TIC TAC TOE GAME")
print("Player 1 : X")
print("Player 2 : O")
display_board()

current_player = "X"

while True:
    print("Player", current_player, "turn")
    position = int(input("Enter position (1-9): "))

    # Adjusting position to list index
    position -= 1

    # Checking if position is empty
    if board[position] == " ":
        board[position] = current_player
        display_board()

        # Checking for winner
        if check_winner(current_player):
            print("Player", current_player, "wins the game!")
            break

        # Checking for draw
        if check_draw():
            print("The game is a draw!")
            break

        # Switching player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        print("Position already occupied. Try again.")