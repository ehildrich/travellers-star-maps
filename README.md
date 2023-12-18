# Traveller's Star Maps	
A simple Python application to generate visual starmaps for use in the TTRPG Traveller. It is currently in progress. 

## Python Libraries
This project utilizes the following Python libraries: 
* Pillow
* mathplotlib

## Text File Format
In order for the stars and lines to be read in properly from the text file, the file must be in the following format:
> STAR<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> Label, X, Y, Z, circle_color, circle_diameter<br>
> ...<br>
> CONNECT<br>
> label1, label2, slot_color, slot_diameter<br>
> label1, label2, slot_color, slot_diameter<br>
> ...
