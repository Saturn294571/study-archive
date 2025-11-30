# student = {
#     'a' : 213,
#     "g" : 312
# }
# student['ccc'] = 123

# print(student)

# print(student.keys())

# print(student.items())

# print(student.get('a'))

# s = 'kronii is tae yoon kim'

# print(s[8:])
# print(s[:-8])

# print(s.replace('kim','ouro'))

# s1 = '        kronii is my ohsi         '

# print(s1.strip())

# print(s1.find('kronii'))

# print(s1.count('i'))

# print(s.split(' '))

# ==============================

# import turtle as t

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.right(90)

# t.up()
# t.forward(100)
# t.down()

# t.fillcolor('yellow')
# t.begin_fill()
# t.circle(40)
# t.end_fill()

# print(dir(t))

# =================================

from tkinter import *

# window = Tk()
# counter = 0

# def onB1Clicked() :
#     global counter
#     global lbtext
#     counter += 1
#     print('버튼 클릭됨')
#     label['text']
    
# lbtext = '버튼 클릭됨' + str(counter)
# label = Label(window, text=lbtext)
# label.pack()

# # button = Button(window, text="클릭!",bg='yellow',fg='blue', width=80,height=2)
# button = Button(window, text='클릭!', command=onB1Clicked)
# button.pack()

# window = Tk()

# e = Entry(window)
# e.pack()
# print(help(e.pack()))

# window.mainloop()
# ====================================
# class counter :
#     def __init__(self):
#         self.count = 0
    
#     def plus(self) :
#         self.count += 1

# ================================

# file = open('C:\\Users\\shehd\\OneDrive\\바탕 화면\\pong_game\\aaa.txt', 'r', encoding='UTF8')
# lines = file.readlines()

# print(lines)
# file.close()

# file = open('C:\\Users\\shehd\\OneDrive\\바탕 화면\\pong_game\\aaa.txt', 'w', encoding='UTF8')
# file.write('adffsdafdsadfasafdsdsafasdfsdafd\n')
# file.close()

# =================================

# import numpy as np
# np_hei = np.array([3,4,1,4,2])
# np_arr = np.array([1,3,5,7,9])

import pandas as pd
data = [1,2,3,4,5]
mydata = {
    '오' : 1,
    '로' : 3,
    '크' : 5,
    '로' : 7,
    '니' : 9
}

a = pd.Series(mydata)
print(a[a == 9])

datas = {
    'name' : ['a','b','c'],
    'dept' : ['s','p','q']
}

df = pd.DataFrame(datas)
df.loc[3] = ['1','q']
print(df)