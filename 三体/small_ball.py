# learn from https://blog.csdn.net/qq_37963615/article/details/98514615
# date: 2020-09-05

# 导入pygame
import pygame
import os

# 创建pygame窗体

# 定义必要的全局变量
WINDOW_W, WINDOW_H = 640, 480    # 窗体尺寸
FPS = 50    # 显示帧频，即每秒刷新多少次
g = round(9.8 * 100  / 1, 2)  # 重力加速度 （此处用的单位是像素每二次方秒）
# g为可以调整的加速度， 1 - 地球标准， 1/6 - 月球

# 创建窗体
pygame.init()    # 初始化pygame
# 设置窗口出现的位置
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200,100)
# 创建一个窗口
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
# 设置窗口标题
text = "小球弹跳，Hello World! 加速度=" + str(g)
pygame.display.set_caption(text)
# 创建时钟对象（可以用来控制循环频率）
clock = pygame.time.Clock()

####### 窗体的 set_mode(resolution(0,0),flags=0,depth=0) #######
#  resolution: 窗体的宽和高
#  flags： 附件选项的集合
#    pygame.FULLSCREEN  全屏显示
#    pygame.DOUBLEBUF   双缓冲模式（推荐和 HWSURFACE 或 OPENGL 一起使用）
#    pygame.HWSURFACE   硬件加速，只有在 FULLSCREEN 下可以使用
#    pygame.OPENGL      创建一个 OPENGL 渲染的显示
#    pygame.RESIZABLE   创建一个可以调整尺寸的窗口
#    pygame.NOFRAME     创建一个没有边框和控制按钮的窗口
#  depth： 使用的颜色深度
###################################################################

# 游戏主循环
if __name__ == '__main__':
    x, y = WINDOW_W/2, 10    # 球的坐标
    vx, vy = 0, 0    # 球在 x, y 方向上的速度
    # 游戏主循环
    while True:
        # 遍历事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接收到退出事件后退出程序
                exit()
        
        # 小球下一个时刻的速度、位置计算
        vy += g * 1 / FPS
        x += vx * 1 / FPS
        y += vy * 1 / FPS
        if y>= WINDOW_H - 10:
            # 到达地面则是其竖直速度反向
            vy = -vy
        
        # 将背景图画上去 (0,0,0) 为RGB颜色
        screen.fill((0,0,0))
        # 根据球的坐标画图
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 10)

        # 刷新画面
        pygame.display.update()

        # 设置FPS
        time_passed = clock.tick(FPS)

input()    # 确保最后窗口等待敲击键盘退出