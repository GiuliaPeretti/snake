import pygame
from settings import *
import random

#Livello 1 -> 56
#Livello 2 -> 40
#Livello 3 -> 20

def draw_backgound():
    screen.fill(BACKGROUND_COLOR)
    for i in range(20, SQUARE_SIZE+20+1, square_width):
        pygame.draw.line(screen, WHITE, (i,20), (i,SQUARE_SIZE+20), 1)
    for i in range(20, SQUARE_SIZE+20+1, square_width):
        pygame.draw.line(screen, WHITE, (20,i), (SQUARE_SIZE+20,i), 1)

def gen_grid():
    status_grid=[]
    for i in range(560//square_width):
        temp=[]
        for j in range(560//square_width):
            temp.append(0)
        status_grid.append(temp)
    return(status_grid)



def gen_buttons():
    x,y,w,h=640,20,100,30
    buttons=[]
    for i in range (1,4):
        buttons.append({'name': 'Level '+str(i), 'coordinates': (x,y,w,h)})
        y=y+h+10
    # buttons.append({'name': 'Play', 'coordinates': (x,y,w,h)})

    return(buttons)

def draw_buttons():
    for b in buttons[:len(buttons)]:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+17,b['coordinates'][1]+3))
    
    if selected!=-1:
        pygame.draw.rect(screen, PINK, buttons[selected]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
        text=font.render(buttons[selected]['name'], True, BLACK)
        screen.blit(text, (buttons[selected]['coordinates'][0]+17,buttons[selected]['coordinates'][1]+3))

    # pygame.draw.rect(screen, GRAY, buttons[-1]['coordinates'])
    # pygame.draw.rect(screen, BLACK,  buttons[-1]['coordinates'], 3)
    # text=font.render( buttons[-1]['name'], True, BLACK)
    # screen.blit(text, ( buttons[-1]['coordinates'][0]+30, buttons[-1]['coordinates'][1]+3))

def get_square_width(i):
    match i:
        case 0:
            return 56
        case 1: 
            return 40
        case 2:
            return 20

def draw_snake():
    print(snake_pos)
    for i in range (len(snake_pos)):
        x=snake_pos[i][1]*square_width+20+4
        y=snake_pos[i][0]*square_width+20+4
        pygame.draw.rect(screen, RED, (x, y, square_width-8, square_width-8))
        status_grid[snake_pos[i][0]][snake_pos[i][1]]=1

def move():
    match direction:
        case 0:
            snake_pos.append( (snake_pos[-1][0]-1, snake_pos[-1][1]) )
            snake_pos.pop(0)
        case 1:
            snake_pos.append( (snake_pos[-1][0], snake_pos[-1][1]+1) )
            snake_pos.pop(0)
        case 2:
            snake_pos.append( (snake_pos[-1][0]+1, snake_pos[-1][1]) )
            snake_pos.pop(0)
        case 3:
            snake_pos.append( (snake_pos[-1][0], snake_pos[-1][1]-1) )
            snake_pos.pop(0)
    draw_snake()

def new_food():
    
    row=random.randint(0,560//square_width-1)
    col=random.randint(0,560//square_width-1)






if __name__ == '__main__':
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Snake♥')
    font = pygame.font.SysFont('arial', 20)


    selected=-1
    select_game=-1
    square_width=56
    direction=3
    snake_pos=[(0,2),(0,3)]
    status_grid=gen_grid()

    draw_backgound()
    buttons=gen_buttons()
    draw_buttons()
    draw_snake()
    # print(status_grid)






    run  = True
    selected_cell=(-1,-1)
    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                for i in range (len(buttons)):
                    if(x>=buttons[i]['coordinates'][0] and x<=buttons[i]['coordinates'][0]+buttons[i]['coordinates'][2] and y>=buttons[i]['coordinates'][1] and y<=buttons[i]['coordinates'][1]+buttons[i]['coordinates'][3]):
                        if(i<len(buttons)):
                            selected=i
                            print("Cella selezionate: "+str(selected))
                            square_width=get_square_width(i)
                            draw_backgound()
                            draw_buttons()
                            break
                else:
                    selected=-1
                draw_buttons()
            if (event.type == pygame.KEYDOWN):
                # up->0, right->1, down->2 left->3
                if(event.key == pygame.K_UP):
                    direction=0
                    move()
                elif(event.key == pygame.K_RIGHT):
                    direction=1
                    move()
                elif(event.key == pygame.K_DOWN):
                    direction=2
                    move()
                elif(event.key == pygame.K_LEFT):
                    direction=3
                    move()
        

        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()