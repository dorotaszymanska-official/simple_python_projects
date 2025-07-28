import random
import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

RANGE_X = 1200
RANGE_Y = 700

FOOD_SIZE = 8

snake_x = 400.0
snake_y = 400.0

snake_width = 8
snake_height = 8

change_x = 0
change_y = 0

running = True

food_x = random.randint(1, RANGE_X - FOOD_SIZE)
food_y = random.randint(1, RANGE_Y - FOOD_SIZE)

pygame.init()

snake_list = []
snake_length = 1

screen = pygame.display.set_mode((RANGE_X, RANGE_Y))
pygame.display.set_caption("Snake")

while running:

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if snake_y <= 0:
        snake_y = 0
        change_y = RANGE_Y - snake_height
    if snake_y >= RANGE_Y - snake_height:
        snake_y = 0
        change_y = 0
    if snake_x <= 0:
        snake_x = RANGE_X - snake_width
        change_x = 0
    if snake_x >= RANGE_X - snake_width:
        snake_x = 0
        change_x = 0

    if keys[pygame.K_UP]:
        change_x = 0
        change_y = -0.4
    elif keys[pygame.K_DOWN]:
        change_x = 0
        change_y = 0.4
    elif keys[pygame.K_LEFT]:
        change_x = -0.4
        change_y = 0
    elif keys[pygame.K_RIGHT]:
        change_x = 0.4
        change_y = 0

    head = []
    head.append(snake_x)
    head.append(snake_y)

    for segment in snake_list[:-1]:
        if (
            (keys[pygame.K_UP] and keys[pygame.K_DOWN])
            or (keys[pygame.K_LEFT] and keys[pygame.K_RIGHT])
            and (segment == head)
        ):
            change_x = 0.25
            change_y = 0.25
            # pass
        else:
            if segment == head:
                running = False

    pygame.draw.rect(screen, WHITE, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

    snake_list.append(head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    snake_x += change_x
    snake_y += change_y

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
        snake_length += 50

pygame.quit()
