#!/bin/python3

from turtle import *
from time import *

# создание словарей
# используй подборщика цветов, чтобы найти и выбрать новые цвета
colours = { 
  'космос': '#060608', 
  'сераялуна': '#BCBDEF', 
  'оченьлимонный': '#A7E30E', 
  'глубокоеморе': '#226363', 
  'настоящаямалина': '#FA057F', 
  'мрачносерый': '#363332', 
  'потрясныйапельсин':  '#F37C06', 
  'крутойциан': '#4FEEF6',
  'идеальнопурпурный': '#6820B0',
  'прекрасныйлимон': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['космос'])

penup()
goto(0, 100)
color(colours['настоящаямалина'])
style = ('Arial', 40, 'bold')
write('ПРИВЕТ', font=style, align='center')
right(90)
forward(60)
color(colours['потрясныйапельсин'])
write('МИР', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['сераялуна'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['оченьлимонный'])
style=('Verdana', 20, 'bold')
write('Типичный', font=style, align='center')
forward(40)
color(colours['настоящаямалина'])
write('смартфон', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['глубокоеморе'])
write('наделён большей', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['потрясныйапельсин'])
write('мощностью', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['идеальнопурпурный'])
write('чем', font=style, align='center')
forward(40)
color(colours['крутойциан'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colours['прекрасныйлимон'])
forward(40)
write('приземлившийся', font=style, align='center')
color(colours['мрачносерый'])
forward(40)
write('Луна', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Нэнси Гиббс, 2012', font=('Arial', 14, 'normal'))
