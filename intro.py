# -*- coding: cp1252 -*-

import pygame, sys, os, time
import warnings
from dialogs import *
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

dir(pygame)

main_dir = os.path.split(os.path.abspath(__file__))[0]
screen =pygame.display.set_mode((800, 600))

def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""
    def newFunc(*args, **kwargs):
        warnings.warn("Call to deprecated function %s." % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    newFunc.__name__ = func.__name__
    newFunc.__doc__ = func.__doc__
    newFunc.__dict__.update(func.__dict__)
    return newFunc

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def update_clock():
    time.clock()
    minutes = 0
    if(time.clock() > 60):
       minutes = int(time.clock()/60)
    seconds = int(time.clock()) - (minutes * 60)
    show_clock(minutes, seconds)


def show_clock(minutes, seconds):
    #print "%02d" % (minutes)
    font = pygame.font.SysFont('helvetica', 25)
    text = (font.render(str(minutes), True, BLACK_COLOR))
    screen.blit(text, (9,9))
    pygame.display.flip()
    text = (font.render(str(seconds), True, BLACK_COLOR))
    screen.blit(text, (9,30))
    pygame.display.flip()
    return

def writeLine(p_text, p_position, p_fontsize, p_font = None,  p_rgbcolor = (0,0,0)):
    font = pygame.font.Font(None, p_fontsize)
    text = font.render(p_text, True, p_rgbcolor)
    screen.blit(text, p_position)
    pygame.display.flip()

@deprecated
def switch(x):
    "call the given function using a dictionary"
    try:    
        d_game_dialogs[x]()
    except:
        print x

class InfoMenu(pygame.sprite.Sprite):
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect().move(235,100)

    def update(self):
        self.kill()
        #time.sleep(4)
        

def main(winstyle = 0):
    #Initializing pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    #Screen
    #screen = pygame.display.set_mode((800, 600)) 

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    InfoMenu.images = [load_image('menu.png')]
    InfoMenu.images[0].set_alpha(150)


    #Game window
    icone = load_image('icon.png')
    icon = pygame.transform.scale(icone, (32,32))
    pygame.display.set_icon(icon)#****Not working****
    pygame.display.set_caption('Ancient - The Game')
    pygame.mouse.set_visible(1)#****
    
    #Background image
    background = load_image('room800600.png')
    background.set_alpha(255) # set the opacity temporarily (betw 0 and 255)
    screen.blit(background, (0,0))
    pygame.display.flip()

    #Initialize game groups
    infomenu = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    #assign default groups to each sprite class
    InfoMenu.containers = infomenu, all    

    clock = pygame.time.Clock()
    
    which_menu = 0
    menuActive = [instructions0, instructions1, instructions2]
    
    while True: #main loop
        all.clear(screen, background)
        all.update()
        
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                sys.exit(0)
        keyState = pygame.key.get_pressed()
                
        if (which_menu < len(menuActive) and not keyState[K_SPACE]):
            InfoMenu()
            dirty = all.draw(screen)
            pygame.display.update(dirty)
            menuActive[which_menu]()
            which_menu = which_menu + 1

        if (which_menu >= 3):
             update_clock()
            
        #cleaning screen calling background design
        screen.blit(background, (0,0))
        pygame.display.flip()

        #update all the sprites (****check whether we need it)
        dirty = all.draw(screen)
        pygame.display.update(dirty)


#call the "main" function if running this script
if __name__ == '__main__': main()
