''' The following is a protoype that needs adjustment for real world application '''
import pygame
from pygame import *
import random
import sys

pygame.init()
'''set dimensons for screen and define clock '''
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((1280,1024),0,32)
'''Define all images here'''

Font_type = pygame.font.SysFont('monospace',52)
Background_image = pygame.image.load("images/Mash title.jpg").convert_alpha()
Tails = pygame.image.load("images/Tail1.png").convert_alpha()
Sonic = pygame.image.load("images/Sonic1.png").convert_alpha()
Shadow = pygame.image.load("images/Shadow1.png").convert_alpha()
Space = pygame.image.load("images/space.jpg").convert_alpha()
Water = pygame.image.load("images/water.jpg").convert_alpha()
Up = pygame.image.load("images/Up.png").convert_alpha()
Down = pygame.image.load("images/Down.png").convert_alpha()
Right = pygame.image.load("images/Right.png").convert_alpha()
Left = pygame.image.load("images/Left.png").convert_alpha()
'''miscellaneous and lists'''
Arrows = [Up,Down,Right,Left]
Fighters = [Tails,Sonic,Shadow]
Fighter_names = ["Tails","Sonic","Shadow"]
Player_1 = 0
Player_2 = 0
Player1Health = 50
Player2Health = 50
def Title_Screen():
    x = 1
    Screen.blit(Background_image,(0,0))
    pygame.display.update() 
    while x != 0 :
        for event in pygame.event.get():       
            if event.type == QUIT:
                sys.exit()
                pygame.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    break
        Text_rect = pygame.Rect((100,800),(200,200))
        label = Font_type.render("Please press enter",52,(0,255,255))
        Screen.blit(label,Text_rect)
        pygame.display.update()
        Clock.tick(3)
        Screen.blit(Background_image,(0,0))
        pygame.display.update()
        Clock.tick(3)
def Character_select_screen():
    x = 1
    a = 0
    Screen.blit(Space,(0,0))
    F1 = pygame.Rect((100,650),(300,300))
    F2 = pygame.Rect((500,650),(300,300))
    F3 = pygame.Rect((900,650),(300,300))
    Name = pygame.Rect((1000,100),(1000,50))
    CurrentChar = pygame.Rect((500,200),(250,300))
    pygame.draw.rect(Screen,(0,0,0),CurrentChar,0)
    pygame.draw.rect(Screen,(0,0,0),Name,0)
    Screen.blit(Fighters[0],F1)
    Screen.blit(Fighters[1],F2)
    Screen.blit(Fighters[2],F3)
    pygame.display.update()
    while x != 0:
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.exit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    Player_1 = a
                    break
                if event.key == K_RIGHT:
                    a += 1
                    if a > 2:
                        a = 0
                    label = Font_type.render(str(Fighter_names[a]),52,(0,255,255))
                    pygame.draw.rect(Screen,(0,0,0),Name,0)
                    Screen.blit(label,Name)
                    pygame.draw.rect(Screen,(0,0,0),CurrentChar,0)
                    Screen.blit(Fighters[a],CurrentChar)
                    pygame.display.update()
                if event.key == K_LEFT:
                    a -= 1
                    if a < 0:
                        a = 2
                    label = Font_type.render(str(Fighter_names[a]),52,(0,255,255))
                    pygame.draw.rect(Screen,(0,0,0),Name,0)
                    Screen.blit(label,Name)
                    pygame.draw.rect(Screen,(0,0,0),CurrentChar,0)
                    Screen.blit(Fighters[a],CurrentChar)
                    pygame.display.update()
    x = 1
    while x != 0:
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.exit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    Player_2 = a
                    break
                if event.key == K_RIGHT:
                    a += 1
                    if a > 2:
                        a = 0
                    label = Font_type.render(str(Fighter_names[a]),52,(0,255,255))
                    pygame.draw.rect(Screen,(0,0,0),Name,0)
                    Screen.blit(label,Name)
                    pygame.draw.rect(Screen,(0,0,0),CurrentChar,0)
                    Screen.blit(Fighters[a],CurrentChar)
                    pygame.display.update()
                if event.key == K_LEFT:
                    a -= 1
                    if a < 0:
                        a = 2
                    label = Font_type.render(str(Fighter_names[a]),52,(0,255,255))
                    pygame.draw.rect(Screen,(0,0,0),Name,0)
                    Screen.blit(label,Name)
                    pygame.draw.rect(Screen,(0,0,0),CurrentChar,0)
                    Screen.blit(Fighters[a],CurrentChar)
                    pygame.display.update()
    return Player_1,Player_2
