# README
## Til PST:
Koden i denne mappen er fra en innlevering jeg hadde i våres på universitetet. Den tar for seg både graph theory og webscraping. Jeg valgte denne koden siden jeg kan se for meg det kan være relevant for stillingen og siden jeg var fornøyd med innleveringen. Det skal være komentarer som forklarer de forskjellige delene ved koden, men ta gjerne kontakt om noe trenger forklaring. Jeg har masse programmer jeg har laget opp igjennom, så om dere vil se noe annet er det bare å si ifra.
Oppgaveteksten er også lagt ved.

## Task 1
Bruker networkX til å lage en framstilling av et datasett. Og bruker en dijkstra metode i networkX til å finne korteste veien mellom to noder.

## Task 2
Essensen av task 2 er at du gir programmet 2 hashtags, så leter programmet gjennom twitter og følger hashtags i x antall steps for hver av de to gitte hashtaggene. Og så lager den en graf som fremstiller sammenhenget mellom de. Programmet følger de første taggene den finner, hvis programmet for nok steps kan den havne på for eksempel noen NSFW tags, så er dere advart. Programmet kan ha lang kjøretid avhengig av hvor mange steps som er valgt, fordi den fysisk scroller og browser twitter.

## Libraries
For å teste koden må disse libraries installeres:
* bs4
* selenium
* networkX
* numpy

Chromedriver må også installeres og lagres i mappen over koden for testing i task 2, link her: https://chromedriver.chromium.org/ 