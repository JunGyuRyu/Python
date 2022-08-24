import tkinter as tk, random as r, pygame, ctypes, sys
from tkinter import messagebox
pygame.init()
pygame.display.set_caption("Math_Hopscotch")
BLACK = (230,230,230)
WHITE = (0, 0, 0)
GREEN = (0,255,0)
RED = (255, 0, 0)
SKYBLUE = (0, 255, 255)
GREEN2 = (0,255,128)
font = pygame.font.SysFont(None, 36)
size = [600,600]
screen = pygame.display.set_mode(size)
turn = 0 
grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

objects = []
done = False

clock = pygame.time.Clock()
turn = 0
KEY_DIRECTION = {
    pygame.K_UP: 'U',
    pygame.K_DOWN: 'D',
    pygame.K_LEFT: 'L',
    pygame.K_RIGHT: 'R',
}

def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 50, position[0] * 50),(50, 50))
    pygame.draw.rect(screen, color, block)
    
class Square:
    def __init__(self):
        self.positions = [(0,0)]
        self.direction = ''
        self.color=RED
 
    def draw(self):
        for position in self.positions:
            draw_block(screen, self.color, position)
    
    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'U':
            if y >= 1:
                self.positions = [(y - 1, x)]
        elif self.direction == 'D':
            if y <= 7:
                self.positions = [(y + 1, x)]
        elif self.direction == 'L':
            if x >= 1:
                self.positions = [(y, x - 1)]
        elif self.direction == 'R':
            if x <= 7:
                self.positions = [(y, x + 1)]

def result(p1Score, p2Score, Winner):
        MsgBox = tk.messagebox.askyesno (Winner, f'1P: {p1Score}   2P: {p2Score} \n\n Retry?')
        if MsgBox == True:
                runGame()

def runGame():
    global done, item_box
    CELL_SIZE = 50
    COLUMN_COUNT = 9
    ROW_COUNT = 9
    X_now, Y_now = 0, 0
    turn = 0
    turnCount = 0
    p1Score, p2Score = 0, 0
    item_index = 0
    item = 0
    myFont = pygame.font.Font( None, 30)
    item_rows = [0,0,0,0,0,0,0,0,0]
    
    for rows in range(9):
        if rows == 0:
                item_rows[rows] = r.randint(1,7)
        elif rows == 8:
                item_rows[rows] = r.randint(1,7)
        else:
                item_rows[rows] = r.randint(0,7)
    
    player1 = Square()
    player2 = Square()
    player2.positions = [(8,0)]
    player2.color = SKYBLUE
    RNumSrn = [[0]*9 for x in range(9)]
    for columns in range(COLUMN_COUNT):
            for rows in range(ROW_COUNT):
                    RNumSrn[columns][rows]=r.randint(1,10)
    while not done:
        Score = myFont.render(f'Score: {p1Score}', True, RED)
        Score2 = myFont.render(f'Score: {p2Score}', True, SKYBLUE)
        STurn = myFont.render(f'1P\'s TURN.', True, RED)
        STurn2 = myFont.render(f'2P\'s TURN.', True, SKYBLUE)
        Intro = myFont.render(f'If it reaches the right end,', True, BLACK)
        Intro2 = myFont.render(f'the person with the highest score wins.', True, BLACK)
        ShowTurn = myFont.render(f'turn {turnCount}', True, GREEN)
        clock.tick(10)
        screen.fill(WHITE)
        for columns in range(COLUMN_COUNT):
            for rows in range(ROW_COUNT):
                if RNumSrn[columns][rows] == 0:
                        image = font.render('{}'.format(RNumSrn[columns][rows]), True, RED)
                elif item_rows[rows] == columns:
                        image = font.render('{}'.format(RNumSrn[columns][rows]), True, GREEN2)
                        rect = (CELL_SIZE * columns, CELL_SIZE * rows, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, GREEN2, rect, 8)
                else:
                        image = font.render('{}'.format(RNumSrn[columns][rows]), True, BLACK)
                        rect = (CELL_SIZE * columns, CELL_SIZE * rows, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, BLACK, rect, 1)
                screen.blit(image, (CELL_SIZE * columns + 10, CELL_SIZE * rows + 10))
        
        for event in pygame.event.get():
                if turn == 0:
                        if event.type == pygame.QUIT:
                            done=True
                        elif event.type == pygame.KEYDOWN:
                            if event.key in KEY_DIRECTION:
                                player1.direction = KEY_DIRECTION[event.key]
                                player1.move()
                                X_now = player1.positions[0][1]
                                Y_now = player1.positions[0][0]
                                if (X_now,Y_now) == (item_rows[Y_now],Y_now):
                                        item_index = r.randint(-3,3)
                                        item = RNumSrn[X_now][Y_now]*item_index
                                        p1Score += item
                                        item = 0
                                else:
                                        p1Score += RNumSrn[X_now][Y_now]
                                RNumSrn[X_now][Y_now] = 0
                                turn += 1
                                turn = turn % 2
                                turnCount += 1
                elif turn == 1:
                        if event.type == pygame.QUIT:
                            done=True
                        elif event.type == pygame.KEYDOWN:
                            if event.key in KEY_DIRECTION:
                                player2.direction = KEY_DIRECTION[event.key]
                                player2.move()
                                X_now = player2.positions[0][1]
                                Y_now = player2.positions[0][0]
                                if (X_now,Y_now) == (item_rows[Y_now],Y_now):
                                        item_index = r.randint(-3,3)
                                        item = RNumSrn[X_now][Y_now]*item_index
                                        p2Score += item
                                        item = 0
                                else:
                                        p2Score += RNumSrn[X_now][Y_now]
                                RNumSrn[X_now][Y_now] = 0
                                turn += 1
                                turn = turn % 2
                                turnCount += 1
                                
        screen.blit(Score, [480, 100])
        screen.blit(Score2, [480, 200])
        screen.blit(ShowTurn, [485, 400])
        screen.blit(Intro, [10, 500])
        screen.blit(Intro2, [10, 530])
        
        if turn == 0:
            screen.blit(STurn, [470, 340])
        else:
            screen.blit(STurn2, [470, 340])
        
        for object in objects:
                object.process()

        if X_now == 8:
                if p1Score > p2Score:
                        result(p1Score, p2Score, 'P1 승리')
                        done = True
                elif p1Score < p2Score:
                        result(p1Score, p2Score, 'P2 승리')
                        done = True
                elif p1Score == p2Score:
                        result(p1Score, p2Score, '무승부')
                        done = True
        player1.draw()
        player2.draw()
        pygame.display.update()
runGame()
pygame.quit()
#코드 250줄
