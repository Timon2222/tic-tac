from pygame import *
window = display.set_mode((700, 500))
display.set_caption('krestiki noliki')
background = transform.scale(image.load('background.png'), (700, 500))



clock = time.Clock()
FPS = 60














sprite1 = transform.scale(image.load('krestik.png'), (70, 50))
sprite2 = transform.scale(image.load('nolik.png'), (70, 50))
game = True
finish = False

window.blit(background,(0, 0))
while game:
    if finish != True:
       



        for e in event.get():
            if e.type == QUIT:
                game = False    
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos
                window.blit(image.load('krestik.png'),(x, y))
            if e.type == MOUSEBUTTONDOWN and e.button == 3:
                x, y = e.pos
                window.blit(image.load('nolik.png'),(x, y))
    clock.tick(FPS)
    display.update()
