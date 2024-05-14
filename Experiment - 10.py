board = [" " for x in range(9)]

def print_board():
    print()
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player", number)
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")
    print_board()
    if is_victory(icon):
        print(icon, "wins! Congratulations!")
        return False;
    elif is_draw():
        print("It's a draw!")
        return False;
    return True;
        
def is_victory(icon):
    return ((board[0] == icon and board[1] == icon and board[2] == icon) or 
       (board[3] == icon and board[4] == icon and board[5] == icon) or 
       (board[6] == icon and board[7] == icon and board[8] == icon) or 
       (board[0] == icon and board[3] == icon and board[6] == icon) or 
       (board[1] == icon and board[4] == icon and board[7] == icon) or 
       (board[2] == icon and board[5] == icon and board[8] == icon) or 
       (board[0] == icon and board[4] == icon and board[8] == icon) or 
       (board[2] == icon and board[4] == icon and board[6] == icon))
        
def is_draw():
    return " " not in board

print_board()
while True:
    if (not player_move("X")): break
    if (not player_move("O")): break
