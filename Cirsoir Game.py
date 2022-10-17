from pygame import init, display, font, QUIT, key, K_a, K_d, K_w, K_s, draw, event # import pygame
init() # init pygame

from pyautogui import alert, prompt # import pyautogui
from random import randint # import random
from time import time # import time

from os import system
system('cls')
print( f"{'=' * 3} Do not close this window! {'=' * 3}" )


# Make Win
win_size_x = 800 # x size win
win_size_y = 700 # y size win

win = display.set_mode( (win_size_x, win_size_y) ) # make win

    # Make win name
win_name = 'Cirsoir'
display.set_caption(win_name)

    # Input coin task
coin_task = int( prompt( '''Controls: 
[W] - Up
[S] - Down
[A] - Left
[D] - Right

Enter task (coins): ''', win_name ) )


win_font = font.Font(None, 20) # text font


# Player Vars

    # player size
player_widht = 30 # player widht
player_height = 30  # player height

player_x = win_size_x / 2 - player_widht / 2 # x player position
player_y = win_size_y / 2 - player_widht / 2 # y player position

player_speed = 1 # player speed

player_lifes = 10 # player lifes


# Coin Vars

    # coin size
coin_widht = 10 # coin widht
coin_height = 10 # coin height

    # coin position
coin_x = randint(50, win_size_x - 20) # x coin position
coin_y = randint(50, win_size_y - 20) # y coin position

coin_count = 0 # coin counter


# Enemy Vars
    # enemy size
enemy_widht = player_widht - 10 # widht
enemy_height = player_height - 10 # height

    # enemy position
enemy_x = randint( 50, win_size_x - 20 ) # x enemy position
enemy_y = randint( 50, win_size_y - 20 ) # y enemy position


time_start = int( time() ) # Time Counter Var


# ========== WHILE ==========
win_run = True # win var

while win_run: # main while

    win.fill( (108, 162, 108) ) # win color (rgb)


    # Exit From While
    for event_ in event.get():
        if event_.type == QUIT: win_run = False


    # Key Control
    keys = key.get_pressed() # read keys

        # up, down
    if keys[K_w] and player_y > (player_height / 2 - 5): player_y -= player_speed # up
    if keys[K_s] and player_y < (win_size_y - (player_height + 10) ): player_y += player_speed # down

        # left, right
    if keys[K_a] and player_x > (player_widht / 2 - 5): player_x -= player_speed # left
    if keys[K_d] and player_x < (win_size_x - (player_widht + 10) ): player_x += player_speed # right


    # Coin Hitbox
    if(coin_x + player_widht) > player_x > (coin_x - player_widht) and (coin_y + player_height) > player_y > (coin_y - player_height):
        coin_count += 1
        coin_task -= 1
        
        # coin position
        coin_x = randint(50, win_size_x - 20) # x coin position
        coin_y = randint(50, win_size_y - 20) # y coin position
        
        # Enemy position
        enemy_x = randint( 50, win_size_x - 20 ) # x enemy position
        enemy_y = randint( 50, win_size_y - 20 ) # y enemy position


    # Enemy Hitbox
    if (enemy_x + player_widht) > player_x > (enemy_x - player_widht) and (enemy_y + player_height) > player_y > (enemy_y - player_height):
        player_lifes -= 1

        # Enemy position
        enemy_x = randint( 50, win_size_x - 20 ) # x enemy position
        enemy_y = randint( 50, win_size_y - 20 ) # y enemy position   
    
    
    # Draw Elements

        # Draw Player
    draw.rect(win, 
             (0, 255, 0), # player color (rgb)
             (player_x, player_y, player_widht, player_height) # player position and size
             )

        # Draw coin
    draw.rect(win, 
             (255, 255, 0), # coin color (rgb)
             (coin_x, coin_y, coin_widht, coin_height) ) # coin position and size

        # Draw Enemy
    if coin_x != enemy_x and coin_y != enemy_y and player_x != enemy_x and player_y != enemy_y: # if all hitbox not on:
        draw.rect(win, 
                 (255, 0, 0), # enemy color (rgb)
                 (enemy_x, enemy_y, enemy_widht, enemy_height) ) # enemy position and size

    else: # else reset enemy position
        enemy_x = randint( 50, win_size_x - 20 ) # x enemy position
        enemy_y = randint( 50, win_size_y - 20 ) # y enemy position


    # Write Information 
    win_coin_count_text = win_font.render(f'Collected Coins: {coin_count}', # text
                                          True, (255, 255, 0) ) # text color

    win_coin_task_text = win_font.render(f'Coins Task: {coin_task}', # text
                                         True, (255, 0, 0) ) # text color

    time_new = int( time() ) # Read time

    win_tm_text = win_font.render( f'Time: {time_new - time_start} sec,{ int( (time_new - time_start) / 60 ) } min', # text
                                  True, (0, 0, 255) ) # text color

    win_player_lifes_text = win_font.render(f'Lifes: {player_lifes}', # text
                                            True, (0, 255, 0) ) # color
    
    
        # Print Information
    win.blit(win_coin_count_text, (10, 10) )
    win.blit(win_coin_task_text, (10, 30) )
    win.blit(win_tm_text, (10, 50) )
    win.blit(win_player_lifes_text, (10, 70) )


    if coin_task <= 0: # if all coins collected
        tm_end = int( time() ) # time end
        tm_all = tm_end - time_start # calculation time spent by the player in the game

        win_run = False # quit win

        # Отображение информации игроку о его достижениях
        alert( f'''Time: {tm_all} sec   ≈{ int(tm_all / 60) } min
≈ 1 coin per {tm_all / coin_count} sec''',
                  win_name,
                  button = 'Quit')


    if player_lifes <= 0: # If player lose
        # Print player's achievements
        alert(f': {coin_count}',
                  win_name, # win name text
                  button = 'Quit') # button text

        win_run = False # stop win run


    if win_run == True: display.update() # reset display
    else: quit()
