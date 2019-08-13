#!/bin/python3

from turtle import *
from time import *

# introdurre i dizionari
# usa lo strumento di selezione per trovare nuovi colori
colori = { 
  'spazio': '#060608', 
  'grigioluna': '#BCBDEF', 
  'superlime': '#A7E30E', 
  'mareblu': '#226363', 
  'moltolampone': '#FA057F', 
  'grigiocupo': '#363332', 
  'moltoarancio':  '#F37C06', 
  'azzurroghiaccio': '#4FEEF6',
  'violaveleno': '#6820B0',
  'giallolimone': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor (colori [ 'spazio'])

penup()
goto(0, 100)
color(colori['moltolampone'])
style = ('Arial', 40, 'bold')
write('CIAO', font=style, align='center')
right(90)
forward(60)
color(colori['moltoarancio'])
write('MONDO', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colori['grigioluna'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colori['moltolampone'])
style=('Verdana', 20, 'bold')
write('Un normale', font=style, align='center')
forward(40)
color(colori['moltolampone'])
write('smartphone', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colori['mareblu'])
write('ha più', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colori['moltoarancio'])
write('potenza di calcolo', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colori['violaveleno'])
write('dell\'', font=style, align='center')
forward(40)
color(colori['azzurroghiaccio'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colori['giallolimone'])
forward(40)
write('che è atterrato', font=style, align='center')
color(colori['grigiocupo'])
forward(40)
write('sulla luna', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
