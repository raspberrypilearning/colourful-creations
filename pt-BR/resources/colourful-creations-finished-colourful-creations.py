#!/bin/python3

from turtle import *
from time import *

# introduz dicionários
# use um selecionador de cores para encontrar e escolher novas cores
cores= { 
  'espacial': '#060608', 
  'cinzalua': '#BCBDEF', 
  'verdelimao': '#A7E30E', 
  'fundodomar': '#226363', 
  'raspberry': '#FA057F', 
  'cinzaescuro': '#363332', 
  'laranjaforte':  '#F37C06', 
  'azulmaneiro': '#4FEEF6',
  'roxodahora': '#6820B0',
  'limaobacana': '#FBF312',
}

tela = Screen()
tela.setup(400, 400)
tela.bgcolor(cores['espacial'])

penup()
goto(0, 100)
color(cores['raspberry'])
style = ('Arial', 40, 'bold')
write('OLÁ,', font=style, align='center')
right(90)
forward(60)
color(cores['laranjaforte'])
write('MUNDO', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(cores['cinzalua'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(cores['verdelimao'])
style=('Verdana', 20, 'bold')
write('Um típico', font=style, align='center')
forward(40)
color(cores['raspberry'])
write('telefone celular', font=('Verdana', 22, 'bold'), align='center')
forward(40)
color(cores['fundodomar'])
write('possui mais', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color (cores ['laranjaforte'])
write('poder de computação', font=('Verdana', 21, 'bold'), align='center')
forward(40)
color(cores['roxodahora'])
write('que', font=style, align='center')
forward(40)
color(cores['azulmaneiro'])
write('a Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(cores['limaobacana'])
forward(40)
write('quando pousou', font=style, align='center')
color(cores['cinzaescuro'])
forward(40)
write('na Lua', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
