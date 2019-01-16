#!/bin/python3

from turtle import *
from time import *

# uvodjenje rječnika
# koristi birač boja da pronadješ i odabereš nove boje
boje = { 
  'svemirska': '#060608', 
  'mjesecsiva': '#BCBDEF', 
  'limetazelena': '#A7E30E', 
  'morskoplava': '#226363', 
  'veomamalinasta': '#FA057F', 
  'sumornosiva': '#363332', 
  'supernarandzasta':  '#F37C06', 
  'kulplava': '#4FEEF6',
  'savrsenoljubicasta': '#6820B0',
  'limunzuta': '#FBF312',
}

ekran = Screen()
ekran.setup(400, 400)
ekran.bgcolor(boje['svemirska'])

penup()
goto(0, 100)
color(boje['veomamalinasta'])
style = ('Arial', 40, 'bold')
write('ZDRAVO', font=style, align='center')
right(90)
forward(60)
color(boje['supernarandzasta'])
write('SVIJETE', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(boje['mjesecsiva'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(boje['limetazelena'])
style=('Verdana', 20, 'bold')
write('Običan', font=style, align='center')
forward(40)
color(boje['veomamalinasta'])
write('pametni telefon', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(boje['morskoplava'])
write('ima više', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(boje['supernarandzasta'])
write('računarske snage', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(boje['savrsenoljubicasta'])
write('od', font=style, align='center')
forward(40)
color(boje['kulplava'])
write('Apola 11', font=('Verdana', 25, 'bold'), align='center')
color(boje['limunzuta'])
forward(40)
write('kada je sletio na', font=style, align='center')
color(boje['sumornosiva'])
forward(40)
write('Mjesec', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
