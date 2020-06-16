#!/bin/python3

from turtle import *
from time import *

# sözlükleri tanıtma
# yeni renkler bulmak ve seçmek için bir renk seçici kullanın
renkler = { 
  'uzay': '#060608', 
  'aygrisi': '#BCBDEF', 
  'limonata': '#A7E30E', 
  'derindeniz': '#226363', 
  'gercekahududu': '#FA057F', 
  'kasvetligri': '#363332', 
  'muhtesemturuncu':  '#F37C06', 
  'karizmatikcamgobegi': '#4FEEF6',
  'mukemmelmor': '#6820B0',
  'sarimtrak': '#FBF312',
}

ekran = Screen()
ekran.setup(400, 400)
ekran.bgcolor(renkler['uzay'])

penup()
goto(0, 100)
color(renkler['gercekahududu'])
style = ('Arial', 40, 'bold')
write('MERHABA', font=style, align='center')
right(90)
forward(60)
color(renkler['muhtesemturuncu'])
write('DÜNYA', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(renkler['aygrisi'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(renkler['limonata'])
style=('Verdana', 20, 'bold')
write('Ortalama', font=style, align='center')
forward(40)
color(renkler['gercekahududu'])
write('bir akıllı', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(renkler['derindeniz'])
write('telefonda', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(renkler['muhtesemturuncu'])
write('Aya iniş', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(renkler['mukemmelmor'])
write('yapan', font=style, align='center')
forward(40)
color(renkler['karizmatikcamgobegi'])
write('Apollo 11\'den', font=('Verdana', 25, 'bold'), align='center')
color(renkler['sarimtrak'])
forward(40)
write('daha fazla hesaplama', font=style, align='center')
color(renkler['kasvetligri'])
forward(40)
write('gücü vardır', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
