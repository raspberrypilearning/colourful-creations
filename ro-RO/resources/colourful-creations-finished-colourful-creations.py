#!/bin/python3

from turtle import *
from time import *

# introdu dictionarele
# foloseste un selector de culori pentru a alege culori noi
culori = { 
  'spatiu': '#060608', 
  'griLuna': '#BCBDEF', 
  'foarteLime': '#A7E30E', 
  'adanculOceanului': '#226363', 
  'chiarMagenta': '#FA057F', 
  'griSumbru': '#363332', 
  'portocaliuMisto':  '#F37C06', 
  'albastruVerzui': '#4FEEF6',
  'movulPerfect': '#6820B0',
  'lamaieDraguta': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(culori['spatiu'])

penup()
goto(0, 100)
color(culori['chiarMagenta'])
style = ('Arial', 40, 'bold')
write('SALUT', font=style, align='center')
right(90)
forward(60)
color(culori['portocaliuMisto'])
write('LUME', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(culori['griLuna'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(culori['foarteLime'])
style=('Verdana', 20, 'bold')
write('Un telefon', font=style, align='center')
forward(40)
color(culori['chiarMagenta'])
write('obișnuit', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(culori['adanculOceanului'])
write('are mai multă', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(culori['portocaliuMisto'])
write('putere', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(culori['movulPerfect'])
write('decât', font=style, align='center')
forward(40)
color(culori['albastruVerzui'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(culori['lamaieDraguta'])
forward(40)
write('atunci când a ajuns', font=style, align='center')
color(culori['griSumbru'])
forward(40)
write('pe lună', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
