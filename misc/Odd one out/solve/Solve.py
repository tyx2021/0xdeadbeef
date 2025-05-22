def xor_strings(str1,str2):
    s = ""
    for i in range(len(str1)):
        s+=chr(ord(str1[i])^ord(str2[i]))
    return s
f = open("flags.txt",'r')
line = f.readline()
ans = line[:-1]
line = f.readline()
while line != "":
    ans=xor_strings(ans,line[:-1])
    line = f.readline()
print(ans)
