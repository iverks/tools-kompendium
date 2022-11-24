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
![konvergensvinkel](../images/Konvergensvinkel%20pluss%20mer/Konvergensvinkel%20pluss%20mer%20-%20page%201.png)

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

#### Signaler/bildekontrast

- Backscatter elektroner
	- relativt atomnummer
- Sekundærelektroner
	- Overflate og topografi
	- Flere enn BSE fordi det ikke er avhengig av at elektronene går inn i materialet
- EDS
	- Kjemisk komposisjon og hvilke grunnstoffer
- EBSD - Electron BackScatter Diffraction
	- krystallstruktur

SETT INN FIGUR FRA "Backscatter elektron" eller lag en ny bedre figur som inkluderer SE, BSE, EDS
![interaksjonsvolumets signaler](https://www.nanoimages.com//wp-content/uploads/sem_img6.png)

SE - overflaten  
BSE + EBSD - øverste andel av interaksjonsvolum  
EDS - Hele interaksjonsvolum

#### SEM interaksjonsvolum

- **Viktig**
- Fysiske grensen for oppløsning
- Større akselerasjonsspenning -> større interaksjonsvolum
- Tyngre materiale -> mindre interaksjonsvolum

### STEM 

#### Signaler/bildekontrast

- BF - Bright field
- EELS - Energy electron loss spectroscopy
	- kjemisk komposisjon
	- elektronsstrktur
	- båndgap
	- oksidasjonstall
- ADF - Annular dark field
- HAADF - High angle annular dark field
	- Z-kontrast (relativt atomnummer)
- EDS - Energy dispersive x-ray spectroscopy
	- Kjemisk komposisjon
- SED - Scanning electron diffraction
	- Krystallstruktur
- DPC - Differential phase contrast
	- Funksjonelle egenskaper
	- Dvs magnetiske og elektriske felt

#### Interaksjonsvolum

- Tykkelsen er under 100 nm
- Dermed får vi et lite interaksjonsvolum
- Vi kan få atomæroppløsning

> Dag Werner Breiby er diffraksjonsmesteren
> -Magnus Nord (parafrasert)


### FIB - Bruksområder

#### Grave og kutte

> Det er en gravemaskin... Nanogravemaskin!

```
  \  /
   \/   Ga+
___   ___
   |_|     Prøve
```

- Skyter $Ga^+$ på materiale
	- Fjerne materiale

#### Deponering

1. Blåser gass på prøven.
2. Skyter $Ga^+$ på prøven og gassen slik at gassen deponeres på prøven.

### Prøvebegrensninger

- Største problem: Vakuum
	- Ikke væsker
	- Ikke levende celler
		- De dør 💀
- Stråleskade
	- Høy-energi elektroner
	- Nesten lysets hastighet ⚡
- Oppladning
	- Man bør ha ledende prøver, hvis ikke bygger det seg ladninger på dem
- Biologiske prøver er mulig men trenger spesiell prøvepreparering

### Sammenligning av instrumenter

|  Verktøy | Oppløsning | Pris | Vakuum | Nødvendig Trening | Veldig tynn prøve |
| --- | --- | --- | --- | --- | --- |
| SEM | nm| lav-medium| Ja| Lite | Nei |
| FIB | nm| medium-høy| Ja| Medium | Nei |
| TEM | Å| medium-veldig høy| Veldig ja | Mye | Jeppsi pepsi |
| AFM | nm| lav-medium| Nei | Lite | Nei |