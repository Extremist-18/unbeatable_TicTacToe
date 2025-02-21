import pygame
import copy  # Needed for deep copying board for minimax

pygame.init()

XO = 'X'
winner = None
draw = None
board = [[None]*3, [None]*3, [None]*3]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 500))  # Extra 100 pixels height for messages
pygame.display.set_caption("Tic Tac Toe")

ximg = pygame.image.load("x.png")
oimg = pygame.image.load("o.png")

ximg = pygame.transform.scale(ximg, (80, 80))
oimg = pygame.transform.scale(oimg, (80, 80))

def draw_grid():
    screen.fill((255, 255, 255), (0, 0, 400, 400))
    # horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (400/3, 0), (400/3, 400), 6)
    pygame.draw.line(screen, (0, 0, 0), (400/3*2, 0), (400/3*2, 400), 6)
    # vertical lines
    pygame.draw.line(screen, (0, 0, 0), (0, 400/3), (400, 400/3), 6)    
    pygame.draw.line(screen, (0, 0, 0), (0, 400/3*2), (400, 400/3*2), 6)
    pygame.display.update()

def is_cell_empty(row, col):
    return board[row-1][col-1] is None

def show_message(text_str, duration=1500):
    """Display a temporary message in the bottom area (400-500) for the given duration (milliseconds)."""
    # Clear bottom area
    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 400, 100))
    font = pygame.font.SysFont('Georgia', 30)
    text = font.render(text_str, True, (255, 0, 0))
    text_rect = text.get_rect(center=(400/2, 450))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(duration)
    # After delay, clear the message area and redraw board state
    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 400, 100))
    redraw_board()

def result():
    global winner, draw
    # Prepare the message based on game state
    if winner:
        message = winner + " wins!"
    elif draw:
        message = "It's a tie!"
    else:
        return

    # Display a temporary message in the bottom area (y=400 to y=500)
    font = pygame.font.SysFont('Georgia', 40)
    text = font.render(message, True, (255, 0, 0))
    # Clear the bottom message area with a black rectangle
    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 400, 100))
    text_rect = text.get_rect(center=(400/2, 450))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(1500)
    # After delay, clear the message area without affecting the board
    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 400, 100))
    pygame.display.update()
    
