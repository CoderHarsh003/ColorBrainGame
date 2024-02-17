import pygame
import random
num = random.randint(15,20)

scene=1
pygame.init()
substances=[]
colors=[]
win = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Brain Game')

lines=1
font1=pygame.font.SysFont(None,100)
font2=pygame.font.SysFont(None,130)
scene1=[[(250,20,20),(20,20,50,50)],[(9,204,8),(300,250,400,100)]]
texts=['RED','YELLOW','BLUE','GREEN','GREY','ORANGE','BLACK','BROWN','PINK','WHITE']
sizes=[143,292,185,240,194,307,239,268,185,240]
pallete=[(255,0,0),(255,240,12),(0,0,255),(0,255,0),(80,80,80),(255,127,40),(0,0,0),(120,60,18),(255,113,187)]
x,y=20,50
k=50
run=True
clock = pygame.time.Clock()
m_pos=(900,900)
def text_screen2(my_font,text, color, x, y):
    screen_text = my_font.render(text, True, color)
    win.blit(screen_text,[x,y])

while run:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.MOUSEMOTION:
            m_pos=pygame.mouse.get_pos()

    if(scene == 1):
        win.fill((31,35,99))
        if (20<=m_pos[0]<=70 and 20<=m_pos[1]<=70):
            scene1[0][0] = (250,20,20)
            if pygame.mouse.get_pressed()[0] == 1:
                run = False
        else:
            scene1[0][0] = (250,100,100)
        if (300<=m_pos[0]<=700 and 250<=m_pos[1]<=350):
            scene1[1][0] = (11,252,9)
            if pygame.mouse.get_pressed()[0] == 1:
                scene = 2
                texts2=texts
                pallete2=pallete
                while len(substances)<num:
                    text_index = random.randint(0,len(texts2)-1)
                    substances.append(text_index)
                    color_index = random.randint(0,len(pallete2)-1)
                    colors.append(color_index)
        else:
            scene1[1][0] = (9,204,8)
        pygame.draw.rect(win, scene1[0][0],scene1[0][1])
        pygame.draw.rect(win, scene1[1][0],scene1[1][1])
        text_screen2(font2,"Start", (255,255,255),395,256)
        text_screen2(font2,"<",(255,255,255),19,-6)
    if scene == 2:
        win.fill((255,255,255))
        for some in range(len(substances)):
            i = substances[some]
            if (x+sizes[i]>980):
                x=20
                y+=80
            text_screen2(font1,texts[i],pallete[colors[some]],x,y)
            x+=sizes[i]+20
        x=20
        y=k
    pygame.display.update()
    clock.tick(100)

pygame.quit()