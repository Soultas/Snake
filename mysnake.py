import pygame
import random
import time
import pickle

pygame.init()

#Colors
black = (0,0,0)
red = (255,0,0)
teal = (50,153,213)
yellow = (255,255,102)
#Dimensions
dis_width = 800
dis_height = 800
#Display definition
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake by Ryan Gonzales')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift",30)
score_font = pygame.font.SysFont("comicsansms",35)

high_score = 0
test_score = [0]

snake_block = 10
snake_speed = 15




    


def protagosnake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,red, [x[0],x[1], snake_block,snake_block])

def current_score(score):
    value = score_font.render("Your Score: "+str(score),True,yellow)
    dis.blit(value, [0,0])

def announcement(msg,color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg, [dis_width/6,dis_height/3])

def init_snek():
    #Defined for while loop to keep game continous
    game_over = False
    game_close = False
    #Definition of dimensions and range of movement
    x_plane = dis_width / 2
    y_plane = dis_height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1
    #Places food randomly in display
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:


        while game_close == True:
            dis.fill(black)
            announcement("You Lost, Press Q-Quit or C-Play Again",red)




                
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        init_snek()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = - snake_block
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = - snake_block
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if x_plane >=dis_width or x_plane < 0 or y_plane >= dis_height or y_plane <0:
            game_close = True

        x_plane += x_change
        y_plane += y_change
        dis.fill(black)
        pygame.draw.rect(dis,teal, [food_x,food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x_plane)
        snake_head.append(y_plane)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        protagosnake(snake_block, snake_list)
        current_score(snake_length -1)



        pygame.display.update()

        if x_plane == food_x and y_plane == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            snake_length +=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


init_snek()