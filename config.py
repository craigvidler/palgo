import pygame

SCREENWIDTH, SCREENHEIGHT = 1200, 596
SCREENRECT = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
GRIDWIDTH = 714
GRIDHEIGHT = 567
GRIDMARGIN = 15
NODEMARGIN = 1
NODESIZE = 20
TEXTSIZE = 14
YPADDING = 2
XPADDING = 6
FILE = 'data/grid.txt'
NODECOLORS = ['gray25', 'aqua', 'orange', 'lime', 'pink', 'yellow', 'blue', 'chartreuse']
BKGCOLOR = 'gray35'
PANELCOLOR = 'gray35'
TEXTCOLOR = 'gray85'
FPS = 10
START = (0, 0)
END = (3, 3)

pygame.init()
pygame.display.set_caption('Palgo')
screen = pygame.display.set_mode(SCREENRECT.size)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Menlo', TEXTSIZE)
