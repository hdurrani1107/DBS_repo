"""
CHESS ENGINE:
THIS IS MY CHESS ENGINE THERE ARE MANY LIKE IT BUT THIS ONE IS MINE
"""

import datetime
import chess
import chess.polyglot
import chess.pgn
import chess.uci

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

def minimax(alpha, beta, depthleft):
    """
    Minimax depth search algorithm, checks legal moves for best move recursively
    """
    bestscore = -9999
    if (depthleft == 0):
        return quies(alpha,beta)
    for move in chess_board.legal_moves:
        chess_board.push(move)
        score = -minimax(-beta,-alpha, depthleft-1)
        chess_board.pop()
        if score >= beta:
            return beta
        if score > bestscore:
            bestscore = score
        if score > alpha:
            alpha = score
    return bestscore

def quies(alpha,beta):
    """
    Prevents Horizon effect of minimax function getting stuck and lowest depth search
    """
    stand_pat = evaluate_board()
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat
    for move in chess_board.legal_moves:
        if chess_board.is_capture:
            chess_board.push(move)
            score = -quies(-beta, -alpha)
            chess_board.pop()
            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha

def selectmove(depth):
    """
    Puts engine together to produce optimal move includes chess books for optimal openings
    """
    try:
        move = chess.polyglot.MemoryMappedReader("baron30.bin").weighted_choice(chess_board).move()
        movehistory.append(move)
        return move
    except:
        bestmove = chess.Move.null()
        bestValue = -9999
        alpha = -100000
        beta = 100000
        for move in chess_board.legal_moves:
            chess_board.push(move)
            boardValue = -minimax(-beta,-alpha,depth-1)
            if boardValue > bestValue:
                bestValue = boardValue
            if (boardValue > alpha):
                alpha = boardValue
            chess_board.pop()
            movehistory.append(bestMove)
        return bestMove

def chess_game_play():
    """
    Function runs the actual chess game in the command prompt:
    """
    chess_board = chess.Board()
    movehistory =[]
    print("Chess Game:")
    #Work in progress: creating the actual board
    #Currently prints to command prompt
    print(chess_board)
    chess_game = 0

    while chess_game != 1:
        #Input actions white vs. black
        print("Whites Move:")
        white_pos = input("Input a move:")
        white_pos = chess.Move.from_uci(white_pos)
        chess_board.push(white_pos)
        print(chess_board)
        print("Black Move:")
        #black_pos = input("Input a move:")
        #black_pos = chess.Move.from_uci(black_pos)
        #chess_board.push(black_pos)
        move = selectmove(3)
        chess_board.push(move)
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
            chess_game = 1
            print("Check Mate, Game Over!")
        elif chess_board.is_stalemate is True:
            chess_game = 1
            print("Stalemate, Game Over!")
        elif chess_board.is_insufficient_material is True:
            chess_game = 1
            print("Insufficient Material, Game Over!")
        else:
            Chess_game = 0

def chess_game_play2():
    """
    Allows you to play against a chess engine
    """
    engine = chess.uci.popen_engine("C:\Users\hummy\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")
    engine.uci()
    engine.name

    movehistory =[]
    game = chess.pgn.Game()
    game.headers["Event"] = "Example"
    game.headers["Site"] = "Linz"
    game.headers["Date"] = str(datetime.datetime.now().date())
    game.headers["Round"] = 1
    game.headers["White"] = "MyChess"
    game.headers["Black"] = "Stockfish9"
    board = chess.Board()
    while not board.is_game_over(claim_draw=True):
        if board.turn:
            move = selectmove(3)
            board.push(move)       
        else:
            engine.position(board)
            move = engine.go(movetime=1000).bestmove
            movehistory.append(move)
            board.push(move)
        
    game.add_line(movehistory)
    game.headers["Result"] = str(board.result(claim_draw=True))
    print(game)
    print(game, file=open("test.pgn", "w"), end="\n\n")

if __name__ == '__main__':
    chess_game_play()
