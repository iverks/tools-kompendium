# Tilbakemeldinger prosjektrapport
## Vag introduksjon

Ikke lag vag introduksjon, vær spesifikk til det problemstillingen handler om.

## Alt er skveret etter teknikkene

Del opp ut i fra problemstillingens delmål, ikke etter verktøy.

Riktig:

- Metode - se under
- Resultat
	- Geometri/topografi (SEM-bilder, AFM, TEM)
	- Kjemisk komposisjon (EDS)
	- Magnetiske domener (STEM-DPC)
- Diskusjon
	- Belyser problemstillingen basert på resultatene
	- F.eks data som peker forskjellige retninger
	- Prøve å motbevise det dere har funnet

## Mye unødvendige detaljer

- Probestrøm er vanligvis ikke nødvendig
- T1 detektor -> skriv heller hva slags kontrast (BSE, SE)
- Forstørrelse: ikke ta med (5000x, 10 000x, etc...). Dette er allerede i scalebar 🧠
- Unødvendig detaljert programvare
	- Burde nevne biblotekene dere faktisk bruker
		- Hyperspy, pyxem, gwyddion - som brukes til dataprosessering
	- IKKE ting 
		- tifffile - bare til å åpne data
		- matplotlib - bare til å plotte

## Metodedelen

- Kort og konsis 🌞
- Ikke skriv "FEI Helios at Nanolab". Dette skal inn i Acknowledgements
- FIB tilt trengs ikke å ta med hvis Ga$^+$-strålen er vinkelrett på prøven

## Referanser

- Vær obs
- Lenker skal ikke være med på vitenskapelige artikler

## Konklusjon

Konklusjonen skal være frittstående
- Gjenta det vitenskapelige målet
- Gjenta de viktigste funnene
- Hvordan de viktigste funnene passer inn i den faglige samtalen

## Author contribution

- Bruk initialer
- Bare de som er listet i forfatter-delen

## Ting på feil steder

- Resultater ender opp i metode 😂😂😂
	- "EDS-detektor [...] se figur 9"
- Teori i metoden
	- "FIB har elektronstråle og galliumstråle" er bare unødvendig 👿👿👿 Skriv varemerke i stedet

## Sette navn på struktur

- Sett navn på det dere lager, bruk de navnene konsekvent
- Eks:
	- Pt deponering => the patinum disk
	- C deponering => the carbon disk
	- Definer dette i metodedelen

## Figurtekster

- Figurtekster skal være relativt frittstående.
- Si teknikken brukt, t.d. SEM-BSE image of [...] 
- Målet er at man skal kunne se figuren, lese teksten og skjønne hva vi prøver å vise

## Figurer

- Bør ha samme x/y-lim hvis praktisk mulig
- Magnus hater padding 😡😡😡😡
- Mumax
	- Fargehjul
	- Samme farge og retning på simuleringer og DPC data (oooooh my gawd )

## Det skal være mellomrom mellom tall og enhet

Bruk pakken `SiUnitX`

## Overdreven språkbruk

- "The results clearly show" (Er det virkelig så åpenbart 🤔🤔🤔)
- "Exploited STEM-DPC" (Stakkars STEM DPC 😭😭😭) 
- "Extremely" (Er du terrorist eller? 💥💥💥)

## Ikke unnskyld dere 😭😭😭

- Skriv heller future work
- Eks:
	- I stedet for "Unfortunately the EDS data sucky 😭👅👣"
	- Skriv "To get a better understanding we can use EDS to look at the composition😎🐍"

## Referere til figur

- As shown in fig 4a the data

## Acknowledegemetnetast

- Ikke takk "lab information"
- "We thank ... , ... for assistance with SEM experiments"
- "We thank ... for fruitful discussions"

## Integrated magnetic induction om STEM-DPC data