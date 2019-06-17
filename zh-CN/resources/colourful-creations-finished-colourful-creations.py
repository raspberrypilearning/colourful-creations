#!/bin/python3

from turtle import *
from time import *

# 介绍字典
# 使用颜色选择器查找并选择新颜色
colours = { 
  '太空': '#060608', 
  '月亮灰': '#BCBDEF', 
  '非常青柠': '#A7E30E', 
  '深海': '#226363', 
  '真是树莓': '# FA057F', 
  '阴沉灰': '#363332', 
  '魅力橙':  '#F37C06', 
  '炫酷青': '#4FEEF6',
  '完美紫': '#6820B0',
  '可爱柠檬': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['太空'])

penup()
goto(0, 100)
color(colours['真是树莓'])
style = ('Arial', 40, 'bold')
write('你好', font=style, align='center')
right(90)
forward(60)
color(colours['魅力橙'])
write('世界', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['月亮灰'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['非常青柠'])
style=('Verdana', 20, 'bold')
write('一部典型的', font=style, align='center')
forward(40)
color(colours['真是树莓'])
write('智能手机', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['深海'])
write('比', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['魅力橙'])
write('着陆在', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['完美紫'])
write('月球上的', font=style, align='center')
forward(40)
color(colours['炫酷青'])
write('阿波罗11号', font=('Verdana', 25, 'bold'), align='center')
color(colours['可爱柠檬'])
forward(40)
write('拥有更强大的', font=style, align='center')
color(colours['阴沉灰'])
forward(40)
write('计算能力', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- 南希·吉布斯, 2012', font=('Arial', 14, 'normal'))
