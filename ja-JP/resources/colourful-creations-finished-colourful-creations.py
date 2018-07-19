#!/bin/python3

from turtle import *
from time import *

# ディクショナリの紹介
# 人間が理解する色のキーとコンピューター向けのヘックスコード（値）をディクショナリに追加。ディクショナリを使って色を選ぶ。
colours = { 
  'space': '#060608', 
  'moongrey': '#BCBDEF', 
  'verylime': '#A7E30E', 
  'deepsea': '#226363', 
  'reallyraspberry': '#FA057F', 
  'gloomygrey': '#363332', 
  'awesomeorange':  '#F37C06', 
  'coolcyan': '#4FEEF6',
  'perfectpurple': '#6820B0',
  'lovelylemon': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['space'])

penup()
goto(0, 100)
color(colours['reallyraspberry'])
style = ('Arial', 40, 'bold')
write('こんにちは', font=style, align='center')
right(90)
forward(60)
color(colours['awesomeorange'])
write('みなさん', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['moongrey'])
dot(400)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['verylime'])
style=('Verdana', 20, 'bold')
write('ふつうの', font=style, align='center')
forward(40)
color(colours['reallyraspberry'])
write('スマートフォーン', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['deepsea'])
write('は', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['awesomeorange'])
write('アポロ１１', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['perfectpurple'])
write('が', font=style, align='center')
forward(40)
color(colours['coolcyan'])
write('月に', font=('Verdana', 25, 'bold'), align='center')
color(colours['lovelylemon'])
forward(40)
write('着陸したときの', font=style, align='center')
color(colours['gloomygrey'])
forward(40)
write('計算速度よりはやい', font=('Verdana', 18, 'bold'), align='center')
color('white')
forward(50)
write('ー　ギブズナンシー, 2012', font=('Arial', 10, 'normal'))
