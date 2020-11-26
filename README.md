# TXT to JSON
Python script om een txt bestand (gecopypaste uit Word) te converteren naar JSON.
In dit geval: Wanneer er 3 lege regels zijn begint een nieuw JSON object.

## Usage
```
./txt2json.py INPUTFILE.txt > result.json
```

## Input
```
    5-1.        Kaart van het noordwestelijke deel van de provincie Utrecht met een gedeel­te van Noord- en Zuid-Holland, waarop aangegeven de grenzen van het water­schap Amstel­land.

                 Met 125 regels toelichting.

                 Jacob van Banchem, 1593 naar Joost Jansz. Beeldsnijder, 1570.

                 Reproduktie; 45 x 59 cm; 1 blad.

                 N.B. Origineel en copyright: Gemeentearchief Leiden, nr. 70362. 

 

    5-2.        'Ultraiectum Dominium. The Bishop-ricke. Kaart van de provincie met aangren­zen­de ge­bieden.

                 Kopergravure; ingekleurd; 17 x 24 cm; 1 blad.

                 Op de achterzijde fragment van een Engelstalige beschrijving van de provincie.

 

    5-3.        'Evesché d'Utrecht'. Kaart van Utrecht en aangrenzende gebieden.

                 Kopergravure; ingekleurd; 10 x 13 cm; 1 blad. 

                 Uit: L. Guicciardini Descrittione di tutti i Paesi Bassi, p. 249.

                 Op de achterzijde fragment van een Franstalige beschrijving van de provincie.

```

## Output
```json
    [
        "5-1.        Kaart van het noordwestelijke deel van de provincie Utrecht met een gedeelte van Noord- en Zuid-Holland, waarop aangegeven de grenzen van het waterschap Amstelland.",
        "Met 125 regels toelichting.",
        "Jacob van Banchem, 1593 naar Joost Jansz. Beeldsnijder, 1570.",
        "Reproduktie; 45 x 59 cm; 1 blad.",
        "N.B. Origineel en copyright: Gemeentearchief Leiden, nr. 70362."
    ],
    [
        "5-2.        'Ultraiectum Dominium. The Bishop-ricke. Kaart van de provincie met aangrenzende gebieden.",
        "Kopergravure; ingekleurd; 17 x 24 cm; 1 blad.",
        "Op de achterzijde fragment van een Engelstalige beschrijving van de provincie."
    ],
    [
        "5-3.        'Evesché d'Utrecht'. Kaart van Utrecht en aangrenzende gebieden.",
        "Kopergravure; ingekleurd; 10 x 13 cm; 1 blad.",
        "Uit: L. Guicciardini Descrittione di tutti i Paesi Bassi, p. 249.",
        "Op de achterzijde fragment van een Franstalige beschrijving van de provincie."
    ],
```