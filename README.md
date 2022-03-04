# Parametric-Turtle-v1.0

I made this in Thonny - Finished it March, 04 2022    

You will probably need Ghostscript to write gifs with ImageIO  
Ghostscript requires you to REBOOT YOUR COMPUTER other than that just download PIL and imageio  

The only variables I would recommend chaging are  
  112 - setup  
  118 - output folder - IMPORTANT (This program will delete all files that begin with "temp_" in this file location)  
  119 - pensize  
  120 - vertrical stretch  
  121 - horizontal stretch  
  122 - graph accuracy and speed (more precise takes longer)  
  123 - how long the output gif is in seconds (this is a minimum time and may sometimes be larger during small inaccurate low framecount graphs)  
  124 - makes the graph more dense (requires more accuracy)  
  125 - the total number of frames (this is a minimum number of frames and may sometimes be larger during small inaccurate low framecount graphs)  
  126 - offset angle (like a unit circle from 90 is up)  
  127 - initial starting point of the graph (the graph cycles through 2π rotations of t so this doesn't effect too much)  
  128 - the save_rate should only be changed if your memory becomes too full.  
        It is how many frames get added to the list before the list needs to be turned into a temporary gif  
        If a list is larger than 2MB python crashes. <200 is fine, I have it at 100 since it doesn't really matter too much  
