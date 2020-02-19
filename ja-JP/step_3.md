## 色のディクショナリ

Using hex colour codes is really flexible but they are hard to remember.

As you probably already know, a dictionary allows you to look up a word, and see it’s meaning. In Python, a dictionary is even more flexible that that - it allows you to look up a value for any 'key' in the dictionary.

Let's create a dictionary to map from human-friendly colour names (keys) to computer-friendly hex codes (values).

+ A dictionary is contained in curly brackets.
    
    Create an empty dictionary called `colours`:
    
    ![スクリーンショット](images/colourful-dict.png)

+ Choose cool names for your colours and edit the `colours =` line to add entries to the dictionary for them.
    
    Here's an example colour dictionary:
    
    ![スクリーンショット](images/colourful-colours.png)
    
    A colon `:` separates the key (colour name) from the value (hex code.) You need a comma `,` between each key:value pair in the dictionary.

+ Now you don't need to remember the hex codes, you can just look them up in the dictionary.
    
    Adapt the following code to use your colour names:
    
    ![スクリーンショット](images/colourful-entries.png)
    
    The key goes inside square brackets '[]' after the name of the dictionary.

+ Now you can update your code to look up colours in the dictionary:
    
    ![スクリーンショット](images/colourful-use.png)

+ Test your code to make sure your text still displays correctly.