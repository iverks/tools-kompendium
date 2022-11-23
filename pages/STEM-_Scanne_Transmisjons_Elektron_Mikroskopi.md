Bruker [[SEM - _Scanne Elektron Mikroskop]]

# STEM

Når vi bruker (S)TEM må vi alltid ha en tynn prøve, i motsetning til på SEM.

Når vi bruker SEM kan vi se på store områder, men når vi bruker STEM kan man maks se på et område med 3mm diameter. Typisk ser man på 100x100 um.

## Navnekonvensjoner
TEM - 🔬 instrumentet
STEM - 📚 metoden scanning på temmen
CTEM - 📚 metoden konvensjonell temming, parallell modus
S(T)EM - 🔬 instrumentet SEM som kan gjøre STEM, men ikke CTEM ⁉

## Parallell vs konvergent 👊

|Parallell | Konvergent|
| :--- | :--- |
| Treffer hele prøven på en gang | Man vet at alt signalet kommer fra en plass |
| | Må scanne |

## STEM vs SEM oppbygging

```
       V      e- kanon    V
    |     | kondensor  |      |
    |     |  objektiv  |      |
    |     |            |      |
prøve 💉                  🐈    prøve
    |     |               ___    prøveholder
    |     | }projektor     |
    | ___ |  system
      detektorer
```

SEM - Ser på det som kommer ut igjen av prøven

STEM - Ser på det som blir transmittert gjennom prøven

## Diffraksjon

Braggs lov. Her er $d$ avstand mellom atomplan, $\lambda$ bølgelengde på partikler som sendes inn, $\theta$ spredningsvinkel

$$
2 d \sin \theta = n \lambda 
$$

$$
\implies \theta = \arcsin\left(\frac{n \lambda}{2 d}\right)
$$

$$
\implies d = \frac{n \lambda}{2 \sin \theta}
$$

Det er ganske chillern.  
Hvis atomene er langt unna hverandre i virkeligheten blir de nærme hverandre i diffraksjonsmønsteret (det resiproke rom)

### Resultater av diffraksjon

Monokrystall: Firkantmønster  
Polykrystall: Ringmønster av skarpe ringer   
Amorft: Ringmønster av diffuse ringer  
Nanokrystallinsk: Uregelmessig firkantmønster  

## Prosjektor-systemet

Prosjektorsystemet ligger mellom det nedre objektivet og kameraet. 

Vi endrer kameralengten ved hjelp av hokus pokus linser for å få hjelpsomme elektroner (z-kontrast elektroner) til å treffe ADF-linsa vår ([[TEM - _Transmission Electron Microscope | mer om adf her]]). Dvs at vi endrer den optiske avstanden fra prøve til detektor. Den optiske avstanden kan gå fra 1cm til 10km.

## Z-kontrast

Signaler i STEM: 
- Direktestrålen
- Diffraksjon/Bragg-spredning
- Z-kontrast
- Røntgen (EDS)

Z-kontrast er elektroner som ~~har blitt elastisk støtt fra atomkjerner~~ hokus pokus kvantekolliderer med atomer, og vinkelen deres er proporsjonal med atomvekt (som er proporsjonalt med atomnummer nesten). Navnet på hokus pokus er "Thermal diffuse scattering"