import pygame
from random import randrange


class Circle():
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self):
        if self.y < 280:
            self.y += 10
        else:
            self.y = 290


def draw_text():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render('Поиграем в шарики!', 1, (255, 255, 100))
    text_w = text.get_width()
    text_h = text.get_height()
    text_x = width // 2 - text_w // 2
    text_y = height // 2 - text_h // 2
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


def draw_circle():
    for cir in circle:
        cir.move()
        pygame.draw.circle(screen, cir.color, (cir.x, cir.y), 10)


def new_circle(pos):
    color = pygame.Color(randrange(0, 256), randrange(0, 256), randrange(0, 256))
    circle.append(Circle(color, pos[0], pos[1]))
    pygame.draw.circle(screen, circle[-1].color, (circle[-1].x, circle[-1].y), 10)


def draw_circle_1000():
    global circle
    circle2 = []
    for cir in circle:
        if cir.y == 290:
            pygame.draw.circle(screen, cir.color, (cir.x, cir.y), 10)
        else:
            circle2.append(cir)
    circle = circle2[:]


pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen2 = pygame.Surface(screen.get_size())
circle = []
speed = []
circle_color = []
running = True

draw_text()
pygame.display.flip()
running = 0
while running == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 2
        if event.type == pygame.MOUSEBUTTONUP:
            running = 1
screen.fill(pygame.Color('black'))
if running == 1:
    running = True
else:
    running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            new_circle(event.pos)
    if len(circle) > 100:
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        draw_circle_1000()
        screen2.blit(screen, (0, 0))
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    clock.tick(10)
    draw_circle()
    pygame.display.flip()






pygame.quit()