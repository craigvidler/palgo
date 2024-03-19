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
NODECOLORS = [
    ('gray25', '#E9D8A6'),  # UNEXPLORED = 0
    ('#EE9B00', '#E9D8A6'),  # CURRENT = 1
    ('#e9c46a', '#E9D8A6'),  # NEIGHBOR = 2
    ('#005F73', '#E9D8A6'),  # QUEUED = 3
    ('#0A9396', '#FFFFFF'),  # VISITED = 4
    ('#CA6702', '#FFFFFF'),  # PATH = 5
    ('#9B2226', '#FFFFFF'),  # START = 6
    ('#9B2226', '#FFFFFF'),  # END = 7
]
BKGCOLOR = 'gray35'
PANELCOLOR = 'gray35'
TEXTCOLOR = '#E9D8A6'
FPS = 20
START = (0, 0)
FILE = 'data/grid.txt'
END = (3, 3)
END = (3, 20)

pygame.init()
pygame.display.set_caption('Palgo')
screen = pygame.display.set_mode(SCREENRECT.size)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Menlo', TEXTSIZE)
