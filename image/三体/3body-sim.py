# 三体运动：三个质量相差不大的天体相互作用下的运动
# 2020-09-05

# 定义一些常量和初始化

from sys import exit
import pygame, math
from pygame.color import *

G     = 900  # 重力加速度，即重力常量
FPS   = 50   # 帧率
exact = 50   # 每帧计算几次，次数越多越精确，它是动态变化的

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((1024,768), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("模拟三体")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 16)

# 定义星球类
class Star():
    x, y = 0, 0  # 坐标
    vx, vy = 0, 0  # x,y方向上的速度
    ax, ay = 0, 0  # x,y方向上的加速度
    m = 0  # 质量
    r = 20  # 半径

    def __init__(self, x, y, vx, vy, m):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m
    
    def set_a(self, other_star):
        '''
        计算star与other_star之间的重力加速度
        '''
        d_2 = (self.x - other_star.x) ** 2 + (self.y - other_star.y) ** 2
        _x = [-1, 1][self.x < other_star.x]
        _y = [-1, 1][self.y < other_star.y]
        if d_2 != 0:
            a = G * self.m * other_star.m / d_2
        else:
            a = 0
        if self.x != other_star.x:
            ax_ = math.sqrt(a ** 2 / (((self.y - other_star.y) / (self.x - other_star.x)) ** 2 +1 ))
            self.ax += ax_ * _x
            self.ay += math.sqrt(a ** 2 - ax_ ** 2) * _y
        else:
            self.ay += a * _y
        
    def run(self, time):
        '''
        计算time时间后的位置
        :param time: 时间， 秒
        :return:
        '''
        self.ax /= (self.m * 2)
        self.ay /= self.m
        self.vx += self.ax * time * 10
        self.vy += self.ay * time
        self.x += self.vx * time
        self.y += self.vy * time

# 设置三个星球
star_list = []
dd = 0.00001
star_list.append(Star(200, 300, -30, -math.sqrt(3)*30, 1000))
star_list.append(Star(400, 300, -30, math.sqrt(3)*30, 1000))
star_list.append(Star(300, 300-math.sqrt(3)*100+dd, 60, 0, 1000))
""" star_list.append(Star(500, 300-math.sqrt(3)*100+dd, 60, 0, 1000))
star_list.append(Star(100, 300, -30, -math.sqrt(3)*30, 1000))
star_list.append(Star(300, 300, -30, math.sqrt(3)*30, 1000))
star_list.append(Star(600, 300-math.sqrt(3)*100+dd, 60, 0, 1000))
star_list.append(Star(350, 300-math.sqrt(3)*100+dd, 60, 0, 1000)) """

# 主循环
# 计算引力加速度
def set_a(star_list):
    for i, star in enumerate(star_list):
        star.ax, star.ay = 0, 0
        for j, other_star in enumerate(star_list):
            if i != j:
                star.set_a(other_star)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出时间后退出程序
            exit()

    for i in range(exact):
        set_a(star_list)
        for star in star_list:
            star.run(1 / FPS / exact)
    # 将背景图画上去
    screen.fill((0, 0, 0))
    max_v = 0
    for star in star_list:
        max_v = max(max_v, math.sqrt(star.vx**2+star.vy**2))
        pygame.draw.circle(screen, (255, 0, 0), (int(star.x), int(star.y)), star.r)
    exact = min(300,max(30,int(max_v)))*5
    screen.blit(font.render("fps: " + str(clock.get_fps()), 1, THECOLORS["white"]), (0,0))
    screen.blit(font.render("exact: " + str(exact), 1, THECOLORS["white"]), (0,15))

    # 刷新画面
    pygame.display.update()
    time_passed = clock.tick(FPS)

input()