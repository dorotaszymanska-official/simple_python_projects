import random
import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

RANGE_X = 1200
RANGE_Y = 700

FOOD_SIZE = 20
BLOCK_SIZE = 20

snake_x = 400.0
snake_y = 400.0

snake_width = 20
snake_height = 20

change_x = 0
change_y = 0

running = True

food_x = random.randint(1, RANGE_X - FOOD_SIZE)
food_y = random.randint(1, RANGE_Y - FOOD_SIZE)

clock = pygame.time.Clock()

direction = "right"

pygame.init()

snake_list = []
snake_length = 1

screen = pygame.display.set_mode((RANGE_X, RANGE_Y))
pygame.display.set_caption("Snake")

while running:
    clock.tick(60)
    screen.fill(BLACK)

    for x in range(0, RANGE_X, BLOCK_SIZE):
        for y in range(0, RANGE_Y, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_UP] and direction != "down":
        direction = "up"
        change_x = 0
        change_y = -BLOCK_SIZE / 5
    elif keys[pygame.K_DOWN] and direction != "up":
        direction = "down"
        change_x = 0
        change_y = BLOCK_SIZE / 5
    elif keys[pygame.K_LEFT] and direction != "right":
        direction = "left"
        change_x = -BLOCK_SIZE / 5
        change_y = 0
    elif keys[pygame.K_RIGHT] and direction != "left":
        direction = "right"
        change_x = BLOCK_SIZE / 5
        change_y = 0

    if snake_y <= 0 or snake_y >= RANGE_Y - snake_height:
        change_y *= -1
    if snake_x <= 0 or snake_x >= RANGE_X - snake_width:
        change_x *= -1

    snake_x += change_x
    snake_y += change_y

    head = []
    head.append(snake_x)
    head.append(snake_y)

    pygame.draw.rect(screen, WHITE, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

    snake_list.append(head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    if len(snake_list) > 2 and snake_list[0] == snake_list[-1]:
        FONT = pygame.font.Font(None, 36)
        END_MESSAGE = FONT.render("Przegrana", True, RED)
        screen.blit(END_MESSAGE, END_MESSAGE.get_rect())
        running = False

    for segment in snake_list:
        pygame.draw.rect(
            screen, RED, (segment[0], segment[1], snake_width, snake_height)
        )
    pygame.display.update()

    snake_rect = pygame.Rect(snake_x, snake_y, snake_width, snake_height)
    food_rect = pygame.Rect(food_x, food_y, FOOD_SIZE, FOOD_SIZE)

    if snake_rect.colliderect(food_rect):
        food_x = random.randint(1, RANGE_X)
        food_y = random.randint(1, RANGE_Y)
        snake_length += 20

pygame.quit()
