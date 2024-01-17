import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

paddle_width = 10
paddle_height = 100

paddle_x = width/2
paddle_y = height/2

paddle_speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    #Update paddle position upon key move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_y += paddle_speed
    if keys[pygame.K_s]:
        paddle_y -= paddle_speed

    pygame.draw.rect(screen, 'White', (paddle_x, paddle_y, paddle_width, paddle_height))

    #Wait 1/fps seconds, display update

    clock.tick(60)
    pygame.display.flip()
