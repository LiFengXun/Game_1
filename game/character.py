import pygame
pygame.init()
jalankanan = [pygame.image.load("sprites/R12.png"),pygame.image.load("sprites/R13.png"),pygame.image.load("sprites/R14.png"),pygame.image.load("sprites/R15.png"),pygame.image.load("sprites/R16.png"),pygame.image.load("sprites/R11.png"),]
jalankiri = [pygame.image.load("sprites/L1.png"),pygame.image.load("sprites/L2.png"),pygame.image.load("sprites/L3.png"),pygame.image.load("sprites/L4.png"),pygame.image.load("sprites/L5.png"),pygame.image.load("sprites/L6.png"),]
latar_belakang = pygame.image.load("sprites/castle1.jpg")
melompat = [pygame.image.load("sprites/U4.png"),pygame.image.load("sprites/U1.png"),pygame.image.load("sprites/U2.png"),pygame.image.load("sprites/U3.png"),pygame.image.load("sprites/U5.png"),pygame.image.load("sprites/U5.png")]
melompat_kiri = [pygame.image.load("sprites/U14.png"),pygame.image.load("sprites/U11.png"),pygame.image.load("sprites/U12.png"),pygame.image.load("sprites/U13.png"),pygame.image.load("sprites/U15.png"),pygame.image.load("sprites/U15.png")]
tebasankiri= [pygame.image.load("sprites/S14.png"),pygame.image.load("sprites/S15.png"),pygame.image.load("sprites/S16.png"),pygame.image.load("sprites/S11.png"),pygame.image.load("sprites/S12.png"),pygame.image.load("sprites/S13.png")]
tebasan_kanan = [pygame.image.load("sprites/S4.png"),pygame.image.load("sprites/S5.png"),pygame.image.load("sprites/S6.png"),pygame.image.load("sprites/S1.png"),pygame.image.load("sprites/S2.png"),pygame.image.load("sprites/S3.png")]
diam = [pygame.image.load("sprites/diam.png")]
diam_kiri = [pygame.image.load("sprites/diamkiri.png")]
tebasan = [pygame.image.load("sprites/Tkanan.png")]
tebasan_kiri = [pygame.image.load("sprites/Tkiri.png")]
santai = [pygame.image.load("sprites/santai.png")]
santai_kiri = [pygame.image.load("sprites/santai_kiri.png")]

enemy = [pygame.image.load("sprites/MR1.png"),pygame.image.load("sprites/MR2.png"),pygame.image.load("sprites/MR3.png"),pygame.image.load("sprites/MR4.png"),pygame.image.load("sprites/MR5.png"),pygame.image.load("sprites/MR6.png")]
enemy1 = [pygame.image.load("sprites/ML1.png"),pygame.image.load("sprites/ML2.png"),pygame.image.load("sprites/ML3.png"),pygame.image.load("sprites/ML4.png"),pygame.image.load("sprites/ML5.png"),pygame.image.load("sprites/ML6.png")]

width_screen = 1000
height_screen = 600
layar = pygame.display.set_mode((width_screen,height_screen))

