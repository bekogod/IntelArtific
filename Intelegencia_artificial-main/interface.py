import pygame
import pygame.locals
from matplotlib import pyplot as plt
from matplotlib import colors
from mapa import Mapa
from player import Player
from vector import Vector
import time

#  Initialize th pygame
pygame.init()

# Cria display do tamanho do ecra
monitor_size = pygame.display.Info()
size = monitor_size.current_w, monitor_size.current_h
screen = pygame.display.set_mode(size)


# Player
playerImgRaw = pygame.image.load('imgs/racecar.png')
playerImg = pygame.transform.rotate(playerImgRaw, 270)

winImg = pygame.image.load('imgs/winner.png')
winImg = pygame.transform.scale(winImg, size)

# Title and icon
pygame.display.set_caption("VectorRace")
icon = pygame.image.load('imgs/icon.jpg')
icon_dimmed = pygame.image.load('imgs/icon_dimmed2.jpg')
icon_dimmed = pygame.transform.scale(icon_dimmed, size)
pygame.display.set_icon(icon)

# Game States
game_menu = "main_menu"

# Introduz texto para o menu


def drawText(text, font, text_col, x, y):
    texto = font.render(text, True, text_col)
    screen.blit(texto, (x, y))


# Desenha o Mapa
def drawMap(screen, mapa, players):

    MAP_SCALE_X = round(monitor_size.current_w/mapa.rows)
    MAP_SCALE_Y = round(monitor_size.current_h/mapa.lines)
    #MAP_SCALE = 128

    content = mapa.content
    colors = [pygame.Color("black"), pygame.Color(
        "grey"), pygame.Color("green"), pygame.Color("red")]
    for line in range(mapa.lines):
        for row in range(mapa.rows):
            pygame.draw.rect(screen, colors[content[line][row]], pygame.Rect(
                row*MAP_SCALE_X, line*MAP_SCALE_Y, MAP_SCALE_X, MAP_SCALE_Y))
    
    for player in players:
        x = player.estado.x * MAP_SCALE_X
        y = (mapa.lines-player.estado.y-1) * MAP_SCALE_Y
        playerImgFinal = pygame.transform.scale(
            playerImg, (MAP_SCALE_X, MAP_SCALE_Y))
        screen.blit(playerImgFinal, (x, y))
    
    drawText("ESC to return", FONT, COLOR_WHITE, 50, 50)
    


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

FONT = pygame.font.SysFont("arielblack", 40)

WIDTH = monitor_size.current_w
HEIGHT = monitor_size.current_h

MENU_BUTTON_X = WIDTH/20
MENU_BUTTON_Y = HEIGHT/4

SPACE_BETWEEN = 60

def createButton(text, number,color):
    
    rect = pygame.draw.rect(screen, color,
                            pygame.Rect(MENU_BUTTON_X, MENU_BUTTON_Y + number * SPACE_BETWEEN , 400, 50))

    drawText(text, FONT,
             COLOR_WHITE, MENU_BUTTON_X + 10, MENU_BUTTON_Y + number * SPACE_BETWEEN + 10)
    
    return rect

def createButton2(text, number,color):
    
    rect = pygame.draw.rect(screen, color,
                            pygame.Rect(MENU_BUTTON_X + 420, MENU_BUTTON_Y + number * SPACE_BETWEEN , 400, 50))

    drawText(text, FONT,
             COLOR_WHITE, MENU_BUTTON_X + 420 + 10, MENU_BUTTON_Y + number * SPACE_BETWEEN + 10)
    
    return rect

def drawMapsMenu(selected):
    screen.fill((50, 50, 50))
    
    map1 = createButton("Mapa Default", 0,COLOR_BLACK)
    map2 = createButton("Mapa Circle", 1,COLOR_BLACK)
    map3 = createButton("Mapa Simple", 2,COLOR_BLACK)
    map4 = createButton("Mapa Big", 3,COLOR_BLACK)
    leave = createButton("Leave", 5,COLOR_BLACK)
    
    
    if selected == 0:                        
        map1 = createButton("Mapa Default", 0,COLOR_RED)
    elif selected == 1:
        map2 = createButton("Mapa Circle", 1,COLOR_RED)
    elif selected == 2:
        map3 = createButton("Mapa Simple", 2,COLOR_RED)
    elif selected == 3:
        map3 = createButton("Mapa Big", 3,COLOR_RED)
    else:
        pass
        
        
    return map1, map2, map3,map4, leave

