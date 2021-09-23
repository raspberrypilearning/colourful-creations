#!/bin/python3

from turtle import *
from time import *

# представляємо словники
# використовуй інструмент підбору кольорів для пошуку та вибору нових кольорів
colours = { 
  'космос': '#060608', 
  'місячно_сірий': '#BCBDEF', 
  'дуже_лимонний': '#A7E30E', 
  'глибоко_морський': '#226363', 
  'реально_малиновий': '#FA057F', 
  'хмуро_сірий': '#363332', 
  'неймовірно_апельсиновий': '#F37C06', 
  'круто_блакитний': '#4FEEF6',
  'ідеально_пурпурний': '#6820B0',
  'чудово_лимонний': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['космос'])

penup()
goto(0, 100)
color(colours['реально_малиновий'])
style = ('Arial', 40, 'bold')
write('Привіт', font = style, align = 'center')
right(90)
forward(60)
color(colours['неймовірно_апельсиновий'])
write('Світ', font = style, align = 'center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['місячно_сірий'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['дуже_лимонний'])
style = ('Verdana', 15, 'bold')
write('Типовий', font = style, align = 'center')
forward(40)
color(colours['реально_малиновий'])
write('смартфон', font = ('Verdana', 25, 'bold'), align = 'center')
forward(40)
color(colours['глибоко_морський'])
write('має більше', font = ('Verdana', 18, 'bold'), align = 'center')
forward(40)
color(colours['неймовірно_апельсиновий'])
write('обчислювальної потужності', font = ('Verdana', 15, 'bold'), align = 'center')
forward(40)
color(colours['ідеально_пурпурний'])
write('ніж', font = style, align = 'center')
forward(40)
color(colours['круто_блакитний'])
write('Аполлон 11', font = ('Verdana', 25, 'bold'), align = 'center')
color(colours['чудово_лимонний'])
forward(40)
write('коли він висадився', font = style, align = 'center')
color(colours['хмуро_сірий'])
forward(40)
write('на Місяці', font = ('Verdana', 25, 'bold'), align = 'center')
color('white')
forward(50)
write('- Ненсі Гіббс, 2012', font = ('Arial', 14, 'normal'))
