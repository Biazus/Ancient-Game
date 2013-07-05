# -*- coding: cp1252 -*-

import pygame, sys, os, time
from pygame.locals import *
from intro import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

BLACK_COLOR = (0, 0, 0)
BLUE_COLOR = (0, 0, 255)

def event_space(menu_on):
    for event in pygame.event.get(): 
         if event.type == QUIT: 
            sys.exit(0)
         elif event.type == KEYDOWN:
            keyState = pygame.key.get_pressed()
            if (keyState[K_SPACE]):
                menu_on = 0
    return menu_on

def instructions0():
     keyState = pygame.key.get_pressed()
     menu_on = 1
     while(not keyState[K_SPACE] and menu_on == 1):

            writeLine("Ancient", (280,20), 100, p_rgbcolor=(70, 20, 20))
    
            textList = []
            font = pygame.font.SysFont('helvetica', 22)
            textList.append(font.render("Voce é o responsável pelo interrogatório", True, BLACK_COLOR))
            textList.append(font.render("de Abduhl, homem de 37 anos, acusado", True, BLACK_COLOR))
            textList.append(font.render("de assassinar 3 pessoas em uma casa na", True, BLACK_COLOR))
            textList.append(font.render("rua onde vive. Abduhl tem antecedentes", True, BLACK_COLOR))
            textList.append(font.render("por porte ilegal de arma, possui dois ", True, BLACK_COLOR))
            textList.append(font.render("filhos e trabalha como alfaiate há 10 anos.", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("Abduhl foi incriminado porque suas digitais", True, BLACK_COLOR))
            textList.append(font.render("constavam na arma do crime, uma pistola", True, BLACK_COLOR))
            textList.append(font.render("convencional, embora recentes resultados", True, BLACK_COLOR))
            textList.append(font.render("de laboratório informam que suas maos", True, BLACK_COLOR))
            textList.append(font.render("nao continham residuos de pólvora.", True, BLACK_COLOR))
            textList.append(font.render("O acusado é lembrado por, há 6 anos", True, BLACK_COLOR))
            textList.append(font.render("atrás, ter sido responsável por colocar", True, BLACK_COLOR))
            textList.append(font.render("fogo em sua antiga casa.", True, BLACK_COLOR))         

            startTextX = 240
            startTextY = 100
            
            for text in textList:
                screen.blit(text, (startTextX,startTextY))
                pygame.display.flip()
                startTextY += 30

            font = pygame.font.SysFont('helvetica', 18)
            text = (font.render("Press Space to continue", True, BLUE_COLOR))
            screen.blit(text, (385,545))
            pygame.display.flip()
            menu_on = event_space(menu_on)
     
            

def instructions1():
     menu_on = 1
     keyState = pygame.key.get_pressed()
     while(not keyState[K_SPACE] and menu_on == 1):

            writeLine("Ancient", (280,20), 100, p_rgbcolor=(70, 20, 20))
            textList = []
            font = pygame.font.SysFont('helvetica', 22)
            textList.append(font.render("Ele jura ser inocente, e inclusive possui", True, BLACK_COLOR))
            textList.append(font.render("um álibi (nao muito confiável): um jovem de", True, BLACK_COLOR))
            textList.append(font.render("25 anos que tem problemas com bebida.", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("Um de seus filhos possui 22 e, o outro, 17.", True, BLACK_COLOR))
            textList.append(font.render("Os filhos sao oriundos de um relaciona-", True, BLACK_COLOR))
            textList.append(font.render("mento instável com Yohanna, que faleceu", True, BLACK_COLOR))
            textList.append(font.render("há 2 anos atrás devido a um acidente de", True, BLACK_COLOR))
            textList.append(font.render("carro.", True, BLACK_COLOR))
            textList.append(font.render("O filho mais novo usa drogas desde entao.", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))

            startTextX = 240
            startTextY = 100
            
            for text in textList:
                screen.blit(text, (startTextX,startTextY))
                pygame.display.flip()
                startTextY += 30

            font = pygame.font.SysFont('helvetica', 18)
            text = (font.render("Press Space to continue", True, BLUE_COLOR))
            screen.blit(text, (385,545))
            pygame.display.flip()
            
            menu_on = event_space(menu_on)


def instructions2():
     menu_on = 1
     keyState = pygame.key.get_pressed()
     while(not keyState[K_SPACE] and menu_on == 1):

            writeLine("Ancient", (280,20), 100, p_rgbcolor=(70, 20, 20))
            textList = []
            font = pygame.font.SysFont('helvetica', 22)
            textList.append(font.render("Como promotor, voce terá a ultima chan-", True, BLACK_COLOR))
            textList.append(font.render("ce de decidir o futuro deste homem du-", True, BLACK_COLOR))
            textList.append(font.render("rante, exatamente, 10 min. em uma sala.", True, BLACK_COLOR))
            textList.append(font.render("Abduhl nao quis a presenca do advogado", True, BLACK_COLOR))
            textList.append(font.render("nesse interrogatório. Você e Abduhl se", True, BLACK_COLOR))
            textList.append(font.render("encontram a sós numa sala, enquanto a-", True, BLACK_COLOR))
            textList.append(font.render("guardam o início da sessao de julgamen-", True, BLACK_COLOR))
            textList.append(font.render("to.", True, BLACK_COLOR))
            textList.append(font.render("Sua reputacao é alta, levando a crer que", True, BLACK_COLOR)) 
            textList.append(font.render("a decisao final do júri basear-se-á, prova-", True, BLACK_COLOR))
            textList.append(font.render("velmente, na sua.", True, BLACK_COLOR))
            textList.append(font.render("", True, BLACK_COLOR))
            textList.append(font.render("Lembre-se, voce tem apenas 10 minutos.", True, BLACK_COLOR))

            startTextX = 240
            startTextY = 100
            
            for text in textList:
                screen.blit(text, (startTextX,startTextY))
                pygame.display.flip()
                startTextY += 30

            font = pygame.font.SysFont('helvetica', 18)
            text = (font.render("Espaco para iniciar", True, BLUE_COLOR))
            screen.blit(text, (385,545))
            pygame.display.flip()
            
            menu_on = event_space(menu_on)
