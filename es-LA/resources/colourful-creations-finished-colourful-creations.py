#!/bin/python3

from turtle import *
from time import *

# introduce diccionarios
#usa un selector de color para buscar y elegir nuevos colores
colores = { 
  'azulmarino': '#060608', 
  'grislunar': '#BCBDEF', 
  'lima': '#A7E30E', 
  'verdeazuladooscuro': '#226363', 
  'rosa': '#FA057F', 
  'grisoscuro': '#363332', 
  'naranja':  '#F37C06', 
  'turquesa': '#4FEEF6',
  'morado': '#6820B0',
  'amarillolimón': '#FBF312',
}

pantalla = Screen()
pantalla.setup(400, 400)
pantalla.bgcolor(colores['negro'])

penup()
goto(0, 100)
color(colores['rosa'])
style = ('Arial', 40, 'bold')
write('HOLA', font=style, align='center')
right(90)
forward(60)
color(colores['naranja'])
write('MUNDO', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colores['grislunar'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colores['lima'])
style=('Verdana', 20, 'bold')
write('Un típico', font=style, align='center')
forward(40)
color(colores['rosa'])
write('celular moderno', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colores['verdeazuladooscuro'])
write('tiene más', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colores['naranja'])
write('poder de cómputo', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colores['morado'])
write('que el', font=style, align='center')
forward(40)
color(colores['turquesa'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colores['amarillolimón'])
forward(40)
write('cuando aterrizó en', font=style, align='center')
color(colores['grisoscuro'])
forward(40)
write('la luna', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
