When we go into random directories, until we finally find a file, most of the content should look like "VGhlcmUgaXMgbm8gZmxhZyBoZXJl"  
This hints us that the flag is encrypted in base-64  
Remember that base-64 breaks up the string into blocks of 3 and joins that together after encoding  
If we encode "deadbeef{" into base-64, we get "ZGVhZGJlZWZ7"  
Therefore, we only need to find "ZGVhZGJlZWZ7" at the start of our string  
![image](https://github.com/user-attachments/assets/b56228ef-016a-4062-86c5-9157e3eeadbc)  
"ZGVhZGJlZWZ7dGgxNV9nNG0zXzE1X0ZVTn0K"
After decoding from base-64  
We get the flag: deadbeef{th15_g4m3_15_FUN}  
