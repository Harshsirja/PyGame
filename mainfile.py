import pygame

# Creating Window
x = pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First game")

# Game Specific Window
exit_game = False
game_over = False

# Creating game loop
while exit_game!=True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("Right Arrow Key")

pygame.quit()
quit()