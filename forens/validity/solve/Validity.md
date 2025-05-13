We are given a file chall.png.
![[Pasted image 20250513034448.png]]
File does not seem to open properly in image viewer. This means that the file is either not a PNG or something is wrong with the png, lets open hexed.it to check.
![[Pasted image 20250513034526.png]]
Upon closer inspection, we notice that some of the image headers are malformed. 
For instance, the IHDR header becomes IHDr. 
Knowing this, lets take another png for reference, and match the tags.
![[Pasted image 20250513034722.png]]
comparing the two pngs, we can correct the malformed headers.
IDHr -> IDHR
srgb -> sRGB
gAMA -> GAMA
![[Pasted image 20250513034852.png]]
scrolling to the end of the file, we noticed that the IEND tag is missing.
After repairing the png accordingly, we are presented with the image:
![[repaired.png]]
