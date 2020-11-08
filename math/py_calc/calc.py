# - *- coding: utf- 8 - *-#
import tkinter
TK_SILENCE_DEPRECATION = 1

root  = tkinter.Tk()
root.minsize(280, 500)
root.title('计算器测试')

# 显示面板
panel = tkinter.StringVar()
panel.set(0)
panel_history = tkinter.StringVar()
panel_history.set('欢迎使用')

# 显示版
font = 'Comic Sans MS'
label = tkinter.Label(root, font = (font,30), bg = '#EEE9E9', bd = '9', fg = '#828282', anchor = 'se', textvariable = panel_history)
label.place(width = 280, height = 170)
label2 = tkinter.Label(root, font = (font,50), bg = '#EEE9E9', bd = '9', fg = 'black', anchor = 'se', textvariable = panel)
label.place(width = 170, height = 60)

# 数字
num_fg = '#4F4F4F'
btn7 = tkinter.Button(root, text = '7', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('7'))
btn7.place(x = 0, y = 285, width = 65, height = 50)
btn8 = tkinter.Button(root, text = '8', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('8'))
btn8.place(x = 70, y = 285, width = 65, height = 50)
btn9 = tkinter.Button(root, text = '9', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('9'))
btn9.place(x = 140, y = 285, width = 65, height = 50)
btn4 = tkinter.Button(root, text = '4', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('4'))
btn4.place(x = 0, y = 340, width = 65, height = 50)
btn5 = tkinter.Button(root, text = '5', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('5'))
btn5.place(x = 70, y = 340, width = 65, height = 50)
btn6 = tkinter.Button(root, text = '6', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('6'))
btn6.place(x = 140, y = 340, width = 65, height = 50)
btn1 = tkinter.Button(root, text = '1', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('1'))
btn1.place(x = 0, y = 395, width = 65, height = 50)
btn2 = tkinter.Button(root, text = '2', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('2'))
btn2.place(x = 70, y = 395, width = 65, height = 50)
btn3 = tkinter.Button(root, text = '3', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('3'))
btn3.place(x = 140, y = 395, width = 65, height = 50)
btn0 = tkinter.Button(root, text = '0', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : number('0'))
btn0.place(x = 70, y = 450, width = 65, height = 50)

# 运算符
btnac = tkinter.Button(root, text = 'AC', bd = 0.5, font = (font,18), bg = 'orange', command = lambda : compute('AC'))
btnac.place(x = 0, y = 230, width = 65, height = 50)

btnback = tkinter.Button(root, text = '<-', font = (font,20), fg = num_fg, bd = 0.5, command = lambda : compute('b'))
btnback.place(x = 70, y = 230, width = 65, height = 50)

btndivi = tkinter.Button(root, text = '/', font = (font,20), fg = num_fg, bd = 0.5, command = lambda : compute('/'))
btndivi.place(x = 140, y = 230, width = 65, height = 50)

btnmul = tkinter.Button(root, text = '*', font = (font,20), bd = 0.5, command = lambda : compute('*'))
btnmul.place(x = 210, y = 230, width = 65, height = 50)

btnsub = tkinter.Button(root, text = '-', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : compute('-'))
btnsub.place(x = 210, y = 285, width = 65, height = 50)

btnadd = tkinter.Button(root, text = '+', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : compute('+'))
btnadd.place(x = 210, y = 340, width = 65, height = 50)

btnequ = tkinter.Button(root, text = '=', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : equal())
btnequ.place(x = 210, y = 395, width = 65, height = 50)

btnper = tkinter.Button(root, text = '%', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : compute('%'))
btnper.place(x = 0, y = 450, width = 65, height = 50)

btnpoint = tkinter.Button(root, text = '.', font = (font,20), fg = (num_fg), bd = 0.5, command = lambda : compute('.'))
btnpoint.place(x = 140, y = 450, width = 65, height = 50)

# 计算函数
lists = []
isPressSign = False
isPressNum = False
def number(num):
    global lists
    global isPressSign
    if isPressSign == False:
        pass
    else:
        panel.set(0)
        isPressSign = False
    oldnum = panel.get()
    if oldnum =='0':
        panel.set(num)
    else:
        newnum = oldnum + num
        panel.set(newnum)
def compute(sign):
    global lists
    global isPressSign
    num = panel.get()
    lists.append(num)
    lists.append(sign)
    isPressSign = True
    if sign == 'AC':
        lists.clear()
        panel.set(0)
    if sign =='b':
        a = num[0:-1]
        lists.clear()
        panel.set()
def equal():
    global lists
    global isPressSign
    curnum = panel.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = eval(computrStr)
    panel.set(endNum)
    panel_history.set(computrStr)
    lists.clear()
root.mainloop()