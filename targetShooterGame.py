import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


bg_planks = pygame.image.load("Wood_BG.png")
land = pygame.image.load("Land_BG.png")
water = pygame.image.load("Water_BG.png")
cld1 = pygame.image.load("Cloud1.png")
cld2 = pygame.image.load("Cloud2.png")
crsH = pygame.image.load("crosshair.png")
duckSurf = pygame.image.load("duck.png")
game_font = pygame.font.Font(None, 50)
text_suface = game_font.render("YOU WON !", True, (255,255,255))
text2_surf = game_font.render("You have 25 seconds", True, (255,255,255))
text3_surf = game_font.render("Time UP !", True, (255,255,255))
land_pos_y = 550
land_spd = 1
water_pos_y = 640
water_spd = 1

duckL = []
rng = random.randint(10, 50)
for duck in range(rng):
    duck_pos_x = random.randrange(50, 1200)
    duck_pos_y = random.randrange(10, 550)
    duck_rect = duckSurf.get_rect(center = (duck_pos_x, duck_pos_y))
    duckL.append(duck_rect)
while True:
    crsH_rect = crsH.get_rect(center = pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index,duck_rect in enumerate(duckL):
                if duck_rect.collidepoint(event.pos):
                    del duckL[index]
            
            
           
    screen.blit(bg_planks, (0,0))
    text_rect = text_suface.get_rect(center = (600, 360))

    for duck_rect in duckL:
        screen.blit(duckSurf, duck_rect)
    
        
    land_pos_y -= land_spd
    
    if land_pos_y <= 540 or land_pos_y >= 600:
        land_spd *= -1
    screen.blit(land, (0,land_pos_y))
    
    water_pos_y += water_spd
    
    if water_pos_y <= 610 or water_pos_y >= 660:
        water_spd *= -1
    screen.blit(water, (0, water_pos_y))
    
    screen.blit(cld1, (20,50))
    screen.blit(cld2, (500,100))
    screen.blit(cld1, (300,300))
    screen.blit(cld2, (1000, 400))
    screen.blit(cld1, (600,250))
    screen.blit(cld2, (1100,200))
    if len(duckL) <= 0:
        screen.blit(text_suface, text_rect)
    screen.blit(crsH, crsH_rect) 
    
    pygame.display.update()
    clock.tick(300)