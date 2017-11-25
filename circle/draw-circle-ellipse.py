# coding = utf-8
# !/usr/bin/env python
# __author__ = "yasen"
# 绘制椭圆与圆形
# learning from https://zhidao.baidu.com/question/431659650877344124.html

from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

elll = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor = 'yellow', alpha = 0.3)
cirl = Circle(xy = (0.0, 0.0), radius = 2, alpha = 0.5)
ax.add_patch(elll)
ax.add_patch(cirl)

x,y = 0,0
ax.plot(x, y, 'ro')

plt.axis('scaled')
# ax.set_xlim(-4,4)
# ax.set_ylim(-4,4)
plt.axis('equal') # changes limits of x or y axis so that equal increments of x and y have the same length

plt.show()