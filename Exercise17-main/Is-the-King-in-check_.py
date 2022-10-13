
# Case:

# You have to write a function that takes for input a 8x8 chessboard in the form of a bi-dimensional array of chars (or strings of length 1, depending on
# the language) and returns a boolean indicating whether the king is in check.
# The array will include 64 squares which can contain the following characters :
#    - '♔' for the black King;
#    - '♛' for a white Queen;
#    - '♝' for a white Bishop;
#    - '♞' for a white Knight;
#    - '♜' for a white Rook;
#    - '♟' for a white Pawn;
#    - ' ' (a space) if there is no piece on that square.
# Note : these are actually inverted-color chess Unicode characters because the codewars dark theme makes 
# the white appear black and vice versa. Use the characters shown above.
# There will always be exactly one king, which is the black king, whereas all the other pieces are white.
# The board is oriented from Black's perspective.
# Remember that pawns can only move and take forward.
# Also be careful with the pieces' lines of sight ;-).

# Solution1:

def king_is_in_check(chessboard):
    king = '♔'
    king_pos = ['','']
    queen = '♛'
    queen1_pos = ['','']
    queen2_pos = ['','']
    queen3_pos = ['','']
    bishop = '♝'
    bishop1_pos = ['','']
    bishop2_pos = ['','']
    bishop3_pos = ['','']
    knight = '♞'
    knight1_pos = ['','']
    knight2_pos = ['','']
    knight3_pos = ['','']
    rook = '♜'
    rook1_pos = ['','']
    rook2_pos = ['','']
    rook3_pos = ['','']
    pawn = '♟'
    pawn1_pos = ['','']
    pawn2_pos = ['','']
    pawn3_pos = ['','']
    for row, s in enumerate(chessboard):
        for col, i in enumerate(s):
            if i == king:
                king_pos = [row,col]
            if i == queen:
                if queen1_pos == ['','']:
                    queen1_pos = [row,col]
                elif queen2_pos == ['','']:
                    queen2_pos = [row,col]
                else:
                    queen3_pos = [row,col]
            if i == bishop:
                if bishop1_pos == ['','']:
                    bishop1_pos = [row,col]
                elif bishop2_pos == ['','']:
                    bishop2_pos = [row,col]
                else:
                    bishop3_pos = [row,col]
            if i == knight:
                if knight1_pos == ['','']:
                    knight1_pos = [row,col]
                elif knight2_pos == ['','']:
                    knight2_pos = [row,col]
                else:
                    knight3_pos = [row,col]
            if i == rook:
                if rook1_pos == ['','']:
                    rook1_pos = [row,col]
                elif rook2_pos == ['','']:
                    rook2_pos = [row,col]
                else:
                    rook3_pos = [row,col]
            if i == pawn:
                if pawn1_pos == ['','']:
                    pawn1_pos = [row,col]
                elif pawn2_pos == ['','']:
                    pawn2_pos = [row,col]
                else:
                    pawn3_pos = [row,col]
    all_non_king_pos = [queen1_pos,queen2_pos,queen3_pos,bishop1_pos,bishop2_pos,bishop3_pos,knight1_pos,knight2_pos,knight3_pos,rook1_pos,rook2_pos,rook3_pos,pawn1_pos,pawn2_pos,pawn3_pos]
    print("Positions","\n","King:",king_pos,"\n","Queen1:",queen1_pos,"\n","Queen2:",queen2_pos,"\n","Queen3:",queen3_pos,"\n","Bishop1:",bishop1_pos,"\n","Bishop2:",bishop2_pos,"\n","Bishop3:",bishop3_pos,"\n","Knight1:",knight1_pos,"\n","Knight2:",knight2_pos,"\n","Knight3:",knight3_pos,"\n","Rook1:",rook1_pos,"\n","Rook2:",rook2_pos,"\n","Rook3:",rook3_pos,"\n","Pawn1:",pawn1_pos,"\n","Pawn2:",pawn2_pos,"\n","Pawn3:",pawn3_pos,"\n")
    queen1_moves = []
    if queen1_pos != ['','']:
        for n in range (1,8):
            if queen1_pos[0]-n >= 0 and queen1_pos[0]-n <= 7 and queen1_pos[1]-n >= 0 and queen1_pos[1]-n <= 7:
                if [queen1_pos[0]-n,queen1_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0]-n,queen1_pos[1]-n])
        for n in range (1,8):
            if queen1_pos[0]+n >= 0 and queen1_pos[0]+n <= 7 and queen1_pos[1]+n >= 0 and queen1_pos[1]+n <= 7:
                if [queen1_pos[0]+n,queen1_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0]+n,queen1_pos[1]+n])
        for n in range (1,8):
            if queen1_pos[0]+n >= 0 and queen1_pos[0]+n <= 7 and queen1_pos[1]-n >= 0 and queen1_pos[1]-n <= 7:
                if [queen1_pos[0]+n,queen1_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0]+n,queen1_pos[1]-n])
        for n in range (1,8):
            if queen1_pos[0]-n >= 0 and queen1_pos[0]-n <= 7 and queen1_pos[1]+n >= 0 and queen1_pos[1]+n <= 7:
                if [queen1_pos[0]-n,queen1_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0]-n,queen1_pos[1]+n])
        for n in range (1,8):
            if queen1_pos[0]+n <= 7:
                if [queen1_pos[0]+n,queen1_pos[1]] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0]+n,queen1_pos[1]])
        for n in range (1,8):
            if queen1_pos[0]-n >= 0:
                if [queen1_pos[0]-n,queen1_pos[1]] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0]-n,queen1_pos[1]])
        for n in range (1,8):
            if queen1_pos[1]+n <= 7:
                if [queen1_pos[0],queen1_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0],queen1_pos[1]+n])
        for n in range (1,8):
            if queen1_pos[1]-n >= 0:
                if [queen1_pos[0],queen1_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen1_moves.append([queen1_pos[0],queen1_pos[1]-n])
    queen2_moves = []
    if queen2_pos != ['','']:
        for n in range (1,8):
            if queen2_pos[0]-n >= 0 and queen2_pos[0]-n <= 7 and queen2_pos[1]-n >= 0 and queen2_pos[1]-n <= 7:
                if [queen2_pos[0]-n,queen2_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0]-n,queen2_pos[1]-n])
        for n in range (1,8):
            if queen2_pos[0]+n >= 0 and queen2_pos[0]+n <= 7 and queen2_pos[1]+n >= 0 and queen2_pos[1]+n <= 7:
                if [queen2_pos[0]+n,queen2_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0]+n,queen2_pos[1]+n])
        for n in range (1,8):
            if queen2_pos[0]+n >= 0 and queen2_pos[0]+n <= 7 and queen2_pos[1]-n >= 0 and queen2_pos[1]-n <= 7:
                if [queen2_pos[0]+n,queen2_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0]+n,queen2_pos[1]-n])
        for n in range (1,8):
            if queen2_pos[0]-n >= 0 and queen2_pos[0]-n <= 7 and queen2_pos[1]+n >= 0 and queen2_pos[1]+n <= 7:
                if [queen2_pos[0]-n,queen2_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0]-n,queen2_pos[1]+n])
        for n in range (1,8):
            if queen2_pos[0]+n <= 7:
                if [queen2_pos[0]+n,queen2_pos[1]] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0]+n,queen2_pos[1]])
        for n in range (1,8):
            if queen2_pos[0]-n >= 0:
                if [queen2_pos[0]-n,queen2_pos[1]] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0]-n,queen2_pos[1]])
        for n in range (1,8):
            if queen2_pos[1]+n <= 7:
                if [queen2_pos[0],queen2_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0],queen2_pos[1]+n])
        for n in range (1,8):
            if queen2_pos[1]-n >= 0:
                if [queen2_pos[0],queen2_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen2_moves.append([queen2_pos[0],queen2_pos[1]-n])
    queen3_moves = []
    if queen3_pos != ['','']:
        for n in range (1,8):
            if queen3_pos[0]-n >= 0 and queen3_pos[0]-n <= 7 and queen3_pos[1]-n >= 0 and queen3_pos[1]-n <= 7:
                if [queen3_pos[0]-n,queen3_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0]-n,queen3_pos[1]-n])
        for n in range (1,8):
            if queen3_pos[0]+n >= 0 and queen3_pos[0]+n <= 7 and queen3_pos[1]+n >= 0 and queen3_pos[1]+n <= 7:
                if [queen3_pos[0]+n,queen3_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0]+n,queen3_pos[1]+n])
        for n in range (1,8):
            if queen3_pos[0]+n >= 0 and queen3_pos[0]+n <= 7 and queen3_pos[1]-n >= 0 and queen3_pos[1]-n <= 7:
                if [queen3_pos[0]+n,queen3_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0]+n,queen3_pos[1]-n])
        for n in range (1,8):
            if queen3_pos[0]-n >= 0 and queen3_pos[0]-n <= 7 and queen3_pos[1]+n >= 0 and queen3_pos[1]+n <= 7:
                if [queen3_pos[0]-n,queen3_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0]-n,queen3_pos[1]+n])
        for n in range (1,8):
            if queen3_pos[0]+n <= 7:
                if [queen3_pos[0]+n,queen3_pos[1]] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0]+n,queen3_pos[1]])
        for n in range (1,8):
            if queen3_pos[0]-n >= 0:
                if [queen3_pos[0]-n,queen3_pos[1]] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0]-n,queen3_pos[1]])
        for n in range (1,8):
            if queen3_pos[1]+n <= 7:
                if [queen3_pos[0],queen3_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0],queen3_pos[1]+n])
        for n in range (1,8):
            if queen3_pos[1]-n >= 0:
                if [queen3_pos[0],queen3_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    queen3_moves.append([queen3_pos[0],queen3_pos[1]-n])
    bishop1_moves = []
    if bishop1_pos != ['','']:
        for n in range (1,8):
            if bishop1_pos[0]-n >= 0 and bishop1_pos[0]-n <= 7 and bishop1_pos[1]-n >= 0 and bishop1_pos[1]-n <= 7:
                if [bishop1_pos[0]-n,bishop1_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    bishop1_moves.append([bishop1_pos[0]-n,bishop1_pos[1]-n])
        for n in range (1,8):
            if bishop1_pos[0]+n >= 0 and bishop1_pos[0]+n <= 7 and bishop1_pos[1]+n >= 0 and bishop1_pos[1]+n <= 7:
                if [bishop1_pos[0]+n,bishop1_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    bishop1_moves.append([bishop1_pos[0]+n,bishop1_pos[1]+n])
        for n in range (1,8):
            if bishop1_pos[0]+n >= 0 and bishop1_pos[0]+n <= 7 and bishop1_pos[1]-n >= 0 and bishop1_pos[1]-n <= 7:
                if [bishop1_pos[0]+n,bishop1_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    bishop1_moves.append([bishop1_pos[0]+n,bishop1_pos[1]-n])
        for n in range (1,8):
            if bishop1_pos[0]-n >= 0 and bishop1_pos[0]-n <= 7 and bishop1_pos[1]+n >= 0 and bishop1_pos[1]+n <= 7:
                if [bishop1_pos[0]-n,bishop1_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    bishop1_moves.append([bishop1_pos[0]-n,bishop1_pos[1]+n])
    bishop2_moves = []
    if bishop2_pos != ['','']:
        for n in range (1,8):
            if bishop2_pos[0]-n >= 0 and bishop2_pos[0]-n <= 7 and bishop2_pos[1]-n >= 0 and bishop2_pos[1]-n <= 7:
                if [bishop2_pos[0]-n,bishop2_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    bishop2_moves.append([bishop2_pos[0]-n,bishop2_pos[1]-n])
        for n in range (1,8):
            if bishop2_pos[0]+n >= 0 and bishop2_pos[0]+n <= 7 and bishop2_pos[1]+n >= 0 and bishop2_pos[1]+n <= 7:
                if [bishop2_pos[0]+n,bishop2_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    bishop2_moves.append([bishop2_pos[0]+n,bishop2_pos[1]+n])
        for n in range (1,8):
            if bishop2_pos[0]+n >= 0 and bishop2_pos[0]+n <= 7 and bishop2_pos[1]-n >= 0 and bishop2_pos[1]-n <= 7:
                if [bishop2_pos[0]+n,bishop2_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    bishop2_moves.append([bishop2_pos[0]+n,bishop2_pos[1]-n])
        for n in range (1,8):
            if bishop2_pos[0]-n >= 0 and bishop2_pos[0]-n <= 7 and bishop2_pos[1]+n >= 0 and bishop2_pos[1]+n <= 7:
                if [bishop2_pos[0]-n,bishop2_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    bishop2_moves.append([bishop2_pos[0]-n,bishop2_pos[1]+n])
    bishop3_moves = []
    if bishop3_pos != ['','']:
        for n in range (1,8):
            if bishop3_pos[0]-n >= 0 and bishop3_pos[0]-n <= 7 and bishop3_pos[1]-n >= 0 and bishop3_pos[1]-n <= 7:
                if [bishop3_pos[0]-n,bishop3_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    bishop3_moves.append([bishop3_pos[0]-n,bishop3_pos[1]-n])
        for n in range (1,8):
            if bishop3_pos[0]+n >= 0 and bishop3_pos[0]+n <= 7 and bishop3_pos[1]+n >= 0 and bishop3_pos[1]+n <= 7:
                if [bishop3_pos[0]+n,bishop3_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    bishop3_moves.append([bishop3_pos[0]+n,bishop3_pos[1]+n])
        for n in range (1,8):
            if bishop3_pos[0]+n >= 0 and bishop3_pos[0]+n <= 7 and bishop3_pos[1]-n >= 0 and bishop3_pos[1]-n <= 7:
                if [bishop3_pos[0]+n,bishop3_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    bishop3_moves.append([bishop3_pos[0]+n,bishop3_pos[1]-n])
        for n in range (1,8):
            if bishop3_pos[0]-n >= 0 and bishop3_pos[0]-n <= 7 and bishop3_pos[1]+n >= 0 and bishop3_pos[1]+n <= 7:
                if [bishop3_pos[0]-n,bishop3_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    bishop3_moves.append([bishop3_pos[0]-n,bishop3_pos[1]+n])
    rook1_moves = []
    if rook1_pos != ['','']:
        for n in range (1,8):
            if rook1_pos[0]+n <= 7:
                if [rook1_pos[0]+n,rook1_pos[1]] in all_non_king_pos:
                    break
                else:
                    rook1_moves.append([rook1_pos[0]+n,rook1_pos[1]])
        for n in range (1,8):
            if rook1_pos[0]-n >= 0:
                if [rook1_pos[0]-n,rook1_pos[1]] in all_non_king_pos:
                    break
                else:
                    rook1_moves.append([rook1_pos[0]-n,rook1_pos[1]])
        for n in range (1,8):
            if rook1_pos[1]+n <= 7:
                if [rook1_pos[0],rook1_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    rook1_moves.append([rook1_pos[0],rook1_pos[1]+n])
        for n in range (1,8):
            if rook1_pos[1]-n >= 0:
                if [rook1_pos[0],rook1_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    rook1_moves.append([rook1_pos[0],rook1_pos[1]-n])
    rook2_moves = []
    if rook2_pos != ['','']:
        for n in range (1,8):
            if rook2_pos[0]+n <= 7:
                if [rook2_pos[0]+n,rook2_pos[1]] in all_non_king_pos:
                    break
                else:
                    rook2_moves.append([rook2_pos[0]+n,rook2_pos[1]])
        for n in range (1,8):
            if rook2_pos[0]-n >= 0:
                if [rook2_pos[0]-n,rook2_pos[1]] in all_non_king_pos:
                    break
                else:
                    rook2_moves.append([rook2_pos[0]-n,rook2_pos[1]])
        for n in range (1,8):
            if rook2_pos[1]+n <= 7:
                if [rook2_pos[0],rook2_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    rook2_moves.append([rook2_pos[0],rook2_pos[1]+n])
        for n in range (1,8):
            if rook2_pos[1]-n >= 0:
                if [rook2_pos[0],rook2_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    rook2_moves.append([rook2_pos[0],rook2_pos[1]-n])
    rook3_moves = []
    if rook3_pos != ['','']:
        for n in range (1,8):
            if rook3_pos[0]+n <= 7:
                if [rook3_pos[0]+n,rook3_pos[1]] in all_non_king_pos:
                    break
                else:
                    rook3_moves.append([rook3_pos[0]+n,rook3_pos[1]])
        for n in range (1,8):
            if rook3_pos[0]-n >= 0:
                if [rook3_pos[0]-n,rook3_pos[1]] in all_non_king_pos:
                    break
                else:
                    rook3_moves.append([rook3_pos[0]-n,rook3_pos[1]])
        for n in range (1,8):
            if rook3_pos[1]+n <= 7:
                if [rook3_pos[0],rook3_pos[1]+n] in all_non_king_pos:
                    break
                else:
                    rook3_moves.append([rook3_pos[0],rook3_pos[1]+n])
        for n in range (1,8):
            if rook3_pos[1]-n >= 0:
                if [rook3_pos[0],rook3_pos[1]-n] in all_non_king_pos:
                    break
                else:
                    rook3_moves.append([rook3_pos[0],rook3_pos[1]-n])
    knight1_moves = []
    if knight1_pos != ['','']:
        if knight1_pos[0]-2 >= 0 and knight1_pos[1]-1 >= 0:
            knight1_moves.append([knight1_pos[0]-2,knight1_pos[1]-1])
        if knight1_pos[0]-2 >= 0 and knight1_pos[1]+1 >= 0:
            knight1_moves.append([knight1_pos[0]-2,knight1_pos[1]+1])
        if knight1_pos[0]-1 >= 0 and knight1_pos[1]+2 >= 0:
            knight1_moves.append([knight1_pos[0]-1,knight1_pos[1]+2])
        if knight1_pos[0]+1 >= 0 and knight1_pos[1]+2 >= 0:
            knight1_moves.append([knight1_pos[0]+1,knight1_pos[1]+2])
        if knight1_pos[0]+2 >= 0 and knight1_pos[1]-1 >= 0:
            knight1_moves.append([knight1_pos[0]+2,knight1_pos[1]-1])
        if knight1_pos[0]+2 >= 0 and knight1_pos[1]+1 >= 0:
            knight1_moves.append([knight1_pos[0]+2,knight1_pos[1]+1])
        if knight1_pos[0]-1 >= 0 and knight1_pos[1]-2 >= 0:
            knight1_moves.append([knight1_pos[0]-1,knight1_pos[1]-2])
        if knight1_pos[0]+1 >= 0 and knight1_pos[1]-2 >= 0:
            knight1_moves.append([knight1_pos[0]+1,knight1_pos[1]-2])
    knight2_moves = []
    if knight2_pos != ['','']:
        if knight2_pos[0]-2 >= 0 and knight2_pos[1]-1 >= 0:
            knight2_moves.append([knight2_pos[0]-2,knight2_pos[1]-1])
        if knight2_pos[0]-2 >= 0 and knight2_pos[1]+1 >= 0:
            knight2_moves.append([knight2_pos[0]-2,knight2_pos[1]+1])
        if knight2_pos[0]-1 >= 0 and knight2_pos[1]+2 >= 0:
            knight2_moves.append([knight2_pos[0]-1,knight2_pos[1]+2])
        if knight2_pos[0]+1 >= 0 and knight2_pos[1]+2 >= 0:
            knight2_moves.append([knight2_pos[0]+1,knight2_pos[1]+2])
        if knight2_pos[0]+2 >= 0 and knight2_pos[1]-1 >= 0:
            knight2_moves.append([knight2_pos[0]+2,knight2_pos[1]-1])
        if knight2_pos[0]+2 >= 0 and knight2_pos[1]+1 >= 0:
            knight2_moves.append([knight2_pos[0]+2,knight2_pos[1]+1])
        if knight2_pos[0]-1 >= 0 and knight2_pos[1]-2 >= 0:
            knight2_moves.append([knight2_pos[0]-1,knight2_pos[1]-2])
        if knight2_pos[0]+1 >= 0 and knight2_pos[1]-2 >= 0:
            knight2_moves.append([knight2_pos[0]+1,knight2_pos[1]-2])
    knight3_moves = []
    if knight3_pos != ['','']:
        if knight3_pos[0]-2 >= 0 and knight3_pos[1]-1 >= 0:
            knight3_moves.append([knight3_pos[0]-2,knight3_pos[1]-1])
        if knight3_pos[0]-2 >= 0 and knight3_pos[1]+1 >= 0:
            knight3_moves.append([knight3_pos[0]-2,knight3_pos[1]+1])
        if knight3_pos[0]-1 >= 0 and knight3_pos[1]+2 >= 0:
            knight3_moves.append([knight3_pos[0]-1,knight3_pos[1]+2])
        if knight3_pos[0]+1 >= 0 and knight3_pos[1]+2 >= 0:
            knight3_moves.append([knight3_pos[0]+1,knight3_pos[1]+2])
        if knight3_pos[0]+2 >= 0 and knight3_pos[1]-1 >= 0:
            knight3_moves.append([knight3_pos[0]+2,knight3_pos[1]-1])
        if knight3_pos[0]+2 >= 0 and knight3_pos[1]+1 >= 0:
            knight3_moves.append([knight3_pos[0]+2,knight3_pos[1]+1])
        if knight3_pos[0]-1 >= 0 and knight3_pos[1]-2 >= 0:
            knight3_moves.append([knight3_pos[0]-1,knight3_pos[1]-2])
        if knight3_pos[0]+1 >= 0 and knight3_pos[1]-2 >= 0:
            knight3_moves.append([knight3_pos[0]+1,knight3_pos[1]-2])
    pawn1_moves = []
    if pawn1_pos != ['','']:
        if pawn1_pos[0]+1 >= 0 and pawn1_pos[1]+1 >= 0:
                pawn1_moves.append([pawn1_pos[0]+1,pawn1_pos[1]+1])
        if pawn1_pos[0]+1 >= 0 and pawn1_pos[1]-1 <= 7:
                pawn1_moves.append([pawn1_pos[0]+1,pawn1_pos[1]-1])
    pawn2_moves = []
    if pawn2_pos != ['','']:
        if pawn2_pos[0]+1 >= 0 and pawn2_pos[1]+1 >= 0:
                pawn2_moves.append([pawn2_pos[0]+1,pawn2_pos[1]+1])
        if pawn2_pos[0]+1 >= 0 and pawn2_pos[1]-1 <= 7:
                pawn2_moves.append([pawn2_pos[0]+1,pawn2_pos[1]-1])
    pawn3_moves = []
    if pawn3_pos != ['','']:
        if pawn3_pos[0]+1 >= 0 and pawn3_pos[1]+1 >= 0:
                pawn3_moves.append([pawn3_pos[0]+1,pawn3_pos[1]+1])
        if pawn3_pos[0]+1 >= 0 and pawn3_pos[1]-1 <= 7:
                pawn3_moves.append([pawn3_pos[0]+1,pawn3_pos[1]-1])
    print("KING POS:",king_pos)          
    print("Queen1 moves: ",queen1_moves)
    print("Queen2 moves: ",queen2_moves)
    print("Queen3 moves: ",queen3_moves)
    print("Bishop1 moves: ",bishop1_moves)
    print("Bishop2 moves: ",bishop2_moves)
    print("Bishop3 moves: ",bishop3_moves)
    print("Knight1 moves: ",knight1_moves)
    print("Knight2 moves: ",knight2_moves)
    print("Knight3 moves: ",knight3_moves)
    print("Rook moves1: ",rook1_moves)
    print("Rook moves2: ",rook2_moves)
    print("Rook moves3: ",rook3_moves)
    print("Pawn1 moves: ",pawn1_moves)
    print("Pawn2 moves: ",pawn2_moves)
    print("Pawn3 moves: ",pawn3_moves)
    if king_pos in queen1_moves:
        return True
    elif king_pos in queen2_moves:
        return True
    elif king_pos in queen3_moves:
        return True
    elif king_pos in bishop1_moves:
        return True
    elif king_pos in bishop2_moves:
        return True
    elif king_pos in bishop3_moves:
        return True
    elif king_pos in knight1_moves:
        return True
    elif king_pos in knight2_moves:
        return True
    elif king_pos in knight3_moves:
        return True
    elif king_pos in rook1_moves:
        return True
    elif king_pos in rook2_moves:
        return True
    elif king_pos in rook3_moves:
        return True
    elif king_pos in pawn1_moves:
        return True
    elif king_pos in pawn2_moves:
        return True
    elif king_pos in pawn3_moves:
        return True
    else:
        return False

# Solution2:

MOVES = {
    '♜': [[x*m for m in range(1,9)] for x in (-1,-1j,1,1j)],
    '♝': [[x*m for m in range(1,9)] for x in (-1-1j,-1+1j,1-1j,1+1j)],
    '♞': [[x+1j*m] for m in range(-2,3) for x in range(-2,3) if abs(x*m) == 2],
    '♟': [[1-1j], [1+1j]],
}
MOVES['♛'] = MOVES['♜'] + MOVES['♝']

def king_is_in_check(chessboard):
    pieces = {x + 1j * y: piece for x, row in enumerate(chessboard)
              for y, piece in enumerate(row) if piece != ' '}
    for z, piece in pieces.items():
        for it in MOVES.get(piece, ()):
            for dz in it:
                if z+dz in pieces:
                    if pieces.get(z+dz) == '♔':
                        return True
                    break
    return False

  # The second solution it is not mine but because it was much sorter i thought it was better showing it.
  
