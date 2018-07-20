#!/bin/python3

from turtle import *
from time import *

# Einführung Dictionaries
# Suche mit Hife eines Farbwahl-Werkzeugs neue Farben aus
farben = { 
  'weltraum': '#060608', 
  'mondgrau': '#BCBDEF', 
  'giftgruen': '#A7E30E', 
  'tiefseeblau': '#226363', 
  'hyperhimbeer': '#FA057F', 
  'garstiggrau': '#363332', 
  'oohrange':  '#F37C06', 
  'totaltuerkis': '#4FEEF6',
  'luxuxslila': '#6820B0',
  'sauergelb': '#FBF312'
}

flaeche = Screen()
flaeche.setup(400, 400)
flaeche.bgcolor(farben['weltraum'])

penup()
goto(0, 100)
color(farben['hyperhimbeer'])
stil = ('Arial', 40, 'bold')
write('HALLO', font=stil, align='center')
right(90)
forward(60)
color(farben['oohrange'])
write('WELT', font=stil, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(farben['mondgrau'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(farben['giftgruen'])
stil=('Verdana', 20, 'bold')
write('Ein heutiges', font=stil, align='center')
forward(40)
color(farben['hyperhimbeer'])
write('Smartphone', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(farben['Tiefseeblaugrün'])
write('hat mehr', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(farben['Orange'])
write('Rechenleistung', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(farben['Dunkelviolett'])
write('als', font=style, align='center')
forward(40)
color(farben['Blaugrün'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(farben['Zitronengelb'])
forward(40)
write('bei der Landung', font=style, align='center')
color(farben['Dunkelgrau'])
forward(40)
write('auf dem Mond', font=('Verdana', 25, 'bold'), align='center')
color(farben['Weiß'])
forward(65)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
