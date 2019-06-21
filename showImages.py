import pygame

print("Oi oi")

pygame.init()
(WIDTH, HEIGHT) = (600, 400)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False