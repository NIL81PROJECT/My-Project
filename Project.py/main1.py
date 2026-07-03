
# Simple Tic Tac Toe Game


board = [' '] * 9

def show():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def win(p):
    if (board[0]==board[1]==board[2]==p or
        board[3]==board[4]==board[5]==p or
        board[6]==board[7]==board[8]==p or
        board[0]==board[3]==board[6]==p or
        board[1]==board[4]==board[7]==p or
        board[2]==board[5]==board[8]==p or
        board[0]==board[4]==board[8]==p or
        board[2]==board[4]==board[6]==p):
        return True
    return False

def draw():
    return ' ' not in board

player = 'X'

while True:
    show()
    pos = int(input("Player "+ player +" enter position (1-9): ")) 

    if board[pos] != ' ':
        print("Position already filled")
        continue

    board[pos] = player

    if win(player):
        show()
        print("Player", player, "wins")
        break

    if draw():
        show()
        print("Game Draw")
        break

    player = 'O' if player == 'X' else 'X'










































