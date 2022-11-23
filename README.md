# Jupyter Notebook kompendium

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://iverks.github.io/tools-kompendium)

Dette kompendiet er laget med [jupyter-book](https://jupyterbook.org/en/stable/intro.html), og [nettsiden](https://iverks.github.io/tools-kompendium) hostes gratis på github pages og oppdateres automatisk når endringer skjer ved hjelp av github actions. Om du er en fremtidig student som ønsker å rette en skrivefeil eller fullføre noe av det som jeg sikkert ikke har skrevet helt ferdig kan du gjøre det ved å klone eller forke repoet og så åpne en pull-request. Jeg kommer nok til å godkjenne det meste.

Kompendiet kan også [kompileres til latex](https://jupyterbook.org/en/stable/advanced/pdf.html) om det er den foretrukkede måten å distribuere det på.

## Utvikling

Jupyter books er skrevet i Markdown. Om du er en flittig bruker av www.timini.no (slik du bør) har du god kjennskap til dette, men uansett: [her er en cheatsheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html). Merk også at jupyter books har en utvidet markdown-syntax, spesielt nyttig er [target headers](https://jupyterbook.org/en/stable/reference/cheatsheet.html#target-headers) med [tilhørende lenker](https://jupyterbook.org/en/stable/reference/cheatsheet.html#referencing-target-headers) , [figures](https://jupyterbook.org/en/stable/reference/cheatsheet.html#figures-and-images) og [admonitions](https://jupyterbook.org/en/stable/reference/cheatsheet.html#admonitions).

For å kompilere boken lokalt til testing må du installere `jupyter-book` med pip (eller conda), så kjører du kommandoen

```console
jupyter-book build .
```

ikke glem `.`. `jb` kan brukes som forkortelse for `jupyter-book`.

## Til de ikke-så-teknisk-anlagte

Om du har en ide til noe å fikse, men ikke er gira på å sette opp jupyter-book osv. Opprett gjerne en [issue](https://github.com/iverks/tools-kompendium/issues), og skriv inn endringen du er gira på, så kan noen som er mer teknisk anlagt få gratis aktivitetspoeng i github for å copy-paste teksten din inn i kildekoden. Det finnes også en knapp for å opprette issues oppe i høyre hjørne på nettsiden.