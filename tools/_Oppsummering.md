# Oppsummering

## Mikroskopi 🔍

###  Nøkkelkonsepter 🔑

- Oppløsning
	- Hvor små ting kan vi se? 
- Hvordan virker en avbildingsteknikk 🤔
	- **Scanne** eller parallell (vi har stort sett brukt scanne)
- Kontrastmekanismer
	- Hva ser vi egentlig?
	- Hva betyr intensiteten?
- Prøve-begrensinger 🦠
	- Væsker fungerer ikke i vakuum

#### Oppløsning

- Probestørrelsen
- Probe-prøve interaksjon

##### Probestørrelse

- Bølgelengde $\lambda$
	- Rayleigh criterion: $\delta = \frac{0.61}{NA}$
	- Fotoner, synlig lys $\approx 300 nm$ ikke bra nok
	- Vi bruker matter waves i stedet $\lambda = \frac{\hbar}{mv}$
		- for $e^-$ $200keV$ $\lambda = 2.5pm$
- Flere ting som begrenser oppløsning
	- Astigmatisme
	- Andre aberrasjoner
	- Filamentstørrelse
	- +++
- Probestørrelsen er summen av alle disse.

##### Probe-prøve interaksjon


```
SEM
      V e-
_____________
      /\
     (  ) <-- Interaksjonsvolum
      ¯
```

```
TEM
       V e-
_____________
______|_|____
       ^-- Interaksjonsvolum
```

Oppløsning = Probestørrelse + interaksjonsvolum

### SEM -struktur


```
     V         - elektronkanon
|    |    |    - kondensorsystem => Forminsker bildet av filamentet
|    |    |    - kondensorsystem
ξ   /     ξ    - Scannecoils
|   |     |    - objektivlinse
	|   👅     - Detektorer
  __◼___      - prøveholder + prøve
     | 
```

### FIB - struktur

Samme som SEM men en galliumkanon i tilelg.

> $FIB = SEM + Ga-kolonne$
> -Magnus Nord

- I tillegg har man ofte en FIB-needle som man kan bruke til å mekanisk manipulere prøven.
- Gassnåler som man kan bruke til å blåse spesifikke gasser på prøven for å deponere dem.

### STEM - struktur

```
     V         - elektronkanon
|    |    |    - kondensorsystem => Forminsker bildet av filamentet
|    |    |    - kondensorsystem
ξ   /     ξ    - Scannecoils
|   | 👅 |    - objektivlinse
    ◼---    - prøveholder + prøve
|   |     |    - objektivlinse
|   |     |    - prosjektorsystem  => Forstørrer elektronspredningen
|   |     |    - prosjektorsystem

    💿      - detekrorer
    📦      - detektorer
    
```

### SEM vs STEM 🥊

- Lignende struktur
- Hovedforskjellene
	- STEM => projeksjonssystemet
	- Akselerasjonsspennig
		- SEM: $1 - 30\,$kV
		- STEM: $60 - 300\,$kV
			- Dette betyr at vi må ha sterkere linser og tykkere kolonne
	- Detektorer
		- SEM: bak prøven
		- STEM: foran prøven "forward scattering"

### Viktige konsepter

#### SEM og FIB

SETT INN BILDER FRA "Konvergensvinkel pluss mer"
![konvergensvinkel](../images/Konvergensvinkel%20pluss%20mer/Konvergensvinkel%20pluss%20mer%20-%20page%201.svg)

- Konvergensvinkel $\alpha$
	- Hvor "spiss" elektronstrålen er.
- Arbeidsavstand
	- Hvor langt unna prøven elektronkanonen er 
- Kondensoraperture
	- Større kondensoraperture -> større konvergensvinkel 
	- Liten kondensoraperture -> få elektroner 😭
- Dybdeskarphet
	- Hvor stort område langs den optiske aksen prøven er i fokus
	- Større konvergensvinkel $\alpha$ gir liten dybdeskarphet

#### STEM

- Konvergensvinkel
	- Samme som SEM og FIB
- Dybdeskarphet
	- Samme som SEM og FIB
- Kameralengde
	- Den optiske avstanden fra prøven til detektoren
	- $1\,$cm $- 10\,$km
	- Kan endres ved hjelp av linsemagi
	- Nyttig for STEM-DPC fordi strålen er veldig parallell
	- Gir samme effekt som å zoome inn på output-signalet


### SEM

- Backscatter elektroner
	- relativt atomnummer
- Sekundærelektroner
	- Overflate og topografi
- EDS
	- Kjemisk komposisjon og hvilke grunnstoffer
- EBSD - Electron BackScatter Diffraction
	- krystallstruktur