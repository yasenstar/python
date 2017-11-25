import math
print('有关圆的计算-周长，面积与球的体积')

print('请选择要进行的计算')
print('1 - 周长')
print('2 - 面积')
print('3 - 体积')

type = int(input())

print('请输入圆的周长')
r = float(input())

圆的周长 = '圆的周长 = 2 x PI x 半径'
圆的面积 = '圆的面积 = PI x 半径的平方'
圆的体积 = '球的体积 = 4/3 x PI x 半径的立方'

print('============打印输出===================')

print('你输入的圆的半径是： ',r)

if type == 1:
    print('计算圆的周长')
    circle_length = 2 * math.pi * r
    print(circle_length)
elif type == 2:
    print('计算圆的面积')
    circle_area = math.pi * math.pow(r,2)
    print(circle_area)
elif type == 3:
    print('计算球的体积')
    ball_volume = 4 / 3 * math.pi * math.pow(r,3)
    print(ball_volume)
else:
    print('选择错误')
    quit()



