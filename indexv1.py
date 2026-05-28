import pygame, random,os
pygame.init()
screen = pygame.display.set_mode((800,800))
run = True

background = pygame.image.load("Pro_Game_Dev/recycle_marathon/images/background.png")
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pro_Game_Dev/recycle_marathon/images/bin.png")
        self.image = pygame.transform.scale(self.image,(50,80))
        # This get all the properties of a rectangle of the image
        self.rect = self.image.get_rect()
class Recyclable(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(30,60))
        self.rect = self.image.get_rect()
class Non_recylable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pro_Game_Dev/recycle_marathon/images/plastic_bag.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()

images = ["Pro_Game_Dev/recycle_marathon/images/box.png","Pro_Game_Dev/recycle_marathon/images/paper_bag.png","Pro_Game_Dev/recycle_marathon/images/pencil.png"]
recycle = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
non_recylable = pygame.sprite.Group()
bin = Bin()
all_sprites.add(bin)
bin.rect.x = 350
bin.rect.y = 10

for i in range(30):
    item = Recyclable(random.choice(images))
    item.rect.x = random.randint(50,750)
    item.rect.y = random.randint(50,750)
    recycle.add(item)
    all_sprites.add(item)

for i in range(20):
    item = Non_recylable()
    item.rect.x = random.randint(50,750)
    item.rect.y = random.randint(50,750)
    non_recylable.add(item)
    all_sprites.add(item)

def bin_move(keypress):
    if keypress[pygame.K_UP]:
        bin.rect.y -= 13
    elif keypress[pygame.K_DOWN]:
        bin.rect.y += 13
    elif keypress[pygame.K_LEFT]:
        bin.rect.x -= 13
    elif keypress[pygame.K_RIGHT]:
        bin.rect.x += 13

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        keypress = pygame.key.get_pressed()
        bin_move(keypress)
    
        non_recylable_list = pygame.sprite.spritecollide(bin,non_recylable,True)
        # for i in non_recylable_list:
        recyclable_list = pygame.sprite.spritecollide(bin,recycle,True)
            
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    pygame.display.update()
