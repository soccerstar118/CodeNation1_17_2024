import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

paddle_width = 10
paddle_height = 100

paddle1 = pygame.rect.Rect(0, height/2, paddle_width, paddle_height)
paddle2 = pygame.rect.Rect(width-paddle_width, height/2, paddle_width, paddle_height)

paddle_speed = 10

ball_x = width/2
ball_y = height/2

ball_vel_x = 5
ball_vel_y = 2

ball_radius = 10

score_1 = 0
score_2 = 0
score_required_to_win = 2

game_over = False

font = pygame.font.SysFont("arial", 70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if not game_over:
        screen.fill("Black")

        #Move ball
        ball_x += ball_vel_x
        ball_y += ball_vel_y

        #Draw ball
        pygame.draw.circle(screen, "White", (ball_x, ball_y), ball_radius)

        #Collide with paddles
        if ball_x - ball_radius <= paddle1.right and paddle1.top <= ball_y <= paddle1.bottom:
            ball_vel_x *= -1
        if ball_x + ball_radius >= paddle2.left and paddle2.top <= ball_y <= paddle2.bottom:
            ball_vel_x *= -1

        #Collide with screen border (top & bottom)
        if ball_y - ball_radius <= 0:
            ball_vel_y *= -1
        if ball_y + ball_radius >= height:
            ball_vel_y *= -1


        # Check score adding conditions
        if ball_x + ball_radius <= 0:
            score_2 += 1
            ball_x = width / 2
            ball_y = height / 2
            ball_vel_x *= -1
        if ball_x - ball_radius >= width:
            score_1 += 1
            ball_x = width / 2
            ball_y = height / 2
            ball_vel_x *= -1


        #Draw scores
        text_surface = font.render(str(score_1), True, 'White')
        text_rect = text_surface.get_rect(center=(width/2-30, 30))
        screen.blit(text_surface, text_rect)

        text_surface = font.render(str(score_2), True, 'White')
        text_rect = text_surface.get_rect(center=(width/2+30, 30))
        screen.blit(text_surface, text_rect)

        if score_1 >= score_required_to_win or score_2 >= score_required_to_win:
            if score_1 >= score_required_to_win:
                display_text = "Player 1 wins!"
            else:
                display_text = "Player 2 wins!"

            text_surface = font.render(display_text, True, 'Blue')
            text_rect = text_surface.get_rect(center=(width / 2, 300))
            screen.blit(text_surface, text_rect)

            #pygame.display.flip()
            game_over = True


        #Draw midline
        pygame.draw.line(screen, 'White', (width/2, height), (width/2, 0))

        #Update paddle1 position upon key move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.y -= paddle_speed
        if keys[pygame.K_s]:
            paddle1.y += paddle_speed

        #Update paddle2 position upon key move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle2.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            paddle2.y += paddle_speed

        pygame.draw.rect(screen, 'White', paddle1)
        pygame.draw.rect(screen, 'White', paddle2)

        #Wait 1/fps seconds, display update

        clock.tick(60)
        pygame.display.flip()
