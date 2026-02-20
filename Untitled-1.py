
board = [" " for _ in range(9)]



def print_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")



def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False



current_player = "X"

while True:
    print_board()
    move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = current_player
    else:
        print("TRY Again")
        continue

    


    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break




    if " " not in board:
        print_board()
        print("DRAW!")
        break

   


    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"