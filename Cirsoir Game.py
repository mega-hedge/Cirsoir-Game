import pygame as pg # подключение pygame и сокращение до "pg"
import pyautogui as pag # подключение PyAutoGui и сокращение до "pag"
import random as rnd # подключение random и сокращение до "rnd"
import time as tm # подключение time и сокращение до "tm"

pg.init() # инициализация pygame


# СТАРТОВЫЙ ЭКРАН
game_name = "Cirsoir"

m_task = int( pag.prompt("Управление: \n[W] - вверх \n[A] - влево \n[S] - вниз\n[D] - вправо \n\nВведите цель (кол-во монет):", game_name) )


# ПЕРЕМЕННЫЕ (параметры) ОКНА
win_x = 800
win_y = 700

win = pg.display.set_mode( (win_x, win_y) ) # создание окна
pg.display.set_caption(game_name) # определение заголовка окна


# ПЕРЕМЕННЫЕ (параметры) ТЕКСТА
win_font = pg.font.Font(None, 20) # шрифт для текста на экране


# ПЕРЕМЕННЫЕ (параметры) ИГРОКА
# размеры
pl_widht = 30 # ширина
pl_height = 30  # длина

pl_x = win_x / 2 - pl_widht / 2 # положение по х
pl_y = win_y / 2 - pl_widht / 2 # положение по у

pl_speed = 16 # скорость

pl_hp = 10


# ПЕРЕМЕННЫЕ (параметры) МОНЕТ
# размеры
m_widht = 10 # ширина
m_height = 10 # длина

# положение
m_x = rnd.randint(50, win_x - 20) # положение по х
m_y = rnd.randint(50, win_y - 20) # положение по у

m_count = 0 # счётчик общего кол-ва монет у игрока


# ПЕРЕМЕННЫЕ (параметры) ВРАГОВ
# размеры
v_widht = pl_widht - 10 # ширина
v_height = pl_height - 10 # длина

# положение
v_x = rnd.randint(50, win_x - 20) # положение по х
v_y = rnd.randint(50, win_y - 20) # положение по у

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
    if keys[pg.K_a] and pl_x > (pl_widht / 2 - 5) or keys[pg.K_LEFT] and pl_x > (pl_widht / 2 - 5): # left
        pl_x -= pl_speed

    if keys[pg.K_d] and pl_x < (win_x - (pl_widht + 10) ) or keys[pg.K_RIGHT] and pl_x < (win_x - (pl_widht + 10) ): # right
        pl_x += pl_speed

    # up, down
    if keys[pg.K_w] and pl_y > (pl_height / 2 - 5) or keys[pg.K_UP] and pl_y > (pl_height / 2 - 5): # up
        pl_y -= pl_speed

    if keys[pg.K_s] and pl_y < (win_y - (pl_height + 10) ) or keys[pg.K_DOWN] and pl_y < (win_y - (pl_height + 10) ): # down
        pl_y += pl_speed



    # СБОР МОНЕТ
    if(m_x + pl_widht) > pl_x > (m_x - pl_widht) and (m_y + pl_height) > pl_y > (m_y - pl_height):
        m_count += 1
        m_task -= 1
        
        # положение монеты
        m_x = rnd.randint(50, win_x - 20) # положение по х
        m_y = rnd.randint(50, win_y - 20) # положение по у
        
        # положение врага
        v_x = rnd.randint(50, win_x - 20) # положение по х
        v_y = rnd.randint(50, win_y - 20) # положение по у

    # СТОЛКНОВЕНИЕ С ВРАГАМИ
    if (v_x + pl_widht) > pl_x > (v_x - pl_widht) and (v_y + pl_height) > pl_y > (v_y - pl_height):
        pl_hp -= 1

        # положение врага
        v_x = rnd.randint(50, win_x - 20) # положение по х
        v_y = rnd.randint(50, win_y - 20) # положение по у       
    
    
    pg.draw.rect(win, (0, 255, 0), (pl_x, pl_y, pl_widht, pl_height) ) # отрисовка квадрата игрока, цвет = зелёный
    pg.draw.rect(win, (255, 255, 0), (m_x, m_y, m_widht, m_height) ) # отрисовка монеты, цвет = жёлтый
    if m_x != v_x and m_y != v_y and pl_x != v_x and pl_y != v_y:
        pg.draw.rect(win, (255, 0, 0), (v_x, v_y, v_widht, v_height) ) # отрисовка врага, цвет = красный
    else:
        # положение
        v_x = rnd.randint(50, win_x - 20) # положение по х
        v_y = rnd.randint(50, win_y - 20) # положение по у


    # Вывод информации
    win_m_count_text = win_font.render(f"Собрано монет: {m_count}", True, (255, 255, 0) )
    win_m_task_text = win_font.render(f"Осталось собрать монет: {m_task}", True, (255, 0, 0) )

    tm_new = int( tm.time() )
    win_tm_text = win_font.render(f"Прошло {tm_new - tm_start} сек ({ int( (tm_new - tm_start) / 60 ) } мин)",
                                  True,
                                  (0, 0, 255)
                                  )
    win_pl_hp_text = win_font.render(f"Осталось жизней: {pl_hp}", True, (0, 255, 0) )
    
    
    win.blit(win_m_count_text, (10, 10) )
    win.blit(win_m_task_text, (10, 30) )
    win.blit(win_tm_text, (10, 50) )
    win.blit(win_pl_hp_text, (10, 70) )


    if m_task <= 0:
        tm_end = int( tm.time() )  # конец отсчёта времени собирания всех монет игроком
        tm_all = tm_end - tm_start # расчёт проведённого времени игроком в игре

        run_win = False

        # Отображение информации игроку о его достижениях
        pag.alert(f"""Вы собрали {m_count} монет за {tm_all} сек (~{ int(tm_all / 60) } мин)!
(~1 монета за {tm_all / m_count} сек)""",
                  game_name,
                  button = "Выйти из игры")


    if pl_hp <= 0:
        # Отображение информации игроку о его достижениях
        pag.alert(f"Вы проиграли собрав монет: {m_count}",
                  game_name,
                  button = "Выйти из игры")

        run_win = False


    if run_win == True:
        pg.display.update() # обновление дисплея
    else:
        pg.quit()
