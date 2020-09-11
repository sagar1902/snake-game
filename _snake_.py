

import pygame, sys, time, random

xsize=900
ysize=1440

check=pygame.init()
if  check[1]>0:
	print('error')
	sys.exit()
else:
	print('success')


pygame.display.set_caption('CLASSIC SNAKE GAME')
window=pygame.display.set_mode((xsize+150,ysize))
'''
font = pygame.font.SysFont('consolas', 30)
final_score_font=pygame.font.SysFont('consolas',50)
over_font = pygame.font.SysFont('consolas', 90)
over_comment_font = pygame.font.SysFont('consolas', 40)
'''
snake_pos=[100,50]
snake_body =[ [100, 50], [100-10, 50], [100-(2*10), 50]]

direction='RIGHT'
change_direction=direction

difficulty=25
fps=pygame.time.Clock()

food_pos = [random.randrange(1, (xsize//10)) * 10, random.randrange(1, (ysize//10)) * 10]
food_spawn = True

score=0

level_completion=0
level=1

'''retry=False	'''

def display_text(font,size,text_str,color,display_pos_x,display_pos_y):
	display_font=pygame.font.SysFont(font,size)
	surface = display_font.render(text_str, True, color)
	rect = surface.get_rect()
	rect.midtop = (display_pos_x, display_pos_y)
	window.blit(surface, rect)    


def start_window():
	window.fill((220,220,220))
	
	display_text('consolas',80,'CLASSIC SNAKE GAME',(0,0,0),xsize/2,ysize/4)
	display_text('consolas',50,'Loading game .',(0,0,0),xsize/2,ysize/4+200)
	display_text('consolas',50,'Instruction',(0,0,0),xsize/2,ysize/4+350)
	display_text('consolas',40,'collect as many objects as possible',(0,0,0),xsize/2,ysize/4+430)
	display_text('consolas',40,'without hitting the wall',(0,0,0),xsize/2,ysize/4+470)
	pygame.display.update()
	time.sleep(1)
	
	window.fill((220,220,220))
	display_text('consolas',80,'CLASSIC SNAKE GAME',(0,0,0),xsize/2,ysize/4)
	display_text('consolas',50,'Loading game . .',(0,0,0),xsize/2,ysize/4+200)
	display_text('consolas',50,'Instruction',(0,0,0),xsize/2,ysize/4+350)
	display_text('consolas',40,'collect as many objects as possible',(0,0,0),xsize/2,ysize/4+430)
	display_text('consolas',40,'without hitting the wall',(0,0,0),xsize/2,ysize/4+470)
	pygame.display.update()
	time.sleep(1)
	
	window.fill((220,220,220))
	display_text('consolas',80,'CLASSIC SNAKE GAME',(0,0,0),xsize/2,ysize/4)
	display_text('consolas',50,'Loading game . . .',(0,0,0),xsize/2,ysize/4+200)
	display_text('consolas',50,'Instruction',(0,0,0),xsize/2,ysize/4+350)
	display_text('consolas',40,'collect as many objects as possible',(0,0,0),xsize/2,ysize/4+430)
	display_text('consolas',40,'without hitting the wall',(0,0,0),xsize/2,ysize/4+470)
	pygame.display.update()
	time.sleep(1)
	
	window.fill((220,220,220))
	display_text('consolas',80,'CLASSIC SNAKE GAME',(0,0,0),xsize/2,ysize/4)
	display_text('consolas',50,'Loading game . . . .',(0,0,0),xsize/2,ysize/4+200)
	display_text('consolas',50,'Instruction',(0,0,0),xsize/2,ysize/4+350)
	display_text('consolas',40,'collect as many objects as possible',(0,0,0),xsize/2,ysize/4+430)
	display_text('consolas',40,'without hitting the wall',(0,0,0),xsize/2,ysize/4+470)
	pygame.display.update()
	time.sleep(1)
	()
	window.fill((220,220,220))
	display_text('consolas',60,'Get Ready!',(0,0,0),xsize/2,ysize/4+100)
	pygame.display.update()
	time.sleep(2)

def over():
	window.fill((220,220,220))
	display_text('consolas',90,'GAME OVER',(0,0,0),xsize/2,ysize/4) 
	display_text('consolas',50,'Your score : '+str(score),(0,0,0),xsize/2,ysize/4+150)
	display_text('consolas',50,'Level reached : '+str(level),(0,0,0),xsize/2,ysize/4+200)
	
	if score<2:
		display_text('consolas',50,'Better luck next time',(0,0,0),xsize/2,ysize/4+270)
		
	elif score<6:
		display_text('consolas',50,'Nice try',(0,0,0),xsize/2,ysize/4+270)
		
	elif score<10:
		display_text('consolas',50,'Well played',(0,0,0),xsize/2,ysize/4+270)
		
	else:
		display_text('consolas',50,'You are Excellent',(0,0,0),xsize/2,ysize/4+270)  
	
	#display_text('consolas',40,'press F to retry',(0,0,0),xsize/2,ysize/4+350)	
	pygame.display.flip()
	#time.sleep(100)
	#pygame.quit()
	#sys.exit()

start_window()
	    	
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_UP or event.key == ord('w'):
        	   change_direction = 'UP'
        	if event.key == pygame.K_DOWN or event.key == ord('s'):
        	   change_direction = 'DOWN'
        	if event.key == pygame.K_LEFT or event.key == ord('a'):
        	   change_direction = 'LEFT'
        	if event.key == pygame.K_RIGHT or event.key == ord('d'):
        	   change_direction = 'RIGHT'
        	if event.key == pygame.K_ESCAPE:
        	   pygame.event.post(pygame.event.Event(pygame.QUIT))
        	  
    if change_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
        
                         
    if direction == 'UP':
        snake_pos[1] -= 5
    if direction == 'DOWN':
        snake_pos[1] += 5
    if direction == 'LEFT':
        snake_pos[0] -= 5
    if direction=='RIGHT':
        snake_pos[0] += 5
           
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0]//10 == food_pos[0]//10 and snake_pos[1]//10 == food_pos[1]//10:
        score += 1
        food_spawn = False
        level_completion+=1
    else:
        snake_body.pop()
    if level_completion==5:
    	difficulty+=10
    	level_completion=0
    	level+=1
    
     
     
    if not food_spawn:
        food_pos = [random.randrange(1, (xsize//10)) * 10, random.randrange(1, (ysize//10)) * 10]
    food_spawn = True    
    
    window.fill((155,155,155))	
    pygame.draw.rect(window,(0,0,0),pygame.Rect(10,10,xsize-10,ysize-10))

   
    for pos in snake_body:
        pygame.draw.rect(window, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window,(255,5,5), pygame.Rect(food_pos[0], food_pos[1], 10, 10))    


    display_text('consolas',40,'Score : '+str(score),(0,0,255),xsize+70,35)  
    display_text('consolas',40,'Level : '+str(level),(0,0,255),xsize+70,75)  
    
    
    if snake_pos[0] < 10 or snake_pos[0] > xsize-10:
        over()
        #if retry==True:
        	#retry=False
        continue
        #pygame.quit()
        #sys.exit
    if snake_pos[1] < 10 or snake_pos[1] > ysize-10:
        over()
        continue
        #pygame.quit()
        #sys.exit()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            over()    	 
  
    pygame.display.update()
    fps.tick(difficulty)