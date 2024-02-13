def solution(board):
    answer = -1
    normal = 1
    error = 0
    num_o = 0
    num_x = 0
    bingos_o = 0
    bingos_x = 0
    
    # get total number of each player's symbol
    for row in board :
        if 'O' in row :
            num_o += row.count('O')
        if 'X' in row :
            num_x += row.count('X')

    # get number of bingos
    for i in range(3) : 
        #horizontal
        if board[i][0] == board[i][1] == board[i][2] :
            if board[i][0] == 'O' :
                bingos_o += 1
            elif board[i][0] == 'X' :
                bingos_x += 1
        #vertical
        if board[0][i] == board[1][i] == board[2][i] :
            if board[0][i] == 'O' :
                bingos_o += 1
            if board[0][i] == 'X' :
                bingos_x += 1
    # diagonal
    if board[1][1] == 'O' :
        if board[0][0] == board[1][1] == board[2][2] :
            bingos_o += 1
        if board[0][2] == board[1][1] == board[2][0] :
            bingos_o += 1
    elif board[1][1] == 'X' :
        if board[0][0] == board[1][1] == board[2][2] :
            bingos_x += 1
        if board[0][2] == board[1][1] == board[2][0] :
            bingos_x += 1
    
    # fault check
    if not (1 >= num_o - num_x >= 0) :
        answer = error
    elif bingos_o != 0 and num_o != num_x + 1 :
        answer = error
    elif bingos_x != 0 and num_o != num_x :
        answer = error
    elif bingos_o > 0 and bingos_x > 0 :
        answer = error
    elif bingos_o == 2 and num_o != 5 :
        answer = error
    else : # normal game
        answer = normal
        
    return answer