import base64
def xor_strings(str1,str2):
    s = ""
    for i in range(len(str1)):
        s+=chr(ord(str1[i])^ord(str2[i]))
    return s

f = open("encoded.txt","r")
arr = []
line = f.readline()
while line != "":
    s = line[:-1]
    arr.append(base64.b64decode(s.encode("ascii")).decode("ascii"))
    line = f.readline()

f.close()
f = open("shuffle.txt",'r')
line = f.readline()
shuffle_list = []
while line != "":
    pos = int(line[:-1])
    shuffle_list.append(pos)
    line = f.readline()

f.close()
shuffle_list.reverse()
for i in shuffle_list:
    arr[i] = xor_strings(arr[i],arr[i-1])

for i in arr:
    print(i)
