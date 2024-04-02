## A Colour Dictionary

Using hex colour codes is really flexible but they are hard to remember. 

As you probably already know, a dictionary allows you to look up a word, and see it’s meaning. In Python, a dictionary is even more flexible that that - it allows you to look up a value for any 'key' in the dictionary.

Let's create a dictionary to map from human-friendly colour names (keys) to computer-friendly hex codes (values).

--- task ---

A dictionary is contained in curly brackets. 

Create an empty dictionary called `colours`:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5-7
---
screen = Screen()
screen.setup(400, 400)

colours = {}

screen.bgcolor('#A7E30E')
--- /code ---

--- /task ---

--- task ---

Choose cool names for your colours and edit the `colours = ` line to add entries to the dictionary for them. 

Here's an example colour dictionary:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 7-9
---
colours = {
  'verylime': '#A7E30E',
  'reallyraspberry': '#BF3F7F'
}
--- /code ---
   
A colon `:` separates the key (colour name) from the value (hex code.) You need a comma `,` between each key:value pair in the dictionary. 

--- /task ---   

--- task ---

Now you don't need to remember the hex codes, you can just look them up in the dictionary. 

Adapt the following code to use your colour names:
  
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 11-12
---
colours = {
  'verylime': '#A7E30E',
  'reallyraspberry': '#BF3F7F'
}

print(colours['verylime'])
print(colours['reallyraspberry'])
--- /code ---
  
The key goes inside square brackets '[]' after the name of the dictionary.

--- /task ---

--- task ---

Now you can update your code to look up colours in the dictionary:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14
line_highlights: 14, 16
---
screen.bgcolor(colours['verylime'])

color(colours['reallyraspberry'])
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')
hideturtle()
--- /code ---

--- /task ---

Test your code to make sure your text still displays correctly.
  




