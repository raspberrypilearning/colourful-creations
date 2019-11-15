#!/bin/python3

from turtle import *
from time import *

# stwórz słowniki
# użyj próbnika kolorów, aby znaleźć i wybrać nowe kolory
kolory = { 
  "kosmos": "#060608", 
  "księżycowoszary": "#BCBDEF", 
  "bardzolimonkowy": "#A7E30E", 
  "głębokomorski": "#226363", 
  "naprawdemalinowy": "#FA057F", 
  "mrocznyszary": "#363332", 
  "superpomarańczowy":  "#F37C06", 
  "coolcyjan": "#4FEEF6",
  "perfekcyjnyfiolet": "#6820B0",
  "ślicznacytryna": "#FBF312",
}

ekran = Screen()
ekran.setup(400, 400)
ekran.bgcolor(kolory["kosmos"])

penup()
goto(0, 100)
color(kolory["naprawdemalinowy"])
styl = ("Arial", 40, "bold")
write("CZEŚĆ", font=styl, align="center")
right(90)
forward(60)
color(kolory["superpomarańczowy"])
write("ŚWIECIE", font=styl, align="center")
hideturtle()

sleep(3)

goto(0,0)
color(kolory["księżycowoszary"])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(kolory["bardzolimonkowy"])
styl=("Verdana", 20, "bold")
write("Typowy", font=styl, align="center")
forward(40)
color(kolory["naprawdemalinowy"])
write("smartfon", font=("Verdana", 25, "bold"), align="center")
forward(40)
color(kolory["głębokomorski"])
write("ma więcej", font=("Verdana", 18, "bold"), align="center")
forward(40)
color(kolory["superpomarańczowy"])
write("mocy obliczeniowej", font=("Verdana", 18, "bold"), align="center")
forward(40)
color(kolory["perfekcyjnyfiolet"])
write("niż", font=styl, align="center")
forward(40)
color(kolory["coolcyjan"])
write("Apollo 11", font=("Verdana", 25, "bold"), align="center")
color(kolory["ślicznacytryna"])
forward(40)
write("gdy wylądowało", font=styl, align="center")
color(kolory["mrocznyszary"])
forward(40)
write("na księżycu", font=("Verdana", 18, "bold"), align="center")
color("white")
forward(50)
write("- Nancy Gibbs, 2012", font=("Arial", 14, "normal"))
