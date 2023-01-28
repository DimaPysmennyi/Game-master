import pygame

def death():
	death = pygame.mixer.Sound('sounds\death.mp3')
	death.set_volume(0.1)
	death.play()



def bg_music(filename):
    pygame.mixer.music.load('sounds\\' + filename)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    
def music_stop():
    pygame.mixer.music.stop()