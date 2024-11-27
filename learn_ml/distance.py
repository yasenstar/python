# learning machine learning
from numpy import *
import numpy as np

vector1 = mat([2.1, 2.5, 3.8])
vector2 = mat([1.0, 1.7, 6.6])

# 曼哈顿距离
print(sum(abs(vector1 - vector2)))
# 欧式距离
print(sqrt((vector1-vector2)*(vector1-vector2).T))
# 闵可夫斯基距离
print(abs(vector1-vector2).max)
# 夹角余弦
print(vector1.dot(vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))