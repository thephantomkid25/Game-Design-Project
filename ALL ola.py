# The following is a protoype that needs adjustment for real world application 

import pygame
from pygame import *
import random
import sys

pygame.init()
pygame.mixer.init()

# set dimensons for screen and define clock 
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((1280,600),0,32)#(1280,1024)

# Define all images here
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
Go_Message = pygame.image.load("images/go!.png").convert_alpha()
Watch_Message = pygame.image.load("images/watch.png").convert_alpha()

# miscellaneous and lists
Arrows = [Up,Down,Right,Left]
Fighters = [Tails,Sonic,Shadow]
Fighter_names = ["Tails","Sonic","Shadow"]
Player_1 = 0
Player_2 = 0
Player1Health = 50
Player2Health = 50

# Load all the sound files 

        # Background Music
booba_intro = pygame.mixer.Sound('booba/booba intro.wav')
booba_intro_1 = pygame.mixer.Sound('booba/booba intro 1.wav')
booba_loop = pygame.mixer.Sound('booba/booba loop.wav')
booba_loop_1 = pygame.mixer.Sound('booba/booba loop 1.wav')
booba_loop_4 = pygame.mixer.Sound('booba/booba loop 4.wav')
booba_loop_6 = pygame.mixer.Sound('booba/booba loop 6.wav')
booba_loop_7 = pygame.mixer.Sound('booba/booba loop 7.wav')

        # Character Sounds
come_get_some = pygame.mixer.Sound('character sounds/ComeGetSome.wav')
falcon_punch = pygame.mixer.Sound('character sounds/FalconPunch 1.wav')
make_my_day = pygame.mixer.Sound('character sounds/GoAheadMakeMyDay.wav')
hail_the_king = pygame.mixer.Sound('character sounds/HailToTheKingBaby.wav')
big_guns = pygame.mixer.Sound('character sounds/ILikeBigGunsAndICannotLie.wav')
equal_kicker = pygame.mixer.Sound('character sounds/ImAnEqualOpportunityAssKicker.wav')
get_medieval = pygame.mixer.Sound('character sounds/ImGonnaGetMedievalOnYourAsses.wav')
its_my_way = pygame.mixer.Sound('character sounds/ItsMyWayOr.wav')
balls_of_steel = pygame.mixer.Sound('character sounds/IveGotBallsOfSteel.wav')
go_postal = pygame.mixer.Sound('character sounds/LooksLikeItsTimeForMeToGoPostal.wav')
my_gun_is_bigger = pygame.mixer.Sound('character sounds/MyGunIsBiggerThanYours.wav')
my_little_friend = pygame.mixer.Sound('character sounds/SayHelloToMyLittleFriend 1.wav')
something_smells = pygame.mixer.Sound('character sounds/SomethingSmellsRottenAroundHere.wav')
who_wants_some = pygame.mixer.Sound('character sounds/WhoWantsSome.wav')
sparta = pygame.mixer.Sound('character sounds/Sparta 2.wav')

# Define all the sound channels
pygame.mixer.set_num_channels(8)
background_music = pygame.mixer.Channel(0)
p1_sounds = pygame.mixer.Channel(1)
p2_sounds = pygame.mixer.Channel(2)
clock_tick_sound = pygame.mixer.Channel(3)
climax_sound = pygame.mixer.Channel(4)
mash_it = pygame.mixer.Channel(5)
saving_roll = pygame.mixer.Channel(6)
stats_screen = pygame.mixer.Channel(7)
SONG_END = pygame.USEREVENT + 1
p1_sounds.set_endevent(SONG_END)
p2_sounds.set_endevent(SONG_END)

def Title_Screen():
    background_music.play(booba_intro_1)
    x = 1
    Screen.blit(Background_image,(0,0))
    pygame.display.update() 
    while x != 0 :
        background_music.queue(booba_loop_1)
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    background_music.stop()
                    break
        Text_rect = pygame.Rect((100,500),(700,200))
        label = Font_type.render("Please press enter",52,(0,255,255))
        Screen.blit(label,Text_rect)
        time.delay(200)
        pygame.display.update(Text_rect)
        pygame.draw.rect(Screen,(0,0,0),Text_rect)
        time.delay(200)
        pygame.display.update(Text_rect)
        pygame.display.update()
        '''Clock.tick(3)
        Screen.blit(Background_image,(0,0))
        pygame.display.update()
        Clock.tick(3)'''
