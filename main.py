import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("First game")

# COLORS
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60

score = 0

class Block:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
    
    def draw(self):
        # WIN is the surface
        # self.color is the RGB value for the color
        # third argument contains type with x, y, width and height
        return pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
    # rect object
    # colliderect // Check if colliding with different object

    def move(self):
        keys = pygame.key.get_pressed() #get list of all the keys available for pygame

        if keys[pygame.K_RIGHT]: #check if right arrow is pressed
            self.x += self.speed # increase by the speed of the player block
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
        
        if self.x < 0: # if x position is 0, stop player from going outside
            self.x = 0
        elif self.x > WIDTH - self.width: # if x is greater than the width of the surface, set x to screen minus width of player
            self.x = WIDTH - self.width


def draw_score():

    font = pygame.font.SysFont("comicsans", 20) # set font
    text = font.render(f'Score: {score}', True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (text_rect.width, 10)

    WIN.blit(text, text_rect)


def main():
    global score # set score to global variable so that the changes made to the variable in this function affect the rest of the code where the variable is used
    game_running = True

    player_height = 40
    player_width = 40
    player_x = (WIDTH // 2) - (player_width // 2)
    player_y = (HEIGHT // 2) - (player_height // 2)
    player_speed = 15

    enemy_height = 50
    enemy_width = 50
    enemy_x = random.randint(0, WIDTH-enemy_width)
    enemy_y = 0
    enemy_speed = 10

    player = Block(player_x, player_y, player_width, player_height, player_speed, GREEN)
    enemy = Block(enemy_x, enemy_y, enemy_width, enemy_height, enemy_speed, RED)

    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
                break
        WIN.fill(BLACK)
        drawn_player = player.draw()
        drawn_enemy = enemy.draw()

        enemy.y += enemy_speed

        if enemy.y >= HEIGHT: # if enemy hits the ground, the player has successfully dodged the enemy
            score += 10
            enemy.x = random.randint(0, WIDTH-enemy_width)
            enemy.y = 0

        if drawn_player.colliderect(drawn_enemy):
            pygame.quit()
        
        draw_score()
        player.move() # listen for keystrokes
        pygame.display.update()
main()