class Character(object):
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.vel = 5
        self.lompat = False
        self.jumlahlompat = 10
        self.left = False
        self.right = False
        self.jumlahjalan = 0
        self.melompat = 0
        self.jumlahmelompat = 0
        self.standing = True
        self.serang = False
        self.jumlahserang = 0
        self.hitbox = (self.x + 5,self.y, 40, 60)
        self.nyawa = 3
        self.gameover = False
        self.santai = False

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_SPACE]:
            self.serang = True
        else:
            self.serang = False

    def gambar(self,layar):
        if self.jumlahjalan + 1 >= 12:
            self.jumlahjalan = 0
        if self.jumlahmelompat + 1 >= 12:
            self.jumlahmelompat = 0
        if self.jumlahserang + 1 >= 12:
            self.jumlahserang = 0

        if not (self.standing):
            if self.right and self.lompat:
                layar.blit(melompat[self.jumlahmelompat // 2], (self.x, self.y))
                self.jumlahmelompat += 1

            elif self.serang:
                if self.left:
                    layar.blit(tebasankiri[self.jumlahserang // 2], (self.x, self.y))
                    self.jumlahserang += 1
                elif self.right:
                    layar.blit(tebasan_kanan[self.jumlahserang // 2], (self.x, self.y))
                    self.jumlahserang += 1

            elif self.left and self.lompat:
                layar.blit(melompat_kiri[self.jumlahmelompat // 2], (self.x, self.y))
                self.jumlahmelompat += 1
            
            elif self.left:
                layar.blit(jalankiri[self.jumlahjalan // 2], (self.x, self.y))
                self.jumlahjalan += 1

            elif self.right:
                layar.blit(jalankanan[self.jumlahjalan // 2], (self.x, self.y))
                self.jumlahjalan += 1
            
            elif self.lompat:
                layar.blit(melompat[self.jumlahmelompat // 2], (self.x, self.y))
                self.jumlahmelompat += 1
            elif self.santai:
                layar.blit(santai[0], (self.x, self.y+20))
            
        else:
            if self.right:
                layar.blit(diam[0], (self.x, self.y))
            elif self.left:
                layar.blit(diam_kiri[0], (self.x, self.y))
            
            elif self.lompat:
                layar.blit(melompat[self.jumlahmelompat // 2], (self.x, self.y))
                self.jumlahmelompat += 1
            elif self.santai:
                layar.blit(santai[0], (self.x, self.y+20))
            elif self.serang:
                layar.blit(tebasankiri[self.jumlahserang // 2], (self.x, self.y))
                self.jumlahserang += 1

        self.hitbox = (self.x+5,self.y, 40, 60)
    
    def tertonjok(self):
        self.x = 100
        self.y = 450
        self.lompat = False
        self.jumlahlompat = 10
        self.jumlahjalan = 0
        fontkata = pygame.font.Font("font/Pixeltype.ttf",80)
        kata = fontkata.render("-5",False,"Red")
        layar.blit(kata,(380,280))
        pygame.display.update()
        i = 0 
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        


class Pembaharuan(object):
    def __init__(self,x,y,radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def gambar(self,layar):
        if self.facing == -1:
            layar.blit(pygame.transform.flip(tebasan[0], True, False), (self.x, self.y-20))
        else:
            layar.blit(tebasan[0], (self.x, self.y-20))
        

class musuh(object):
    enemy = [pygame.image.load("sprites/MR1.png"),pygame.image.load("sprites/MR2.png"),pygame.image.load("sprites/MR3.png"),pygame.image.load("sprites/MR4.png"),pygame.image.load("sprites/MR5.png"),pygame.image.load("sprites/MR6.png")]
    enemy1 = [pygame.image.load("sprites/ML1.png"),pygame.image.load("sprites/ML2.png"),pygame.image.load("sprites/ML3.png"),pygame.image.load("sprites/ML4.png"),pygame.image.load("sprites/ML5.png"),pygame.image.load("sprites/ML6.png")]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.jumlahjalan = 0
        self.vel = 5
        self.hitbox = (self.x + 3, self.y, 40, 60)
        self.health = 1000
        self.visible = True

    
    def gambar(self,layar):
        self.move()
        if self.visible:
            if self.jumlahjalan + 1 >= 12:
                self.jumlahjalan = 0
            
            if self.vel > 0:
                layar.blit(self.enemy[self.jumlahjalan // 2], (self.x, self.y))
                self.jumlahjalan += 1
            else:
                layar.blit(self.enemy1[self.jumlahjalan // 2], (self.x, self.y))
                self.jumlahjalan += 1

            pygame.draw.rect(layar, (255,0,0) ,(self.hitbox[0], self.hitbox[1]-20, 50,10))
            pygame.draw.rect(layar, (0,128,0) ,(self.hitbox[0], self.hitbox[1]-20, (50 - (0.05 * (1000-self.health))) ,10))
            self.hitbox = (self.x +3, self.y + 10, 40, 60)
            

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.jumlahjalan = 0 
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.jumlahjalan = 0

    def tertebas(self):
        if self.health > 0:
            self.health -= 10
        else: 
            self.visible = False

    

        
        
        