def drawJogMenu(selected):
    screen.fill((50, 50, 50))
    
    one = createButton("Um jogador", 0,COLOR_BLACK)
    two = createButton("Dois jogadores", 1,COLOR_BLACK)
    leave = createButton("Leave", 3,COLOR_BLACK)
    
    
    if selected == 0:                        
        one = createButton("Um jogador", 0,COLOR_RED)
    elif selected == 1:
        two = createButton("Dois jogadores", 1,COLOR_RED)
    else:
        pass
        
        
    return one,two, leave



def drawAlgoritmosMenu(selected,players):
    screen.fill((50, 50, 50))
    
    selected = players[0].alg_selected
    selected2 = players[1].alg_selected
    
    
    a_estrela = createButton("A*", 0,COLOR_BLACK)
    greedybf = createButton("GreedyBF", 1,COLOR_BLACK)
    greedy = createButton("Greedy", 2,COLOR_BLACK)
    bfs = createButton("BFS", 3,COLOR_BLACK)
    dfs = createButton("DFS", 4,COLOR_BLACK)
    
    a_estrela2 = createButton2("A*", 0,COLOR_BLACK)
    greedybf2 = createButton2("GreedyBF", 1,COLOR_BLACK)
    greedy2 = createButton2("Greedy", 2,COLOR_BLACK)
    bfs2 = createButton2("BFS", 3,COLOR_BLACK)
    dfs2 = createButton2("DFS", 4,COLOR_BLACK)
    
    
    leave_alg = createButton("Leave", 6,COLOR_BLACK)

    
    
    if selected == 0:                        
        a_estrela = createButton("A*", 0,COLOR_RED)
    elif selected == 1:
        greedybf = createButton("GreedyBF", 1,COLOR_RED)
    elif selected == 2:
         greedy = createButton("Greedy", 2,COLOR_RED)
    elif selected == 3:
        bfs = createButton("BFS", 3,COLOR_RED)
    elif selected == 4:
        dfs = createButton("DFS", 4,COLOR_RED)
    else:
        pass
    
    if selected2 == 0:                        
        a_estrela2 = createButton2("A*", 0,COLOR_RED)
    elif selected2 == 1:
        greedybf2 = createButton2("GreedyBF", 1,COLOR_RED)
    elif selected2 == 2:
         greedy2 = createButton2("Greedy", 2,COLOR_RED)
    elif selected2 == 3:
        bfs2 = createButton2("BFS", 3,COLOR_RED)
    elif selected2 == 4:
        dfs2 = createButton2("DFS", 4,COLOR_RED)
    else:
        pass
        
        
    return a_estrela, greedybf, greedy, bfs, dfs,a_estrela2, greedybf2, greedy2, bfs2, dfs2, leave_alg

def drawPathMenu():
    screen.fill((50, 50, 50))
    
    
    a_estrela = createButton("A*", 0,COLOR_BLACK)
    greedybf = createButton("GreedyBF", 1,COLOR_BLACK)
    greedy = createButton("Greedy", 2,COLOR_BLACK)
    bfs = createButton("BFS", 3,COLOR_BLACK)
    dfs = createButton("DFS", 4,COLOR_BLACK)
    
    leave_alg = createButton("Leave", 6,COLOR_BLACK)

    
        
    return a_estrela, greedybf, greedy, bfs, dfs,leave_alg


def buttonIndex(buttonList,mousePos):
    i = 0
    for button in buttonList:
        if button.collidepoint(mousePos):
            return i
        i += 1
    
    return -1

def getPltXY( path):
        """Retorna o caminho PLT

        Args:
            path (List): Lista com nodos do caminho

        Returns:
            Tuple: Tuplo de uma Lista de todos os x's e outra de todos os y's para serem desenhados
        """
        xpath = [x + 0.5 for (x, y) in path]
        ypath = [y + 0.5 for (x, y) in path]
        return (xpath, ypath)

def showPath( path, final=False):
        """Mostra o caminho PLT

        Args:
            path (List): Lista com todos os nodos do caminho
            final (bool, optional): Quando é TRUE, demonstra o mapa. Quando é FALSE, guarda em cache e
            mostra mais tarde com o plt.show()
        """
        x, y = getPltXY(path)
        plt.plot(x, y, 'b.--', linewidth=2, markersize=20)

        if final:
            plt.show()