def Combo_seq_screen(b,c):
    combo_P1 = 0
    combo_P2 = 0
    Screen.blit(Water,(0,0))
    Area = pygame.Rect((100,100),(600,600))
    Char = pygame.Rect((800,500),(300,300))
    Combo = pygame.Rect((800,900),(50,50))
    Timer = pygame.Rect((800,100),(150,75))
    Player = pygame.Rect((1000,100),(200,200))
    Screen.blit(Fighters[b],Char)
    pygame.draw.rect(Screen,(255,255,255),Combo)
    x = 0 #garbage value
    index = 0
    timer = pygame.time.Clock()
    fps = 1.5 #modified later
    player = []
    Comp = []
    a = 13.0
    #for event in pygame.event.get():
    while a >= 0: 
        while x <= 3:
            random.seed()
            index = random.randint(0,3)
            pygame.draw.rect(Screen,(255,255,255),Area)
            Screen.blit(Arrows[index],(random.randint(100,600),random.randint(100,600)))
            pygame.display.update()
            Comp.append(index)
            x += 1
            timer.tick(fps)
        x = 0 #reset garbage variable
        pygame.draw.rect(Screen,(255,255,0),Area)
        pygame.display.update(Area)
        pygame.time.delay(1000)
        pygame.draw.rect(Screen,(255,255,255),Area)
        pygame.display.update(Area)
        while (x <= 3):
            if a <= 0:
                break
            label = Font_type.render(str(int(a)),15,(255,0,0))
            pygame.draw.rect(Screen,(255,255,255),Timer)
            Screen.blit(label, Timer)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.exit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        x += 1
                        player.append(2)
                    elif event.key == K_UP:
                        x += 1
                        player.append(0)
                    elif event.key == K_LEFT:
                        x += 1
                        player.append(3)
                    elif event.key == K_DOWN:
                        x += 1
                        player.append(1)
            a -= .001
            timer.tick(1000)
        x = 0
        if Comp == player:
            combo_P1 += 1
            pygame.draw.rect(Screen,(255,255,255),Combo)
            label = Font_type.render(str(combo_P1),15,(255,0,0))
            Screen.blit(label,Combo)
            pygame.display.update()
        else:
            pygame.display.update()
        Comp = []
        player = []
        a -= .001
        timer.tick(1000)
    pygame.event.clear()
    Screen.blit(Water,(0,0))
    pygame.display.update()
    pygame.time.delay(5000) # delay b4 P2 start
    Area = pygame.Rect((100,100),(600,600))
    Char = pygame.Rect((800,500),(300,300))
    Combo = pygame.Rect((800,900),(50,50))
    Timer = pygame.Rect((800,100),(150,75))
    Player = pygame.Rect((1000,100),(200,200))
    pygame.draw.rect(Screen,(255,255,255),Area)
    pygame.draw.rect(Screen,(255,255,255),Timer)
    Screen.blit(Fighters[c],Char)
    pygame.draw.rect(Screen,(255,255,255),Combo)
    pygame.display.update()
    pygame.time.delay(5000) #delay before P2 start game
    x = 0 #garbage value
    index = 0
    timer = pygame.time.Clock()
    fps = 2.1 #modified later
    player = []
    Comp = []
    a = 23.0
    #for event in pygame.event.get():
    while a >= 0: 
        while x <= 3:
            random.seed()
            index = random.randint(0,3)
            pygame.draw.rect(Screen,(255,255,255),Area)
            Screen.blit(Arrows[index],(random.randint(100,600),random.randint(100,600)))
            pygame.display.update()
            Comp.append(index)
            x += 1
            label = Font_type.render(str(int(a)),15,(255,0,0))
            a -= 1
            timer.tick(fps)
        x = 0 #reset garbage variable
        while (x <= 3):
            if a <= 0:
                break
            label = Font_type.render(str(int(a)),15,(255,0,0))
            pygame.draw.rect(Screen,(255,255,255),Timer)
            Screen.blit(label, Timer)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                    pygame.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        x += 1
                        player.append(2)
                    elif event.key == K_UP:
                        x += 1
                        player.append(0)
                    elif event.key == K_LEFT:
                        x += 1
                        player.append(3)
                    elif event.key == K_DOWN:
                        x += 1
                        player.append(1)
            a -= .001
            timer.tick(1000)
        x = 0
        if Comp == player:
            combo_P2 += 1
            pygame.draw.rect(Screen,(255,255,255),Combo)
            label = Font_type.render(str(combo_P2),15,(255,0,0))
            Screen.blit(label,Combo)
            pygame.display.update()
        else:
            pygame.display.update()
        a -= .001
        Comp = []
        player = []
        timer.tick(1000)
    return combo_P1,combo_P2
