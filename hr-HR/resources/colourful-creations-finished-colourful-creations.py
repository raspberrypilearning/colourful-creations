#!/bin/python3

from turtle import *
from time import *

# uvodenje rjecnika
# pomocu alata za odabir boje pronadi i odaberi nove boje
boje = { 
  'svemirska': '#060608', 
  'mjesecsiva': '#BCBDEF', 
  'kricavozelena': '#A7E30E', 
  'morskoplava': '#226363', 
  'jakoruzicasta': '#FA057F', 
  'ekstrasiva': '#363332', 
  'supernarancasta':  '#F37C06', 
  'kulplava': '#4FEEF6',
  'savrsenaljubicasta': '#6820B0',
  'slatkozuta': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(boje['svemirska'])

penup()
goto(0, 100)
color(boje['jakoruzicasta'])
style = ('Arial', 40, 'bold')
write('BOK', font=style, align='center')
right(90)
forward(60)
color(boje['supernarancasta'])
write('SVIMA', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(boje['mjesecsiva'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(boje['kricavozelena'])
style=('Verdana', 20, 'bold')
write('Obican', font=style, align='center')
forward(40)
color(boje['jakoruzicasta'])
write('pametni telefon', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(boje['morskoplava'])
write('ima vise', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(boje['supernarancasta'])
write('racunalne snage', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(boje['savrsenaljubicasta'])
write('nego', font=style, align='center')
forward(40)
color(boje['kulplava'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(boje['slatkozuta'])
forward(40)
write('kada je sletio na', font=style, align='center')
color(boje['ekstrasiva'])
forward(40)
write('Mjesec', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
