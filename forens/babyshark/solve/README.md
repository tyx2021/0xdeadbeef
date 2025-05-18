# Solve
> wire shark doo doo doo doo doo doo

Baby Shark is swimming along a Transmission Control Protocol stream, labelled 5! Can you find the flag?

From the hint, we can tell that the flag can be found in TCP (Transmission Control Protocol) stream 5.

1. Filter `tcp.stream eq 5`

2. Follow TCP stream by right clicking any of the filtered packets and then `Follow > TCP stream`

3. The flag is found in the stream, but it is encoded: `qrnqorrs{onol_funex_qbbqbbqbb}`

4. Since the flag is a basic Caesar's Cipher (ROT13), we can use CyberChef or anything to decode it (eg. `ROT13(true,true,false,13)` in CyberChef)

**Flag**: `deadbeef{baby_shark_doodoodoo}`
