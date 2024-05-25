import pygame
import time
from character import Character, musuh
from character import Pembaharuan
import character

#Sprites --> credit from https://www.spriters-resource.com/submitter/Silverbolt/

pygame.init()

score = 0

layar = pygame.display.set_mode((character.width_screen,character.height_screen))
waktu = pygame.time.Clock()
pygame.display.set_caption("Inuyasha : First Generation")

image = pygame.image.load("sprites/logo.png")
pygame.display.set_icon(image)

font = pygame.font.Font("font/Pixeltype.ttf",50)
font1 = pygame.font.Font("font/Pixeltype.ttf",30)
font2 = pygame.font.Font("font/Pixeltype.ttf",21)
tutor1 = font2.render("Press A for Left", False, "Black")
tutor2 = font2.render("Press D for Right", False, "Black")
tutor3 = font2.render("Press W for Jump", False, "Black")
tutor4 = font2.render("Press S for Relax", False, "Black")
tutor5 = font2.render("Press Space for Skill", False, "Black")
text = font.render("Inuyasha : First Generation", False,"Red")
text1 = font1.render("Created by Silence", False,"Black")
fontscore = pygame.font.Font("font/Pixeltype.ttf",30)


keyboard = pygame.image.load("sprites/keyboard.png")
music = pygame.mixer.music.load("sound/MainBattle.mp3")
pygame.mixer.music.play(-1)
skilleffect = pygame.mixer.Sound("sound/skillsword.mp3")

#tampilan awal 
template = pygame.image.load("sprites/gunung1.png")
modelpertama = pygame.image.load("sprites/judul.png")
modelkeempat = pygame.image.load("sprites/kanji.png")
modelkedua = pygame.image.load("sprites/Inuyasha.png")
modelketiga = pygame.image.load("sprites/kagome.png")
perintah = font1.render("Press Enter to Start", False, "Black")
versi = font2.render("Version 1.0.1", False, "Black")
versi1 = font1.render("Version 1.0.1", False, "Black")
def redrawGame():
    character.layar.blit(character.latar_belakang, (0,0))
    layar.blit(text,(290, 20))
    layar.blit(text1,(420, 50))
    layar.blit(keyboard, (20, 20))
    pygame.draw.rect(layar, (0,0,0), (10,10,250,120),1)
    #tutorial
    layar.blit(tutor1,(130,20))
    layar.blit(tutor2,(130,35))
    layar.blit(tutor3,(130,50))
    layar.blit(tutor4,(130,65))
    layar.blit(tutor5,(130,80))
    #
    man.gambar(layar)
    mario.gambar(layar)
    
    textscore = fontscore.render("Score : "+str(score),1, "black")
    layar.blit(textscore,(450,75))
    layar.blit(versi1,(850,565))
    for senjata in pedang:
        senjata.gambar(layar)
    pygame.display.update()


#code dimulai ya sobat!
man = Character(100,450,40,60) 
mario = musuh(200, 450,40, 60,940)
pedang = []
tebasanberulang = 0 
gameON = True
active = False
start_game = False

while gameON:
    waktu.tick(20)
    if mario.visible == True:
        if man.hitbox[1] < mario.hitbox[1] + mario.hitbox[3] and man.hitbox[1] + man.hitbox[3] > mario.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] >  mario.hitbox[0] and man.hitbox[0] < mario.hitbox[0] + mario.hitbox[2]:
                man.tertonjok()
                score -= 5
    else:
        fontkata = pygame.font.Font("font/Pixeltype.ttf",80)
        kata = fontkata.render("You Win",False,"Red")
        layar.blit(kata,(390,280))
        pygame.display.update()
        delay_start = time.time()
        while time.time() - delay_start < 4: 
            pass
        gameON = False


    if tebasanberulang > 0:
        tebasanberulang +=  1
    if tebasanberulang > 5:
        tebasanberulang = 0
    
    for senjata in pedang:
        if senjata.y - senjata.radius < mario.hitbox[1] + mario.hitbox[3] and senjata.y + senjata.radius > mario.hitbox[1]:
            if senjata.x + senjata.radius > mario.hitbox[0] and senjata.x - senjata.radius < mario.hitbox[0] + mario.hitbox[2]:
                mario.tertebas()
                score += 1
                pedang.pop(pedang.index(senjata))

        if senjata.x < 1000 and senjata.x > 0:
            senjata.x += senjata.vel
        else:
            pedang.pop(pedang.index(senjata))

    key = pygame.key.get_pressed()
    man.update(key)

    if key[pygame.K_SPACE] and tebasanberulang == 0:
        man.serang = True
        skilleffect.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(pedang) < 5:
            pedang.append(Pembaharuan(round(man.x + man.width // 2) , round(man.y + man.height // 2), 6, (0,0,0), facing))
        
        tebasanberulang = 1

    if key[pygame.K_d] and man.x < 1000 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    elif key[pygame.K_s]:
        man.santai = True
        man.right = False
        man.left = False
        man.standing = False
    elif key[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    else:
        man.standing = True
        man.jumlahjalan = 0

    if not man.lompat:
        if key[pygame.K_w]:
            man.lompat = True
            man.standing = False
            man.right = False
            man.left = False
    else:
        if man.jumlahlompat >= -10:
            neg = 1
            if man.jumlahlompat < 0:
                neg = -1
            man.y -= (man.jumlahlompat ** 2) * 0.45 * neg
            man.jumlahlompat -= 1
        else:
            man.lompat = False
            man.jumlahlompat = 10
            man.standing = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameON = False
    

    if key[pygame.K_RETURN]:
        start_game = True
    
    if start_game:
        redrawGame()
    else:
        layar.blit(template,(0,0))
        layar.blit(modelpertama, (300,50))
        layar.blit(modelkedua, (200,230))
        layar.blit(modelketiga, (600,250))
        layar.blit(modelkeempat, (400,150))
        layar.blit(perintah, (400,300))
        layar.blit(versi, (450,350))
        layar.set_alpha(400)
        pygame.display.update()
    

pygame.quit()





