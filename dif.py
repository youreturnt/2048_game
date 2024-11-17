import pygame
import sys

arr1 = [
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 4, 0, 0],
    [0, 0, 0, 0]
]

colors = {
    'background': (90, 90, 90),
    'empty_button': (130, 130, 120),
    'full_button': (0, 0, 0)
}

pygame.init()
screen = pygame.display.set_mode((400, 500))
screen.fill(colors['background'])

y = 30
vert = 0
for j in range(4):
    x = 30
    gor = 0
    for i in range(4):
        font = pygame.font.SysFont('couriernew', 60)
        text = font.render(str(arr1[vert][gor]), True, colors['full_button'])
        screen.blit(text, (x, y))
        x += 90
        gor += 1
    y += 60
    vert += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()