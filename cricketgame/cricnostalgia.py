# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# screen_width = 800
# screen_height = 600

# # Colors
# white = (255, 255, 255)
# green = (0, 128, 0)
# black = (0, 0, 0)
# red = (255, 0, 0)

# # Create the display
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Nostalgic Button Phone Cricket Game')

# # Clock for controlling the frame rate
# clock = pygame.time.Clock()

# # Batsman properties
# batsman_width = 60
# batsman_height = 120
# batsman_x = screen_width // 2
# batsman_y = screen_height - batsman_height - 10
# batsman_speed = 10

# # Ball properties
# ball_width = 10
# ball_height = 10
# ball_x = random.randint(0, screen_width - ball_width)
# ball_y = 0
# ball_speed = 5

# # Score
# score = 0

# # Font for displaying score
# font = pygame.font.SysFont("comicsansms", 35)

# def show_score(score):
#     value = font.render("Score: " + str(score), True, black)
#     screen.blit(value, [0, 0])

# def game_over():
#     over_text = font.render("Game Over", True, red)
#     screen.blit(over_text, [screen_width // 2 - 100, screen_height // 2])
#     pygame.display.update()
#     pygame.time.wait(2000)
#     pygame.quit()
#     quit()

# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Key press handling
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and batsman_x > 0:
#         batsman_x -= batsman_speed
#     if keys[pygame.K_RIGHT] and batsman_x < screen_width - batsman_width:
#         batsman_x += batsman_speed

#     # Ball movement
#     ball_y += ball_speed
#     if ball_y > screen_height:
#         ball_y = 0
#         ball_x = random.randint(0, screen_width - ball_width)
#         ball_speed += 0.5  # Increase ball speed as game progresses

#     # Collision detection
#     if (batsman_y < ball_y + ball_height < batsman_y + batsman_height) and \
#        (batsman_x < ball_x + ball_width < batsman_x + batsman_width):
#         score += 1
#         ball_y = 0
#         ball_x = random.randint(0, screen_width - ball_width)
        
#     # Fill the screen with white
#     screen.fill(green)
    
#     # Draw the batsman
#     pygame.draw.rect(screen, black, [batsman_x, batsman_y, batsman_width, batsman_height])
    
#     # Draw the ball
#     pygame.draw.rect(screen, red, [ball_x, ball_y, ball_width, ball_height])
    
#     # Display the score
#     show_score(score)
    
#     # Check for game over
#     if ball_y + ball_height >= screen_height:
#         game_over()
    
#     # Update the display
#     pygame.display.update()
    
#     # Control the frame rate
#     clock.tick(30)

# # Quit the game
# pygame.quit()
