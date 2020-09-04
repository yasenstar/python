# coding = utf-8
'''
Created on Nov 25 2017
@author: Yasen
'''
from math import pi
from numpy import cos, sin
from matplotlib import pyplot as plt

if __name__ == '__main__':
    '''plot data margin'''
    angles_circle = [i*pi/180 for i in range(0,360)]    #i先转换成double
    # angles_circle = [i/np.pi for i in np.arange(0,360)]    # <=>
    # angles_circle = [i/180*pi for i in np.arange(0,360)]
    x = cos(angles_circle)
    y = sin(angles_circle)
    plt.plot(x,y,'r')

    plt.axis('equal')
    plt.axis('scaled')
    plt.show()