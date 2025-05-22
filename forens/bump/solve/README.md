# BUMP
Note that .bmp files are in little-endian formatting, hence chunks of 2 or 4 bytes specified will be read in reverse
1. hexedit the file
2. `42 4D 1A FF` - bmp file
3. https://en.wikipedia.org/wiki/BMP_file_format
4. 
00000000   42 4D 86 44  11 00 00 00  00 00 36 00  00 00 28 00  00 00 01 00  00 00 CC 01  00 00 01 00  18 00 FF 00 
5. Byte at 0x1E: FF
6. Set it to 00 (No compression)
7. Notice width is 1, modify address at 0x12 0x13 from 01 00 to 33 30 (specified in question)
8. Get flag
**Flag:** `deadbeef{bmp_m0re_l1k3_pmo}`