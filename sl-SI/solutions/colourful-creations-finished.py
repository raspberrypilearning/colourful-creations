#!/bin/python3

from turtle import *
from time import *

# uvedi slovarje
# za iskanje in izbiro barv uporabi iskalnik barv
barve = { 
  'vesolje': '#060608', 
  'sivmesec': '#BCBDEF', 
  'kislalimeta': '#A7E30E', 
  'globokomorje': '#226363', 
  'zrelamalina': '#FA057F', 
  'sivosiva': '#363332', 
  'krasnooranžna':  '#F37C06', 
  'kulskomodra': '#4FEEF6',
  'popolnovijolična': '#6820B0',
  'ljubkalimona': '#FBF312',
}

zaslon = Screen()
zaslon.setup(400, 400)
zaslon.bgcolor(colours['vesolje'])

penup()
goto(0, 100)
color(barve['zrelamalina'])
stil = ('Arial', 40, 'bold')
write('POZDRAVLJEN', font=stil, align='center')
right(90)
forward(60)
color(barve['krasnooranžna'])
write('SVET', font=stil, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(barve['sivmesec'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(barve['kislalimeta'])
stil=('Verdana', 20, 'bold')
write('Tipični', font=stil, align='center')
forward(40)
color(barve['zrelamalina'])
write('pametni telefon', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(barve['globokomorje'])
write('ima bolj', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(barve['krasnooranžna'])
write('zmogljiv procesor, ', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(barve['popolnovijolična'])
write('kot', font=stil, align='center')
forward(40)
color(barve['kulskomodra'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(barve['ljubkalimona'])
forward(40)
write('ko je pristal na', font=stil, align='center')
color(barve['sivosiva'])
forward(40)
write('luni', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
