"""
CHESS ENGINE:
THIS IS MY CHESS ENGINE THERE ARE MANY LIKE IT BUT THIS ONE IS MINE
"""

import chess

def evaluate_board():
    """
    Evaluates position to see who is in an advantageous position
    """
        
    pawntable = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10,-20,-20, 10, 10,  5,
    5, -5,-10,  0,  0,-10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0,  0,  0,  0,  0,  0,  0,  0]

    knightstable = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50]

    bishopstable = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -20,-10,-10,-10,-10,-10,-10,-20]

    rookstable = [
    0,  0,  0,  5,  5,  0,  0,  0,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    5, 10, 10, 10, 10, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0]

    queenstable = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  5,  5,  5,  5,  5,  0,-10,
    0,  0,  5,  5,  5,  5,  0, -5,
    -5,  0,  5,  5,  5,  5,  0, -5,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20]

    kingstable = [
    20, 30, 10,  0,  0, 10, 30, 20,
    20, 20,  0,  0,  0,  0, 20, 20,
    -10,-20,-20,-20,-20,-20,-20,-10,
    -20,-30,-30,-40,-40,-30,-30,-20,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30]

    if chess_board.is_checkmate():
        if chess_board.turn:
            return -9999
        else:
            return 9999
    if chess_board.is_stalemate():
        return 0
    if chess_board.is_insufficient_material():
        return 0
    wp = len(chess_board.pieces(chess.PAWN, chess.WHITE))
    bp = len(chess_board.pieces(chess.PAWN, chess.BLACK))
    wn = len(chess_board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(chess_board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(chess_board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(chess_board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(chess_board.pieces(chess.ROOK, chess.WHITE))
    br = len(chess_board.pieces(chess.ROOK, chess.BLACK))
    wq = len(chess_board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(chess_board.pieces(chess.QUEEN, chess.BLACK))
    material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)
    pawnsq = sum([pawntable[i] for i in chess_board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)] 
                                    for i in chess_board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in chess_board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] 
                                    for i in chess_board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([bishopstable[i] for i in chess_board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)] 
                                    for i in chess_board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in chess_board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] 
                                    for i in chess_board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in chess_board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)] 
                                    for i in chess_board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in chess_board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)] 
                                    for i in chess_board.pieces(chess.KING, chess.BLACK)])
    eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
    if chess_board.turn:
        return eval
    else:
        return -eval

print("Chess Game:")
#Work in progress: creating the actual board
chess_board = chess.Board()
print(chess_board)
game = 0



while game != 1:
    #Input actions white vs. black
    print("Whites Move:")
    white_pos = input("Input a move:")
    white_pos = chess.Move.from_uci(white_pos)
    chess_board.push(white_pos)
    print(chess_board)
    print("Black Move:")
    black_pos = input("Input a move:")
    black_pos = chess.Move.from_uci(black_pos)
    chess_board.push(black_pos)
    print(chess_board)
    #Advantge Evaluation
    advantage = evaluate_board()
    if advantage > 0:
        print("White Advantage: ", advantage)
    elif advantage < 0:
        print("Black Advantage: ", advantage)
    else:
        print("Even Advantage")

    #End Game Eval
    if chess_board.is_checkmate is True:
        game = 1
        print("Check Mate, Game Over!")
    elif chess_board.is_stalemate is True:
        game = 1
        print("Stalemate, Game Over!")
    elif chess_board.is_insufficient_material is True:
        game = 1
        print("Insufficient Material, Game Over!")
    else:
        game = 0