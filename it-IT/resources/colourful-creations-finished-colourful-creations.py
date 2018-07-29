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
style = ('Arial', 40, 'grassetto')
write('CIAO', font=style, align='centrato')
right(90)
forward(60)
color(colours['moltoarancio'])
write('MONDO', font=style, align='centrato')
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
style=('Verdana', 20, 'grassetto')
write('Un normale', font=style, align='centrato')
forward(40)
color(colours['moltolampone'])
write('smartphone', font=('Verdana', 25, 'grassetto'), align='centrato')
forward(40)
color(colours['mareblu'])
write('ha più', font=('Verdana', 18, 'grassetto'), align='centrato')
forward(40)
color(colours['moltoarancio'])
write('potenza di calcolo', font=('Verdana', 25, 'grassetto'), align='centrato')
forward(40)
color(colours['violaveleno'])
write('dell'', font=style, align='centrato')
forward(40)
color(colours['azzurroghiaccio'])
write('Apollo 11', font=('Verdana', 25, 'grassetto'), align='centrato')
color(colours['giallolimone'])
forward(40)
write('che è atterrato', font=style, align='centrato')
color(colours['grigrioluna'])
forward(40)
write('sulla luna', font=('Verdana', 25, 'grassetto'), align='centrato')
color('bianco')
forward(50)
write('Nancy Gibbs, 2012', font=('Arial', 14, 'normale'))
