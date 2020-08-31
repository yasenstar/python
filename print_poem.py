# -*- coding: utf-8 -*-
"""
Spyder Editor

print poem
"""

def print_verse(time, author=None):
    # 唐诗
    print(author)
    if author=='李白':
        print("朝代：{0}，作者：{1}".format(time,author))
        print("床前明月光")
        print("疑是地上霜")
        print("举头望明月")
        print("低头思故乡")
        return 1
    else:
        print("author should be 李白")
        return 0
    
print_verse('唐代','李白')

