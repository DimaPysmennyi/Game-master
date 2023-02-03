import pygame

def sound(filename, a):
	sound1 = pygame.mixer.Sound('sounds\\' + filename)
	sound1.set_volume(a)
	sound1.play()

def bg_music(filename):
    pygame.mixer.music.load('sounds\\' + filename)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    
    
def music_stop():
    pygame.mixer.music.stop()

sound_repeat = 0