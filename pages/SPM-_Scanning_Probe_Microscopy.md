Scanning Probe Microscopy er å ta bilder av en prøve ved å skanne en fysisk probe rett over prøven. [[AFM - Atomic Force Microscopy]] er en type SPM.


## Prototype: Scanning tunneling mikroskopi STM 

En probe med spenning på føres over prøven. Når proben er nærme nok kan man detektere en tunelleringsspenning mellom prøven og proben. En negativ feedback loop gjør at proben holder seg nøyaktig like langt unna prøven.

- Lav spenning: gå nærmere
- Høy spenning: gå lengre unna

## AFM teori

Kraften mellom tuppen og prøven er summen av pauli repulsion og van der waals tiltrekning

$$
V_{LJ}(\Delta z) = 4 \epsilon 
\left[
\left( \frac{\sigma}{\Delta z} \right)^{12} -
\left( \frac{\sigma}{\Delta z} \right)^6
\right]
$$

![funksjon for kraft](https://i.imgur.com/dP6j0w3.png)

### Oppbygging

- Laser
- AFM prober - tip og cantilever
- Piezoelektrisk scanner
- Posisjonssensitiv detektor (PSD)
- Feedback loop system
- Ristepiezo (bare tapping mode)

#### Tip og cantilever

Tip radius bestemmer oppløsningen. En mindre tip git bedre oppløsning. Tippen er ofte laget av  silisiumnitrat for contact mode eller silisium for tapping mode.  Toppen av cantileveren pleier å være coatet for å øke reflektiviteten. Man kan også coate tippen slik at den er elektrisk ledende eller lage den av magnetiske materialer dersom det er gunstig.

#### Piezoelectric scanners

- Direkte piezoelektrisk effekt
	- Trykk på ting -> spenning
- Invers piezoelektrisk effekt:
	- Spenning/strøm -> Trekker seg sammen/utvider seg

Om man setter sammen flere piezoelektriske motorer kan man kontrollere bevegelsen i flere dimensjoner.

#### PSD - posisjonssensitiv detektor

Laser spretter fra cantilever. Posisjon av laser måles på fotodiode.

![psd](https://i.imgur.com/jLoAix1.png)

### Contact mode

Gni tuppen inntil prøven som en huleboer. Få mye data raskt, men kan skade prøven.

### Tapping mode

La cantilever oscillere med en gitt frekvens over prøven. Oscillasjonsamplituden går ned når tippen kommer nærme prøven pga demping fra van der Waals krefter. Feedback-loopen er basert på denne amplituden.

### Phase channel tapping mode

Regioner med forskjellig mykhet har forskjellige faseforskyvninger. Hvorfor? Vet ikke. Dette kan man bruke til å skille mellom forskjellige faser i prøven.

#### Fordeler og ulemper

- Contact mode
	- +Rask hastighet
	- +Tåler bedre bratte deler av prøven
	- +Renser prøven for dritt
	- -Ødelegger tippen
	- -Skader myke prøver
	- -Tiltrekker dritt
	- -Sterke laterale og normale krefter
- Tapping mode
	- +Høyere lateral oppløsning
	- +Mindre skade på tippen og prøven
	- +Fasekontrast [[#Phase channel tapping mode]]
	- -Litt tregere skannehastighet
	- -Krever en ristepiezo

### Eksempler på AFM-bilder

![eksempler på afm bilder](https://i.imgur.com/mITs040.png)

Menneskehår "kan ikke" avbildes i SEM fordi de ikke leder strøm.
I sjokoladebildet kan man se de forskjellige 

### Artefakter og begrensninger

#### Hysterese

Piezoelektriske skannere har ikkelinjære hysteresekurver. Resultatet av dette er at skanningene fra traces og retraces ser forskjellige ut. Det går an å løse ved å bruke ikke-linjære bølger på den piezoelektriske skanneren (hva betyr dette????). Dette må da rekalibreres fordi piezoelektriske elementer foreldes over tid.

####  Bøyning i topografi

Bøyning i topografi

#### Dritt på tuppen

![](https://i.imgur.com/2gP6uAW.png)

#### Dobbel-tipp effekten

![doble bilder](https://i.imgur.com/XOfD8ea.png)

#### Dårlig valgt gain

Man kan se at man har valgt riktig gain om scannen fra trace er lik scannen fra retrace.

![smearing og overkompensering](https://i.imgur.com/nBwOXW6.png)


## Piezoresponse Force Microscopy - PFM

Sender en AC strøm på tippen for å se hva som skjer med prøven.

## Conductive AFM - cAFM

Ser hvor mye strøm som går mellom tippen og prøven.

## Electrostatic FM - EFM

Ladd tupp. Holder den langt unna prøven. Ser på elektrostatiske krefter mellom tippen og prøven. Nice.

## Magnetic FM - MFM

Samme familie som EFM 💏. Holder tippen høyt over prøven. Gjør tippen magnetisk. Se på magnetostatiske krefter fra prøven.