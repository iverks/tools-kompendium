[[SEM - _Scanne Elektron Mikroskop]]

# SEMmens oppbygging

 - Elektronkanon  
 - Elektromagnetiske linser  
	 - Aberrasjoner
 - Kondensorsystemet

## Oppbyggning av SEM

```
     V         - elektronkanon
|         |    - linser
|         |    /

   _____       - prøveholder
     | 
```


## Elektronkanon

```
		 __
		|  |
		|  |  
		\  / - Field emission gun
		 \/  - Skarp tupp
	____    ______
	___/	\____  - Anode 1
	____     _____ 
    ___|    |____  - Anode 2
```
 - Varmer opp tuppen -> 1700 K
 - 4kV mellom Anode 1 og tupp
	 - Trekker elektroner ut av tuppen
 - Anode 2 og tupp
	 - 200 kV mellom Anode 2 og tupp for TEM
	 - 5 kV mellom Anode 2 og tupp for SEM
	 - Akselererer elektroner
 - Optiske aksen
	 - Linje som går gjennom hele mikroskopet

### Egenskaper til elektronkanon

- Elektron-strøm
	- Så mange elektroner som mulig
- Virtuell størrelse
	- Hvor stor er tuppen???
- Energispredning
	- Hvor stor variasjon er det i den kinetiske energien til elektronene som skytes ut?
	- 1 eV spredning er MYE
	- 0.3 eV spredning er bra :)
	- Dette kommer av kromatiske aberrasjoner
- Vakuum
	- Hvor mye vakuum trenger den for å virke?
- Pris & levetid
- Temperatur
	- Høy temperatur gjør at den tåler mer kontaminering fordi det brennes bort

### Typer elektronkanoner

- LaB6 
	- Billig - 10 000 kr
	- Tåler dårlig vakuum $10^{-4}\rightarrow 10^{-6} Pa$
	- Størrelse 10 000 nm
	- Energispredning $\Delta E \Rightarrow 1.5 eV$
	- Temperatur $T = 1700K$ 
- Schottky Field Emission Gun (FEG)
	- Dyrere - 100 000 kr (i TEM)
	- Vakuum $10^{-7} Pa$
	- Størrelse 15 nm
	- Energispredning $\Delta E \Rightarrow 0.7 eV$
	- Temperatur $T = 1700 K$
	- FEG SEM = FLEX
- Cold FEG
	- Kjemipedyrt (for TEM - millioner)
	- Vakuum $10^{-8} Pa$
	- Størrelse 3 nm
	- Ekstremt presis energispredning $\Delta E = 0.3 eV$ 
	- $T = 300K$

## EM-Linser

 - Lage et magnetfelt
	 - $2 - 3 T$ som er veldig mye
 - Lorentz-kraften
	 -  $\vec{F} = -e(\vec{E}+\vec{v} \times \vec{B})$
	 $=-e\vec{v} \times \vec{B}$
	 - Kontrollere styrken ved å endre strømmen

### Aberrasjoner

EM-Linser er dritt  
- Typisk vinkel er $10 mrad$, milli-radianer, som tilsvarer $=0.57 ^o$
- Det finnes bare konvekse linser 😭
- Linsene er ikke perfekte, dvs de har aberrasjoner. Det finnes flere typer aberrasjoner

#### Sfæriske aberrasjoner

Treffer ikke fokuspunktet, men et større fokusområde.  
Elektronene som kommer fra forskjellige vinkler fra det samme punktet møtes ikke på samme punkt.  
Konsekvensen er at elektronproben blir større.  

#### Kromatiske aberrasjoner

Linsa bøyer elektroner med forskjellig energi forskjellig.  
Konsekvensen er igjen at elektronproben blir større.  
Derfor vil folk ha ColdFEG 😳  

## Kondensor(linse)systemet

Gjøre $e^-$ proben så liten som mulig  
Forminsker bildet av elektronkanon-tuppen ved å sette på sterke linser som trekker bildet lengre unna. Problemet med dette er at en mindre andel av elektronene treffer neste linse og dermed prøven.

### Aperturer

Aberrasjoner suger
Men aberrasjoner er proporsjonale med avstand til den optiske akse, dermed kan vi sette inn aperturer som blokkerer de dårlige elektronene. Det er elektronene som er lengst unna den optiske akse som er dårligst.
Men 😢: mindre aperture -> 
- Færre elektroner
- Mer parallell stråle
- Mindre effekt av aberrasjoner 🎉
- Rayleigh criterion 😡:
	- $\delta = \frac{0.61\lambda}{NA}$ der $NA$ er numerical aperture

