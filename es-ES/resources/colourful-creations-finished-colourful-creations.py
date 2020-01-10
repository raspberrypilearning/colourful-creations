#!/bin/python3

from turtle import *
from time import *

# introduce diccionarios
# usa un selector de color para encontrar y elegir nuevos colores
colores = { 
  'espacio': '#060608', 
  'grislunar': '#BCBDEF', 
  'muylima': '#A7E30E', 
  'marprofundo': '#226363', 
  'realmenteframbuesa': '#FA057F', 
  'grissombrio': '#363332', 
  'naranjaimpresionante':  '#F37C06', 
  'cianmolon': '#4FEEF6',
  'moradoperfecto': '#6820B0',
  'limonencantador': '#FBF312',
}

pantalla = Screen()
pantalla.setup(400, 400)
pantalla.bgcolor(colores['espacio'])

penup()
goto(0, 100)
color(colores['realmenteframbuesa'])
style = ('Arial', 40, 'bold')
write('HOLA', font=style, align='center')
right(90)
forward(60)
color(colores['naranjaimpresionante'])
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
color(colores['muylima'])
style=('Verdana', 20, 'bold')
write('Un típico', font=style, align='center')
forward(40)
color(colores['realmenteframbuesa'])
write('teléfono móvil', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colores['marprofundo'])
write('tiene más', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colores['naranjaimpresionante'])
write('potencia de cálculo', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colores['moradoperfecto'])
write('que', font=style, align='center')
forward(40)
color(colores['cianmolon'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colores['limonencantador'])
forward(40)
write('cuando aterrizó en', font=style, align='center')
color(colores['grissombrio'])
forward(40)
write('la luna', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
