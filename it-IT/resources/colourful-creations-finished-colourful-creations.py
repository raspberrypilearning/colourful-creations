#!/bin/python3

from turtle import *
from time import *

# apre i dizionari
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
screen.bgcolor(colours['spazio'])

penup()
goto(0, 100)
color(colours['moltolampone'])
style = ('Arial', 40, 'bold')
write('CIAO', font=style, align='center')
right(90)
forward(60)
color(colours['moltoarancio'])
write('MONDO', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['grigioluna'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['superlime'])
style=('Verdana', 20, 'bold')
write('Un normale', font=style, align='center')
forward(40)
color(colours['moltolampone'])
write('smartphone', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['mareblu'])
write('ha più', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['moltoarancio'])
write('potenza di calcolo', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['violaveleno'])
write('dell'', font=style, align='center')
forward(40)
color(colours['azzurroghiaccio'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colours['giallolimone'])
forward(40)
write('che è atterrato', font=style, align='center')
color(colours['grigrioluna'])
forward(40)
write('sulla luna', font=('Verdana', 25, 'bold'), align='center')
color('bianco')
forward(50)
write('Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
