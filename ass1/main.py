import pygame
import message
pygame.init()
white=(255,255,255)
black=(0,0,0)
blue=(255,0,0)
green=(0,155,0)
indigo=(155,0,55)
display_width=800
display_height=600
game_display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Donkey-Kong')
block_size=20
fps=20
font = pygame.font.SysFont(None, 39)
clock=pygame.time.Clock()
def walls():
	pygame.draw.rect(game_display, indigo, [0,0,800,20])
        pygame.draw.rect(game_display, indigo, [780,0,20,600])
        pygame.draw.rect(game_display, indigo, [0,580,800,20])
        pygame.draw.rect(game_display, indigo, [0,0,20,600])
def stairs():
	pygame.draw.rect(game_display, indigo, [0,485,700,15])
	pygame.draw.rect(game_display, indigo, [200,370,600,15])
	pygame.draw.rect(game_display, indigo, [0,255,600,15])
	pygame.draw.rect(game_display, indigo, [150,130,650,15])
	pygame.draw.rect(game_display, indigo, [140,0,15,70])
	pygame.draw.rect(game_display, indigo, [140,70,250,15])
	pygame.draw.rect(game_display, indigo, [390,0,15,85])
def ladders():
	screen_text = font.render("H",True,white)
	pygame.draw.rect(game_display, black, [300,70,20,15])
	l1 = [70,69,70,80,90,100,110,112]
	for i in l1:
		game_display.blit(screen_text, [300,i])
	pygame.draw.rect(game_display, black, [500,130,20,15])
	l2 = [130,129,130,140,150,160,170,180,190,200,210,220,230,238]
	for i in l2:
		game_display.blit(screen_text, [500,i])
	pygame.draw.rect(game_display, black, [200,130,20,15])
	l3 = [130,129,130,140,150,160,170,220,230,238]
	for  i in l3:
		game_display.blit(screen_text, [200,i])
	pygame.draw.rect(game_display, black, [350,255,20,15])
	l4 = [255,254,255,265,275,285,295,305,315,325,335,345,354]
	for i in l4: 
		game_display.blit(screen_text, [350,i])
	pygame.draw.rect(game_display, black, [600,370,20,15])
	l5 = [370,369,370,380,420,430,440,450,460,470]
	for  i in l5: 
		game_display.blit(screen_text,[600,i])
	pygame.draw.rect(game_display, black, [250,370,20,15])
	l6 = [370,369,370,380,390,400,410,420,430,440,450,460,470]
	for i in l6: 
		game_display.blit(screen_text,[250,i])
	pygame.draw.rect(game_display, black, [650,485,20,15])
	l7=[485,484,495,505,515,525,535,545,555,564]
	for i in l7:
		game_display.blit(screen_text,[650,i])
	pygame.draw.rect(game_display, black, [150,485,20,15])
	l8 = [485,484,495,505,515,555,564]
	for i in l8:
		game_display.blit(screen_text,[150,i]) 
def gameloop():
	game_exit=False
	game_over=False
	game_death=False
	lives=3
	player_x=block_size
	player_y=display_height-(2*block_size)
	player_x_change=0
	player_y_change=0
	pressed_left=False
	pressed_right=False
	while not game_exit:
		while game_death:
			lives-=1
			if lives==0:
				game_over=True
			else:
				game_death=False
				player_x=block_size
				player_y=display_height-(2*block_size)
				pygame.draw.rect(game_display,blue,[player_x,player_y,block_size,block_size])
				pygame.display.update()
		while game_over:
			game_display.fill(black)
			message.message_to_screen("PlayAgain:W,GameExit:Q",blue,display_width,display_height,game_display)
	                pygame.display.update()
	  		for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_exit = True
						game_over = False
					elif event.key == pygame.K_w:
						gameloop()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				game_exit=True
			elif event.type == pygame.KEYDOWN:          # check for key presses          
        			if event.key == pygame.K_LEFT:        # left arrow turns left
            				pressed_left = True
        			elif event.key == pygame.K_RIGHT:     # right arrow turns right
            				pressed_right = True
			elif event.type == pygame.KEYUP:            # check for key releases
			        if event.key == pygame.K_LEFT:        # left arrow turns left
			        	pressed_left = False
			        elif event.key == pygame.K_RIGHT:     # right arrow turns right
			        	pressed_right = False
		if pressed_left:
			player_x-=block_size
		if pressed_right:
			player_x+=block_size
		if player_x>=display_width or player_x<0 or player_y>=display_height or player_y<0:
			game_death = True
		game_display.fill(black)
		walls()
		stairs()
		ladders()
		pygame.draw.rect(game_display,green,[170,50,block_size,block_size])
		pygame.draw.rect(game_display,blue,[player_x,player_y,block_size,block_size])
                pygame.display.update()
	 	clock.tick(fps)
	pygame.quit()
	quit()
gameloop()
