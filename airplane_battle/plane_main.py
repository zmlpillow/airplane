import pygame
from plane_sprite import  *

SCREEN_RECT = pygame.Rect(0,0,480,700)

class PlaneGame(object):
    '''飞机大战主游戏'''
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #　设置游戏时钟
        self.clock = pygame.time.Clock()
        # 设置游戏的精灵
        self.__create_sprite()
        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
    def __create_sprite(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print('游戏开始')
        while True:
            # 1 设置刷新帧率
            self.clock.tick(60)
            # 2 事件检测
            self.__event_handle()
            # 3 碰撞检测
            self.__check_collide()
            # 4　加入精灵
            self.__update_sprites()
            # 5 更新显示
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4

        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -4

        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies) > 0:
            self.hero.kill()
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()

if __name__ == '__main__':
    plane_game = PlaneGame()
    plane_game.start_game()