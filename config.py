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
    ('#9B2226', '#E9D8A6'),  # CURRENT = 1
    ('#E9C46A', '#E9D8A6'),  # NEIGHBOR = 2
    ('#005F73', '#E9D8A6'),  # QUEUED = 3
    ('#0A9396', '#FFFFFF'),  # VISITED = 4
    ('#CA6702', '#FFFFFF'),  # PATH = 5
    ('#CA6702', '#FFFFFF'),  # START = 6
    ('#CA6702', '#FFFFFF'),  # END = 7
]
BKGCOLOR = 'gray35'
PANELCOLOR = 'gray35'
TEXTCOLOR = '#E9D8A6'
FILE = 'data/grid.txt'
FPS = 10
START = (0, 0)
END = (3, 3)
END = (26, 33)

pygame.init()
pygame.display.set_caption('Palgo')
screen = pygame.display.set_mode(SCREENRECT.size)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Menlo', TEXTSIZE)
