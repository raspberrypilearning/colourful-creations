## Using hex colour codes



Python turtle has predefined colours such as 'red' and 'white' but you can also use hex colour codes (you may have seen these in the HTML & CSS course.) 

--- task ---

Open the [Colourful creations starter](https://editor.raspberrypi.org/en/projects/colourful-creations-starter){:target="_blank"} project. The code editor will open in another browser tab.

--- /task ---


If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- task ---

Add the following set up code for using the turtle:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from turtle import *

screen = Screen()
screen.setup(400, 400)
screen.bgcolor('white')
--- /code ---
    
Notice that you used a named colour: 'white'.

--- /task ---

--- task ---

Turtle has a list of colour names that you can use, but sometimes you want to choose your own colours. Turtle also allows you to use hex colour codes. 

Open <a href="http://jumpto.cc/colour-picker" target="_blank">jumpto.cc/colour-picker</a> and choose a colour you like. Find its hex code beginning with a '#', such as '#A7E30E'. 

--- /task ---

--- task ---

Copy the hex code, including the hash, by highlighting it and then right-clicking and choosing Copy, or using Ctrl-C. 

--- /task ---  

--- task ---

Now change the line of code that sets the screen colour to use your colour. For example:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from turtle import *

screen = Screen()
screen.setup(400, 400)
screen.bgcolor('#A7E30E')
--- /code ---
   
You can use right-click and Paste or Ctrl-V to paste your hex code into the editor. 

--- /task ---

--- task ---

Choose another hex colour code and use it to create coloured text:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7-10
---
from turtle import *

screen = Screen()
screen.setup(400, 400)
screen.bgcolor('#A7E30E')

color('#BF3F7F')
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')
hideturtle()
--- /code ---

You don't have to use the 'Arial' font, you could try 'Verdana', 'Times' or 'Courier'.
   
'40' is the font size, you can try changing that too.  

--- /task ---  

--- task ---

Try different colours until you get two that you really like that look good together. 

--- /task ---   





