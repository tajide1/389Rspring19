# Extra Credit Writeup - Binaries II

Name: Oluwatobi Ajide
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Oluwatobi Ajide

## Assignment Writeup

### Part 1 (100 Pts)
Using radare2, I analyzed the locker file. First Iopened the file using the command "r2 locker" and then typed "aaa" to able to step into 
the main of the locker file using "s main". Stepping into the main of locker allowed me to be able to use the command "VV" to view the graph format of the locker file. Analyzing the cmp functions allowed me to notice comaparisons to hex. The hex values i noticed were:
43 4d 53 43 33 38 39 52 2d 7b 30 6e 33 5f 73 6c 4b 73 7d. Which gave me the key CMSC389R-{0n3_slKs}.

![](your_image_goes_here.png)
