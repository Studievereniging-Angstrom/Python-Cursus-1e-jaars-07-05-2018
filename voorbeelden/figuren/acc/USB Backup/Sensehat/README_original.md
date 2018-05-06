# TIS-TN-METEC2
Meettechnieken 2 - code voor studenten (raspberries)

## Werking van de software
De python code ``` sensehat.py``` vraagt de versnellingssensor zo vaak mogelijk om data in 3 richtingen van de versnellingssensor. 
Deze data wordt in een file met unieke naam, maar beginnend met ```acc_``` en eindigend met ```.csv``` in de directory ```data``` weggeschreven. 

Een voorbeeld regel uit de file is hieronder weergegeven:
```
1502808562.755552,0.2572351098060608,0.008254947140812874,0.9484680891036987
```
In de eerste column staat de tijd, de volgende zijn de versnellingen (in g, m/s^2) gemeten door de sensor. Deze zijn verder niet gecalibreerd.

De software wordt automatisch opgestard bij het aanzetten van de Raspberrypi. Als er een USB-stick aanwezig is wordt deze in de ```/home/pi/data``` directory gemount zodat de datafile op de usb-stick weggeschreven wordt. Hiervoor is een vFAT geformatteerde USB-stick nodig. 

Als in de root van de USB-stick de file ```RTIMULib.ini``` staat wordt deze
gebruikt in plaats van de standaard file. 

## Bediening
Met de joystick kan de Raspberrypi bedient worden. 
 * start: joystick omhoog
 * pauze: joystik omlaag
 * instellingen opvragen: joystick naar links
 * afsluiten: 3x achter elkaar joystick indrukken
 
Als de instellingen opgevraagd worden wordt de numerieke waarde van de
variabele ```LSM9DS1AccelFsr``` weergegeven.  Door een door de user in te
stellen  ```RTIMULib.ini```
file op de USB-stick te plaatsen is deze variabele aan te passen en kan onder
andere de gevoeligheid van de versnellingssensor aangepast worden. 

Als er geen ```RTIMULib.ini``` file op de USB-stick geplaatst is wordt de
standaard file gebruikt. 

Bij afsluiten wordt de Raspberrypi uitgezet. Wacht nog een halve minuut voordat de USB-stick verwijdert kan worden. 

# Crontab
```@reboot /home/pi/TIS-TN-METR2-code/sensehat.py```

# RTIMUlib
De RTIMUlib file regelt alle settings van de sensoren. Hier kunnen eventueel de gevoeligheid aangepast worden.

# SSH of inloggen
De raspberrypi is via ssh en met HDMI en toetsenbord/muis te verbinden. Het useraccount is het standaard pi account:
 * username: pi
 * password: raspberry
