##Wat is er anders?

De volgende sensoren worden gebruikt, waarvan hun data op respectievelijke wijze word opgeslagen.
- time
- accelerometer x
- accelerometer y
- accelerometer z
- humidity
- temperature from humidity
- temperature from pressure
- pressure
- compass x
- compass y
- compass z

Verder hoeft de Pi niet meer opnieuw opgestart te worden om meerdere metingen te doen (die niet achter elkaar in 1 bestand worden opgeslagen). Tevens word de sensehat.py code nu vanaf de usb-stick genaamd 'DATA' opgestart. Iedereen kan dus gemakkelijk de code aanpassen zonder enige kennis van linux te hebben.

## Installatie 
Let op, de software is getest met Raspbian GNU/Linux 9 (stretch)
Wanneer deze code voor het eerst gebruikt word op een raspberry pi dient de volgende code ingetypt te worden in de terminal.
```
sudo python3  /media/pi/DATA/Sensehat/service_installation.py
```
## Starten van het script
Zodra sensehat.service is geinstalleerd kan het script gestart worden m.b.v. onderstaande code.
```
sudo python3  /media/pi/DATA/Sensehat/start_script.py
```
## Gebruik instructies
Joystick naar rechts om sensehat.py op te starten.
Alle andere controls zijn hetzelfde gebleven.

Oorspronkelijke code: https://github.com/HHS-TN/TIS-TN-METR2-code