# Traveller's Star Maps	
A simple Python application to generate visual starmaps for use in the TTRPG Traveller. It is currently in progress. 



## Python Libraries
This project utilizes the following Python libraries: 

* Pillow
* math
* mathplotlib
* os
* datetime



## Text File Format
In order for the stars and lines to be read in properly from the text file, the file must be in the following format:

> PARAMETER<br>
> Image Size: X<br>
> Edge Size: X<br>
> Line Width: X<br>
> Line Offset: X<br>
> Star Size: X<br>
> Circle Size: X<br>
> Font Size: X<br>
> STAR<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> ...<br>
> CONNECT<br>
> label1, label2, slot_color, slot_diameter<br>
> label1, label2, slot_color, slot_diameter<br>
> ...

Within each section, the items can be in any order. 