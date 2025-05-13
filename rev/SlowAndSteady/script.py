import base64
def xor_strings(str1,str2):
    s = ""
    for i in range(len(str1)):
        s+=chr(ord(str1[i])^ord(str2[i]))
    return s


f = open("Original.txt",'r')
line = f.readline()
arr = []
while line != "":
    s = line[:-1]
    arr.append(s)
    line = f.readline()

f.close()
f = open("shuffle.txt",'r')
line = f.readline()
while line != "":
    pos = int(line[:-1])
    arr[pos] = xor_strings(arr[pos],arr[pos-1])
    line = f.readline()
f.close()

f = open("encoded.txt",'w')
for s in arr:
    f.write(base64.b64encode(s.encode("ascii")).decode("ascii"))
    f.write('\n')
f.close()