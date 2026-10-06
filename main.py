import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("My Game!")

player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))
player = pygame.image.load("sprite_sheet.png").convert_alpha()
player = pygame.transform.scale(player, (300, 300))

player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

falling_object = pygame.surface.Surface((50, 50))
falling_object.fill((255, 255, 255))


falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_vel_x = -0.2
            if event.key == pygame.K_d:
                player_vel_x = 0.2
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2
            else:
                player_vel_x = 0
                player_vel_y = 0
        if event.type == pygame.QUIT:
            quit(0)


window.fill((0, 0, 0))
window.blit(player, (player_x, player_y))
window.blit(falling_object, (falling_object_x, falling_object_y))
player_x += player_vel_x
player_y += player_vel_y
falling_object_x += falling_object_vel_x
falling_object_y += falling_object_vel_y
falling_object_vel_y += 0.01  # Simulate gravity for the falling object
if falling_object_y > 600:  # Simulate collision with the ground
    falling_object_y = 600
    falling_object_vel_y = 0
if player_y > 600:  # Simulate collision with the ground for the player
    player_y = 600
    player_vel_y = 0
window.blit(player, (player_x, player_y))


pygame.display.flip()

 
 