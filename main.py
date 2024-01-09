import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH=1920
HEIGHT=1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jaival's Donut")
font = pygame.font.SysFont("SansSerif", 18, bold=True)

run = True
while run:
    screen.fill((black))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