def MASH_Screen(u,y,w,q):
    global Player1Health
    global Player2Health
    a = 10.0
    x = 0
    j = 0
    n = 0
    while a >= 0 and (-290 < n <290):
        Screen.blit(Space,(0,0))
        Timer = pygame.Rect((580,0),(120,75))
        Playerbox1 = pygame.Rect((20,20),(50,50))
        Playerbox2 = pygame.Rect((1210,20),(50,50))
        Healthf1 = pygame.Rect((50,900),(150,20))
        Healthf2 = pygame.Rect((1080,900),(150,20))
        Charachter_box1 = pygame.Rect((300,700),(300,300))
        Charachter_box2 = pygame.Rect((680,700),(300,300))
        Sprite_1 = pygame.Rect((50,300),(300,300))
        Sprite_2 = pygame.Rect((930,300),(300,300))
        Screen.blit(Fighters[u],Charachter_box1)
        Screen.blit(Fighters[y],Charachter_box2)
        Screen.blit(Font_type.render(str("P1"),15,(255,0,0)),Playerbox1)
        Screen.blit(Font_type.render(str("P2"),15,(255,0,0)),Playerbox2)
        pygame.draw.rect(Screen,(0,0,0),Healthf1)
        pygame.draw.rect(Screen,(0,0,0),Healthf2)
        pygame.draw.rect(Screen,(255,255,255),Sprite_1)
        pygame.draw.rect(Screen,(255,255,255),Sprite_2)
        player1_thug = pygame.Rect((350,450),(290+n,75))
        player2_thug = pygame.Rect((640+n,450),(290-n,75))
        pygame.draw.rect(Screen,(255,0,0),player1_thug)
        pygame.draw.rect(Screen,(255,0,255),player2_thug)
        for event in pygame.event.get():
            if a <= 0 or (-290 >= n) or (n> 290) :
                break
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    n -= 1 * w
                elif event.key == K_UP:
                    n -= 1 * w
                elif event.key == K_LEFT:
                    n -= 1 * w
                elif event.key == K_DOWN:
                    n -= 1 * w
                elif event.key == K_d:
                    n += 1 * q
                elif event.key == K_a:
                    n += 1 * q
                elif event.key == K_s:
                    n += 1 * q
                elif event.key == K_w:
                    n += 1 * q
        a -= float(1.0/500)
        pygame.draw.rect(Screen,(255,255,255),Timer)
        label = Font_type.render(str(int(a)),15,(255,0,0))
        Screen.blit(label,Timer)
        player1_thug = pygame.Rect((350,450),(290+n,75))
        player2_thug = pygame.Rect((640+n,450),(290-n,75))
        pygame.draw.rect(Screen,(255,0,0),player1_thug)
        pygame.draw.rect(Screen,(255,0,255),player2_thug)
        pygame.display.update()
        Clock.tick(500)
    if n < 0:
        print "P2 won"
        Player2Health -= n/4
    elif n > 0:
        print "P1 won"
        Player1Health -= n/4
    else:
        print "tie"
    return Player1Health,Player2Health

if __name__ == '__main__':
    Title_Screen()
    pygame.event.clear()
    u,y = Character_select_screen() # u and y are P1 and P2 charachters respectively
    pygame.event.clear()
    w,q = Combo_seq_screen(u,y) # P1 and P2 combo values respectively
    pygame.event.clear()
    print MASH_Screen(u,y,1,1)
''' need to modify screen 3, so combos are together instead of randomly generated'''
