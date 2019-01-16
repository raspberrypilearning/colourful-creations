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
  '真正树莓': '#FA057F', 
  '阴沉灰': '#363332', 
  '漂亮的橙色':  '#F37C06', 
  '酷青': '#4FEEF6',
  '完美紫': '#6820B0',
  '可爱的柠檬': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['太空'])

penup()
goto(0, 100)
color(colours['真正树莓'])
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')
right(90)
forward(60)
color(colours['漂亮的橙色'])
write('WORLD', font=style, align='center')
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
write('A typical', font=style, align='center')
forward(40)
color(colours['真正树莓'])
write('smart phone', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['深海'])
write('has more', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['漂亮的橙色'])
write('computing power', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['完美紫'])
write('than', font=style, align='center')
forward(40)
color(colours['酷青'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colours['可爱的柠檬'])
forward(40)
write('when it landed on', font=style, align='center')
color(colours['阴沉灰'])
forward(40)
write('the moon', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