def Character_select_screen():
    background_music.play(booba_loop_1,-1)
    x = 1
    a = 0
    Screen.blit(Space,(0,0))
    F1 = pygame.Rect((100,650),(300,300))
    F2 = pygame.Rect((500,650),(300,300))
    F3 = pygame.Rect((900,650),(300,300))
    Name = pygame.Rect((1000,100),(1000,50))
    CurrentChar = pygame.Rect((500,200),(250,300))
    label = Font_type.render(str(Fighter_names[a]),52,(0,255,255))
    pygame.draw.rect(Screen,(0,0,0),Name,0)
    pygame.draw.rect(Screen,(0,0,0),CurrentChar,0)
    Screen.blit(Fighters[a],CurrentChar)
    Screen.blit(label,Name)
    Screen.blit(Fighters[0],F1)
    Screen.blit(Fighters[1],F2)
    Screen.blit(Fighters[2],F3)
    pygame.display.update()
    while x != 0:
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END:
                background_music.set_volume(1.0)
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
                    background_music.set_volume(0.4)
                    if a == 0:
                        p1_sounds.play(my_little_friend)
                    elif a == 1:
                        p1_sounds.play(falcon_punch)
                    elif a == 2:
                        p1_sounds.play(sparta)    
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
                    background_music.set_volume(0.4)
                    if a == 0:
                        p1_sounds.play(my_little_friend)
                    elif a == 1:
                        p1_sounds.play(falcon_punch)
                    elif a == 2:
                        p1_sounds.play(sparta)
                    pygame.display.update()
    x = 1
    while x != 0:
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END:
                background_music.set_volume(1.0)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    Player_2 = a
                    background_music.stop()
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
                    background_music.set_volume(0.4)
                    if a == 0:
                        p1_sounds.play(my_little_friend)
                    elif a == 1:
                        p1_sounds.play(falcon_punch)
                    elif a == 2:
                        p1_sounds.play(sparta)
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
                    background_music.set_volume(0.4)
                    if a == 0:
                        p1_sounds.play(my_little_friend)
                    elif a == 1:
                        p1_sounds.play(falcon_punch)
                    elif a == 2:
                        p1_sounds.play(sparta)
                    pygame.display.update()
    return Player_1,Player_2
def Combo_seq_screen(b,c):
    background_music.play(booba_loop_4,-1)
    combo_P1 = 0
    combo_P2 = 0
    Screen.blit(Water,(0,0))
    Area = pygame.Rect((100,100),(600,600))
    Char = pygame.Rect((800,500),(300,300))
    Combo = Screen.blit(Left,(1000,900))
    UserInput = pygame.Rect((350,350),(853,683))
    Timer = pygame.Rect((800,100),(150,75))
    Player = pygame.Rect((1000,100),(200,200))
    Screen.blit(Fighters[b],Char)
    pygame.draw.rect(Screen,(255,255,255),Combo)
    combo_level = 0
    x = 0 #garbage value
    index = 0
    timer = pygame.time.Clock()
    fps = 2.0 #modified later
    player = []
    Comp = []
    a = 13.0
    Screen.blit(Watch_Message,Area)
    pygame.display.update()
    time.delay(2000)
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
            if x == 4:
                time.delay(1000)
                pygame.display.update(Area)
                Screen.blit(Go_Message,Area)
                pygame.display.update(Area)
                time.delay(2000)
                pygame.draw.rect(Screen, (255,255,255),Area)
        x = 0 #reset garbage variable
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
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        x += 1
                        player.append(2)
                        Screen.blit(Right,UserInput)
                    elif event.key == K_UP:
                        x += 1
                        player.append(0)
                        Screen.blit(Up,UserInput)
                    elif event.key == K_LEFT:
                        x += 1
                        player.append(3)
                        Screen.blit(Left,UserInput)
                    elif event.key == K_DOWN:
                        x += 1
                        player.append(1)
                        Screen.blit(Down,UserInput)
                pygame.display.update(UserInput)
            a -= .0025
            timer.tick(1000)
            if x == 4:
                time.delay(1000)
                pygame.display.update(Area)
                Screen.blit(Watch_Message,Area)
                pygame.display.update(Area)
                time.delay(1000)
                pygame.draw.rect(Screen, (255,255,255),Area)
                time.delay(1000)
        if x > 3 : 
            pygame.time.delay(1000)
            pygame.draw.rect(Screen,(255,0,0),Area)
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
    

   # PUT A LEVEL INDACTOR
   # TIGHTEN UP THE COMBO SEQUENCE
   # PUT UP THE IMAGES THE DESIGN TEAM GAVE YOU
   # MODIFY PLAYER 2 COMBO SEQUENCE PART


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
                    pygame.quit()
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
            a -= .0025
          # a -= .01
          # a -= .001
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
                    n -= 3 * w
                elif event.key == K_UP:
                    n -= 3 * w
                elif event.key == K_LEFT:
                    n -= 3 * w
                elif event.key == K_DOWN:
                    n -= 3 * w
                elif event.key == K_d:
                    n += 3 * q
                elif event.key == K_a:
                    n += 3 * q
                elif event.key == K_s:
                    n += 3 * q
                elif event.key == K_w:
                    n += 3 * q
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

