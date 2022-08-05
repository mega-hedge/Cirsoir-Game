import pygame as pg # подключение pygame и сокращение до "pg"
import pyautogui as pag # подключение PyAutoGui и сокращение до "pag"
import random as rnd # подключение random и сокращение до "rnd"
import time as tm # подключение time и сокращение до "tm"


pg.init() # инициализация pygame


print("\nНЕ ЗАКРЫВАЙТЕ ЭТО ОКНО!\n") # вывод информации для игрока


# СТАРТОВЫЙ ЭКРАН
game_name = "Cirsoir"

m_task = int( pag.prompt("Управление: \n[↑] - вверх \n[←] - влево \n[→] - вправо \n[↓] - вниз \n\nВведите цель (кол-во монет):", game_name) )


# ПЕРЕМЕННЫЕ (параметры) ОКНА
win_x = 1000
win_y = 700

win = pg.display.set_mode( (win_x, win_y) ) # создание окна
pg.display.set_caption(game_name) # определение заголовка окна


# ПЕРЕМЕННЫЕ (параметры) ИГРОКА
# размеры
pl_widht = 30 # ширина
pl_height = 30  # длина

pl_x = win_x / 2 - pl_widht / 2 # положение по х
pl_y = win_y / 2 - pl_widht / 2 # положение по у

pl_speed = 9 # скорость


# ПЕРЕМЕННЫЕ (параметры) МОНЕТ
# размеры
m_widht = 10 # ширина
m_height = 10  # длина
# положение
m_x = rnd.randint(30, win_x - 20) # положение по х
m_y = rnd.randint(30, win_y - 20) # положение по у

m_count = 0 # счётчик общего кол-ва монет у игрока


# ПЕРЕМЕННЫЕ (параметры) ТЕКСТА
win_font = pg.font.Font(None, 20)


tm_start = int( tm.time() ) # начало отсчёта времени собирания всех монет игроком


# ========== ЦИКЛ WHILE ==========
run_win = True # переменная состояния цикла while
while run_win:

    win.fill( (108, 162, 108) ) # цвет окна "(red, green, blue)". (задан чёрный цвет) Очищает экран при каждом проходе цикла
    pg.time.delay(16) # задержка между повторениями цикла while в мс.


    # обработка выхода их цикла while
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_win = False


    # ПРОВЕРКА НАЖАТЫХ КЛАВИШ с проверкой границ окна
    keys = pg.key.get_pressed()

    # left, right
    if keys[ pg.K_LEFT ] and pl_x > (pl_widht / 2 - 5): # left
        pl_x -= pl_speed

    if keys[ pg.K_RIGHT ] and pl_x < (win_x - (pl_widht + 10) ): # right
        pl_x += pl_speed

    # up, down
    if keys[ pg.K_UP ] and pl_y > (pl_height / 2 - 5): # up
        pl_y -= pl_speed

    if keys[ pg.K_DOWN ] and pl_y < (win_y - (pl_height + 10) ): # down
        pl_y += pl_speed



    # СБОР МОНЕТ
    if (m_x + pl_widht) > pl_x > (m_x - pl_widht) and (m_y + pl_height) > pl_y > (m_y - pl_height):
        m_count += 1
        m_task -= 1
        
        
        # положение
        m_x = rnd.randint(20, win_x - 20) # положение по х
        m_y = rnd.randint(20, win_y - 20) # положение по у
    
    
    pg.draw.rect(win, (0, 255, 0), (pl_x, pl_y, pl_widht, pl_height) ) # отрисовка квадрата игрока, цвет = зелёный
    pg.draw.rect(win, (255, 255, 0), (m_x, m_y, m_widht, m_height) ) # отрисовка монеты, цвет = жёлтый


    # Вывод информации о монетах
    win_m_count_text = win_font.render(f"Кол-во монет: {m_count}", False, (255, 255, 0) )
    win_m_task_text = win_font.render(f"Осталось собрать монет: {m_task}", True, (255, 0, 0) )
    
    win.blit(win_m_count_text, (10, 10) )
    win.blit(win_m_task_text, (10, 30) )
    

    if m_task <= 0:
        win_run = False
        pg.quit()
        
        tm_end = int( tm.time() )  # конец отсчёта времени собирания всех монет игроком
        tm_all = int( tm_end - tm_start ) # расчёт проведённого времени игроком в игре

        # Отображение информации игроку о его достижениях
        print("=" * 10, "Вы собрали все монеты за", tm_all, "сек!", "=" * 10)
        pag.alert(f"Вы собрали все монеты за {tm_all} сек!", game_name, button = "Выйти из игры")

    pg.display.update() # обновление дисплея


pg.quit()
