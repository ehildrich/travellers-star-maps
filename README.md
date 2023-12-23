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
><br>
> STAR<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> ...<br>
><br>
> CONNECT<br>
> label1, label2, slot_color, slot_diameter<br>
> label1, label2, slot_color, slot_diameter<br>
> ...

Within each section, the items can be in any order. 

# Values
All stars are placed on a square plane which runs from -100 to 100 on both axes. Each star's x, y, and z value must be within this range. The diameter of stars, the slot diameter of lines, the Line Width, Line Offset, Star Size, Circle Size, and Font Size values are all relative to this 200x200 plane. The only exceptions are the Image Size and Edge Size, which are in pixels. 