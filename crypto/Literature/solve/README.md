Verse 1:
It seems pretty clear from the verse, and our encrypted text that we must decode it from base64  
![image](https://github.com/user-attachments/assets/1eacf093-3cfd-41d5-9499-2f6589257cb1)  

Verse 2:
"_F0_si0rg}33ehTRHtebd_ga_Pulf_aed{fe"  
We need to split the string into groups of 3  
'_F0' '_si' '0rg' '}33' 'ehT' 'RHt' 'ebd' '_ga' '\_Pu' 'lf\_' 'aed' '{fe'   
And we need to reverse all of them  
'0F\_' 'is\_' 'gr0' '33}' 'The' 'tHR' 'dbe' 'ag\_' 'uP\_' '\_fl' 'dea' 'ef{' 

Verse 3:
The verse hints that the order of the characters in the key play some part in the encryption of the text  
It is also quite obvious to see if you pay close attention, that reordering of a few chunks might write out the flag  
Consider the position of each letter in the key in the alphabet, we get \[9, 3, 7, 11, 0, 10, 5, 2, 8, 1, 4, 6\]  
If we now reorder the chunks based on this array, i.e. '0F\_' becomes the 9th chunk, and so on, we get  
'The', '\_fl', 'ag_', 'is_', 'dea', 'dbe', 'ef{', 'gr0', 'uP_', '0F_', 'tHR', '33}'

Verse 4:
Combine the chunks together, to get  
The_flag_is_deadbeef{gr0uP_0F_tHR33}  
Flag: deadbeef{gr0uP_0F_tHR33}

