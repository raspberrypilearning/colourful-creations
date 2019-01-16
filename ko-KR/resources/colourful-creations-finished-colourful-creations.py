#!/bin/python3

from turtle import *
from time import *

# 사전 소개
# 색상 선택 도구를 사용하여 새로운 색상을 찾고 선택하십시오.
colours = { 
  '우주색': '#060608', 
  '달빛회색': '#BCBDEF', 
  '매우라임색': '# A7E30E', 
  '깊은바다색': '# 226363', 
  '진짜딸기색': '# FA057F', 
  '우울한회색': '# 363332', 
  '굉장한오렌지색': '# F37C06', 
  '시원한옥색': '# 4FEEF6',
  '완벽한보라색': '# 6820B0',
  '사랑스러운레몬색': '# FBF312',
}

screen = Screen ()
screen.setup (400, 400)
screen.bgcolor(colours['매우라임색'])

penup ()
goto(0, 100)
color(colours['진짜딸기색'])
style = ('Arial', 40, 'bold')
write('안녕', font=style, align='center')
right(90)
forward(60)
color(colours['굉장한오렌지색'])
write('WORLD', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['달빛회색'])
dot(350)

screen.bgcolor(colours['우주색'])
setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['매우라임색'])
style=('Verdana', 20, 'bold')
write('전형적인', font=style, align='center')
forward(40)
color(colours['진짜딸기색'])
write('스마트폰', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['시원한옥색'])
write('더 많은', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['굉장한오렌지색'])
write('컴퓨팅 파워', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['완벽한보라색'])
write('보다', font=style, align='center')
forward(40)
color(colours['시원한옥색'])
write('아폴로11', font=('Verdana', 25, 'bold'), align='center')
color(colours['사랑스러운레몬색'])
forward(40)
write('착륙했을 때', font=style, align='center')
color(colours['우울한회색'])
forward(40)
write('달', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
