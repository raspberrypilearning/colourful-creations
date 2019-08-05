#!/bin/python3

from turtle import *
from time import *

# introduction aux dictionnaires
# utilise un sélecteur de couleur pour trouver et choisir de nouvelles couleurs
couleurs = { 
  'espace': '#060608', 
  'grislune': '#BCBDEF', 
  'citronvert': '#A7E30E', 
  'profondeurs': '#226363', 
  'superframboise': '#FA057F', 
  'grissombre': '#363332', 
  'toporange':  '#F37C06', 
  'coolcyan': '#4FEEF6',
  'violetparfait': '#6820B0',
  'citronadorable': '#FBF312',
}

ecran = Screen()
ecran.setup(420, 420)
ecran.bgcolor(couleurs['espace'])

penup()
goto(0, 100)
color(couleurs['superframboise'])
style = ('Arial', 40, 'bold')
write('SALUT', font=style, align='center')
right(90)
forward(60)
color(couleurs['toporange'])
write('LE MONDE', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(couleurs['grislune'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(couleurs['citronvert'])
style=('Verdana', 15, 'bold')
write('Un smartphone', font=style, align='center')
forward(40)
color(couleurs['superframboise'])
write('typique', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(couleurs['profondeurs'])
write('a plus de', font=('Verdana', 20, 'bold'), align='center')
forward(40)
color(couleurs['toporange'])
write('puissance de calcul', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(couleurs['violetparfait'])
write('que', font=style, align='center')
forward(40)
color(couleurs['coolcyan'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(couleurs['citronadorable'])
forward(40)
write('quand il a atterri sur', font=style, align='center')
color(couleurs['grissombre'])
forward(40)
write('la lune', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
