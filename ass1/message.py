import pygame
def text_objects(msg,color):
	font = pygame.font.SysFont(None,25)
	text_surface = font.render(msg, True, color)
	return text_surface, text_surface.get_rect()
def message_to_screen(msg,color,display_width,display_height,game_display):
	text_surface, text_rect=text_objects(msg,color)
	text_rect.center=(display_width/2),(display_height/2)
	game_display.blit(text_surface,text_rect)
