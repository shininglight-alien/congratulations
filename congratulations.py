# congratulations

import pygame
import sys
import random

# adding pygame
pygame.init()

# sizes and colors
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 72
FONT = pygame.font.SysFont(None, FONT_SIZE)
BALLOON_COLORS = [(255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (139, 0, 139)]
BALLOON_SIZES = [50, 75, 100]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Congratulations!")

def draw_balloon(x, y, size, color):
    pygame.draw.ellipse(screen, color, (x, y, size, size))
    pygame.draw.polygon(screen, color, ((x, y), (x + size // 2, y - size // 2), (x + size, y)))

def draw_text(text, x, y):
    text_surface = FONT.render(text, True, FONT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
    
running = True
clock = pygame.time.Clock()
balloons = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balloons.append({
                'x': random.randint(0, WIDTH),
                'y': random.randint(0, HEIGHT),
                'size': random.choice(BALLOON_SIZES),
                'color': random.choice(BALLOON_COLORS),
                'speed': (random.randint(-5, 5) / 10, random.randint(-5, 5) / 10)
            })
            
screen.fill(BACKGROUND_COLOR)
draw_text("Congratulations!", WIDTH // 2, HEIGHT // 2 - 50)
for balloon in balloons:
        balloon['x'] += balloon['speed'][0]
        balloon['y'] += balloon['speed'][1]
        if balloon['x'] < 0 or balloon['x'] + balloon['size'] > WIDTH:
            balloon['speed'][0] = -balloon['speed'][0]
        if balloon['y'] < 0 or balloon['y'] + balloon['size'] > HEIGHT:
            balloon['speed'][1] = -balloon['speed'][1]
        draw_balloon(balloon['x'], balloon['y'], balloon['size'], balloon['color'])

pygame.display.flip()
clock.tick(30)

if random.randint(0, 200) == 0:
        balloons.append({
            'x': random.randint(0, WIDTH),
            'y': random.randint(0, HEIGHT),
            'size': random.choice(BALLOON_SIZES),
            'color': random.choice(BALLOON_COLORS),
            'speed': (random.randint(-5, 5) / 10, random.randint(-5, 5) / 10)
        })

# quitting pygame
pygame.quit()
sys.exit()