import pygame

SCREENWIDTH, SCREENHEIGHT = 1200, 659
SCREENRECT = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
GRIDWIDTH = 714
GRIDHEIGHT = 630
GRIDMARGIN = 15
NODEMARGIN = 1
NODESIZE = 20
TEXTSIZE = 14
YPADDING = 2
XPADDING = 6
NODECOLORS = [
    '#404040',  # UNEXPLORED
    '#9B2226',  # CURRENT
    '#E9C46A',  # NEIGHBOR
    '#005F73',  # QUEUED
    '#0A9396',  # VISITED
    '#CA6702',  # PATH
    '#CA6702',  # START
    '#CA6702',  # END
]
TEXTCOLORS = [
    '#E9D8A6',  # UNEXPLORED
    '#E9D8A6',  # CURRENT
    '#E9D8A6',  # NEIGHBOR
    '#E9D8A6',  # QUEUED
    '#FFFFFF',  # VISITED
    '#FFFFFF',  # PATH
    '#FFFFFF',  # START
    '#FFFFFF',  # END
]
BKGCOLOR = 'gray35'
PANELCOLOR = 'gray35'
TEXTCOLOR = '#E9D8A6'
FILE = 'data/grid.txt'
FPS = 60
START = (0, 0)
END = (29, 29)

pygame.init()
pygame.display.set_caption('Palgo')
screen = pygame.display.set_mode(SCREENRECT.size)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Menlo', TEXTSIZE)
