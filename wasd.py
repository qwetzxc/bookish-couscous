import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Размер окна и блока змейки
window_width, window_height = 800, 600
block_size = 20

# Инициализация окна
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

# Функция отрисовки текста на экране
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

# Функция для отображения сообщений
def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 30)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((window_width / 2), (window_height / 2))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()

# Главное меню
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    intro = False
                elif event.key == pygame.K_2:
                    pygame.quit()
                    quit()

        game_display.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 80)
        text_surf, text_rect = text_objects("Главное меню", large_text)
        text_rect.center = ((window_width / 2), (window_height / 4))
        game_display.blit(text_surf, text_rect)

        font = pygame.font.Font('freesansbold.ttf', 30)
        text_surf, text_rect = text_objects("Играть - 1", font)
        text_rect.center = ((window_width / 2), (window_height / 2))
        game_display.blit(text_surf, text_rect)

        text_surf, text_rect = text_objects("Выйти - 2", font)
        text_rect.center = ((window_width / 2), (window_height / 2 + 100))
        game_display.blit(text_surf, text_rect)

        pygame.display.update()

# Основная функция игры
def game_loop():
    game_exit = False
    game_over = False
    lead_x, lead_y = window_width / 2, window_height / 2
    lead_x_change, lead_y_change = 0, 0

    snake_list = []
    snake_length = 1

    apple_x, apple_y = round(random.randrange(0, window_width - block_size) / block_size) * block_size, round(random.randrange(0, window_height - block_size) / block_size) * block_size

    score = 0

    while not game_exit:

        while game_over:
            game_display.fill(white)
            message_display("Конец игры! Нажмите C - снова играть или Q - выход")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(white)

        # Отрисовка яблока
        pygame.draw.rect(game_display, red, [apple_x, apple_y, block_size, block_size])

        # Отрисовка змейки
        for segment in snake_list:
            pygame.draw.rect(game_display, green, [segment[0], segment[1], block_size, block_size])

        # Обновление позиции змейки
        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)

        # Удаление лишних блоков змейки
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        pygame.display.update()

        # Проверка съедания яблока
        if lead_x == apple_x and lead_y == apple_y:
            apple_x, apple_y = round(random.randrange(0, window_width - block_size) / block_size) * block_size, round(random.randrange(0, window_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 1

        # Отображение счета
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_surf, text_rect = text_objects(f"Счет: {score}", font)
        text_rect.center = (60, 30)
        game_display.blit(text_surf, text_rect)

        clock.tick(10)

    pygame.quit()
    quit()

# Запуск игры
def start_game():
    game_intro()
    game_loop()

start_game()
