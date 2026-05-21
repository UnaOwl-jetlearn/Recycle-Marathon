import pygame, random
pygame.init()
screen = pygame.display.set_mode((800,800))
run = True

background = pygame.image.load("recycle_marathon/images/background.png")
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recycle_marathon/images/bin.png")
        self.image = pygame.transform.scale(self.image,(50,80))
        # This get all the properties of a rectangle of the image
        self.rect = self.image.get_rect()
class Recyclable(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(30,60))
        self.rect = self.image.get_rect()

images = ["recycle_marathon/images/box.png","recycle_marathon/images/paper_bag.png","recycle_marathon/images/pencil.png"]
recycle = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
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

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    pygame.display.update()

