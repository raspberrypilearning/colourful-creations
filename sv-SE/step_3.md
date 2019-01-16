## En färgordlista

Att använda hex färgkoder är väldigt flexibel men de är svåra att komma ihåg.

Som du förmodligen redan vet kan en ordlista du leta upp ett ord och se det är meningen. I Python är en ordlista ännu mer flexibel så att det låter dig leta upp ett värde för valfri nyckel i ordlistan.

Låt oss skapa en ordlista för att kartlägga från mänskliga användarnamn (nycklar) till datorvänliga hex-koder (värden).

+ En ordbok finns i lockiga parenteser.
    
    Skapa en tom ordbok som heter `färger`:
    
    ![skärmdump](images/colourful-dict.png)

+ Välj coola namn för dina färger och redigera `färger =` rad för att lägga till poster i ordlistan för dem.
    
    Här är ett exempel färgordlista:
    
    ![skärmdump](images/colourful-colours.png)
    
    En kolumn `:` skiljer nyckeln (färgnamn) från värdet (hex-koden.) Du behöver ett komma `,` mellan varje nyckel: värdet par i ordlistan.

+ Nu behöver du inte komma ihåg hex-koderna, du kan bara titta upp dem i ordboken.
    
    Anpassa följande kod för att använda dina färgnamn:
    
    ![skärmdump](images/colourful-entries.png)
    
    Nyckeln går in i hakparentes "[]" efter namnet på ordlistan.

+ Nu kan du uppdatera din kod för att leta upp färger i ordlistan:
    
    ![skärmdump](images/colourful-use.png)

+ Testa din kod för att kontrollera att texten fortfarande visas korrekt.