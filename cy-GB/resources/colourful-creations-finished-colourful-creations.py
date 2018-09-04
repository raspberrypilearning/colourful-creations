#!/bin/python3

from turtle import *
from time import *

# cyflwynwch eiriaduron
# defnyddiwch ddewisydd lliw i ddarganfod a dewis lliwiau newydd
lliwiau = { 
  'bwlch': '#060608', 
  'llwydlleuad': '#BCBDEF', 
  'leimiawn': '#A7E30E', 
  'môrdwfn': '#226363', 
  'mafongoiawn': '#FA057F', 
  'llwydtywyll': '#363332', 
  'orenanhygoel':  '#F37C06', 
  'gwyrddlascŵl': '#4FEEF6',
  'porfforperffaith': '#6820B0',
  'lemonhyfryd': '#FBF312',
}

sgrin = Screen()
sgrin.setup(400, 400)
sgrin.bgcolor(lliwiau['gofod'])

penup()
goto(0, 100)
color(lliwiau['mafongoiawn'])
arddull = ('Arial', 40, 'bold')
write('HELO', font=arddull, align='center')
right(90)
forward(60)
color(lliwiau['orenanhygoel'])
write('BYD', font=arddull, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(lliwiau['llwydlleuad'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(lliwiau['leimiawn'])
arddull=('Verdana', 20, 'bold')
write('Mae gan', font=arddull, align='center')
forward(40)
color(lliwiau['mafongoiawn'])
write('ffôn clyfar', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(lliwiau['môrdwfn'])
write('nodweddiadol', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(lliwiau['orenanhygoel'])
write('fwy o bŵer', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(lliwiau['porfforperffaith'])
write('cyfrifiaduro nac', font=arddull, align='center')
forward(40)
color(lliwiau['gwyrddlascŵl'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(lliwiau['lemonhyfryd'])
forward(40)
write('pan laniodd ar', font=arddull, align='center')
color(lliwiau['llwydtywyll'])
forward(40)
write('y lleuad', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
