#!/bin/python3

from turtle import *
from time import *

# woordenboeken
# gebruik een kleurenkiezer om nieuwe kleuren te vinden en te kiezen
kleuren = { 
  'ruimte': '#060608', 
  'maangrijs': '#BCBDEF', 
  'erglimoen': '#A7E30E', 
  'diepzee': '#226363', 
  'echteframboos': '#FA057F', 
  'sombergrijs': '#363332', 
  'waanzinnigoranje':  '#F37C06', 
  'koelcyaan': '#4FEEF6',
  'perfectpaars': '#6820B0',
  'heerlijkecitroen': '#FBF312',
}

scherm = Screen()
scherm.setup(400, 400)
scherm.bgcolor(kleuren['ruimte'])

penup()
goto(0, 100)
color(kleuren['echteframboos'])
style = ('Arial', 40, 'bold')
write('HALLO', font=style, align='center')
right(90)
forward(60)
color(kleuren['waanzinnigoranje'])
write('WERELD', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(kleuren['maangrijs'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(kleuren['erglimoen'])
style=('Verdana', 20, 'bold')
write('Een gewone', font=style, align='center')
forward(40)
color(kleuren['echteframboos'])
write('smartphone', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(kleuren['diepzee'])
write('heeft meer', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(kleuren['waanzinnigoranje'])
write('rekenkracht', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(kleuren['perfectpaars'])
write('dan', font=style, align='center')
forward(40)
color(kleuren['koelcyaan'])
write('de Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(kleuren['heerlijkecitroen'])
forward(40)
write('toen die landde', font=style, align='center')
color(kleuren['sombergrijs'])
forward(40)
write('op de maan', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
