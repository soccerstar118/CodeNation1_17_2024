import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    #pygame.draw.
    pygame.draw.circle(screen, 'White', (width/2, height/2), 15)

    pygame.display.flip()