def redraw_board():
    """Redraw the current board state (images) after a temporary message."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                if i == 0:
                    posx = 30
                elif i == 1:
                    posx = 400/3 + 30
                elif i == 2:
                    posx = 400/3*2 + 30
                if j == 0:
                    posy = 30
                elif j == 1:
                    posy = 400/3 + 30
                elif j == 2:
                    posy = 400/3*2 + 30
                screen.blit(ximg, (posy, posx))
            elif board[i][j] == 'O':
                if i == 0:
                    posx = 30
                elif i == 1:
                    posx = 400/3 + 30
                elif i == 2:
                    posx = 400/3*2 + 30
                if j == 0:
                    posy = 30
                elif j == 1:
                    posy = 400/3 + 30
                elif j == 2:
                    posy = 400/3*2 + 30
                screen.blit(oimg, (posy, posx))
    pygame.display.update()

def minimax(bd, depth, isMaximizing):
    winner_local = wincases_board(bd)
    if winner_local == 'O':  # computer wins
        return 10 - depth
    elif winner_local == 'X':  # human wins
        return depth - 10
    elif checkTie(bd):
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for i in range(3):
            for j in range(3):
                if bd[i][j] is None:
                    bd[i][j] = 'O'
                    score = minimax(bd, depth + 1, False)
                    bd[i][j] = None
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if bd[i][j] is None:
                    bd[i][j] = 'X'
                    score = minimax(bd, depth + 1, True)
                    bd[i][j] = None
                    bestScore = min(bestScore, score)
        return bestScore

def get_best_move(bd):
    bestScore = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if bd[i][j] is None:
                bd[i][j] = 'O'
                score = minimax(bd, 0, False)
                bd[i][j] = None
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    return move

def wincases_board(bd):
    for i in range(3):
        if (bd[i][0] == bd[i][1] == bd[i][2]) and (bd[i][0] is not None):
            return bd[i][0]
        if (bd[0][i] == bd[1][i] == bd[2][i]) and (bd[0][i] is not None):
            return bd[0][i]
    if (bd[0][0] == bd[1][1] == bd[2][2]) and (bd[0][0] is not None):
        return bd[0][0]
    if (bd[0][2] == bd[1][1] == bd[2][0]) and (bd[0][2] is not None):
        return bd[0][2]
    return None

def wincases():
    global winner, draw, board
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pygame.draw.line(screen, (250, 0, 0), (0, (row+1)*400/3 - 400/6), (400, (row+1)*400/3 - 400/6), 4)
            result()
            return
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            pygame.draw.line(screen, (250, 0, 0), ((col+1)*400/3 - 400/6, 0), ((col+1)*400/3 - 400/6, 400), 4)
            result()
            return
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
        result()
        return
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]
        pygame.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
        result()
        return

def checkTie(bd):
    for row in bd:
        if None in row:
            return False
    return True

def getimg(row, col): 
    global board, XO
    if row == 1:
        posx = 30
    elif row == 2:    
        posx = 400/3 + 30
    elif row == 3:
        posx = 400/3*2 + 30     
    
    if col == 1:
        posy = 30   
    elif col == 2:
        posy = 400/3 + 30
    elif col == 3:
        posy = 400/3*2 + 30  

    board[row-1][col-1] = XO
    if XO == 'X':
        screen.blit(ximg, (posy, posx))
    else:   
        screen.blit(oimg, (posy, posx))
    pygame.display.update()
         
def input_to_block():
    global XO, winner, draw, board
    x, y = pygame.mouse.get_pos()
    
    if x < 400/3:
        col = 1
    elif x < 400/3*2:
        col = 2
    elif x < 400:
        col = 3       
    else:
        col = None
    
    if y < 400/3:
        row = 1     
    elif y < 400/3*2:
        row = 2 
    elif y < 400:
        row = 3
    else:
        row = None                  
    
    if row and col:
        if not is_cell_empty(row, col):
            show_message("Make a valid move!")
            return
        getimg(row, col)
        wincases()
    
    # If game is not over, let the computer move
    if winner is None and not checkTie(board):
        comp_move = get_best_move(copy.deepcopy(board))
        if comp_move is not None:
            i, j = comp_move
            board[i][j] = 'O'
            comp_row, comp_col = i+1, j+1
            if comp_row == 1:
                posx = 30
            elif comp_row == 2:    
                posx = 400/3 + 30
            elif comp_row == 3:
                posx = 400/3*2 + 30     
            if comp_col == 1:
                posy = 30   
            elif comp_col == 2:
                posy = 400/3 + 30
            elif comp_col == 3:
                posy = 400/3*2 + 30  
            screen.blit(oimg, (posy, posx))
            pygame.display.update()
            wincases()
        elif checkTie(board):
            draw = True
            result()

# Draw grid and then let the computer make the first move if the board is empty
draw_grid()
if all(all(cell is None for cell in row) for row in board):
    # Computer's turn as first move
    first_move = get_best_move(copy.deepcopy(board))
    if first_move is not None:
        # Alternatively, choose the center if available as the best first move:
        i, j = 1, 1   # Center cell is the best move on an empty board
        board[i][j] = 'O'
        comp_row, comp_col = i+1, j+1
        if comp_row == 1:
            posx = 30
        elif comp_row == 2:    
            posx = 400/3 + 30
        elif comp_row == 3:
            posx = 400/3*2 + 30     
        if comp_col == 1:
            posy = 30   
        elif comp_col == 2:
            posy = 400/3 + 30
        elif comp_col == 3:
            posy = 400/3*2 + 30  
        screen.blit(oimg, (posy, posx))
        pygame.display.update()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_to_block()
    pygame.display.update()
    clock.tick(30)
