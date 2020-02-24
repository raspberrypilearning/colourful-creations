#!/bin/python3

from turtle import *
from time import *

# 辞書の紹介
＃カラーピッカーを使用して新しい色を見つけて選択する
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
write('ハロー', font=style, align='center')
right(90)
forward(60)
color(colours['awesomeorange'])
write('ワールド', font=style, align='center')
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
write('一般的な', font=style, align='center')
forward(40)
color(colours['reallyraspberry'])
write('スマートフォーンは', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['deepsea'])
write('月に', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['awesomeorange'])
write('着陸した', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['perfectpurple'])
write('アポロ１１号', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['coolcyan'])
write('よりも', font=style, align='center')
color(colours['lovelylemon'])
forward(40)
write('計算能力が', font=('Verdana', 25, 'bold'), align='center')
color(colours['gloomygrey'])
forward(40)
write('高い', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
