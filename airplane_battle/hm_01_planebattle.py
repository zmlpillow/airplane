import  pygame
from plane_sprite import *

pygame.init()
# 创建一个游戏窗口
screen = pygame.display.set_mode((480,700))
#　加载游戏背景
# 1 导入图片,加载背景
bg = pygame.image.load('./images/background.png')
screen.blit(bg,(0,0))
#　２　加载英雄到屏幕
hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(150,300))
# ３　刷新
pygame.display.update()

#　设置时钟
clock = pygame.time.Clock()

enemy = GameSprite('./images/enemy1.png')
enemy_group = pygame.sprite.Group(enemy)


hero_rect = pygame.Rect(150,300,102,126)
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
    hero_rect.y -= 1
    if hero_rect.y<= -126:
        hero_rect.y = 700
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    pass

pygame.quit()