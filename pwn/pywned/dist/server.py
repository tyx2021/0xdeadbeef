sz = 500
data = [0 for _ in range(sz)]
used = [0 for _ in range(sz)]
print("Storing flag...")
flag = 'deadbeef{REDACTED}'
print(f"{len(flag) = }")
def insert(pos, str):
    length = len(str)
    if pos + length >= sz: return "Out of bounds"
    data[pos] = length
    used[pos] = 1
    for i in range(1, len(str) + 1):
        data[pos + i] = ord(str[i-1])   
        used[pos + i] = 1
def remove(pos):
    length = data[pos]
    for i in range(pos, pos + length + 1):
        if i >= sz: break
        used[i] = 0 
def read(pos):
    length = data[pos]
    ret = ""
    for i in range(pos, pos + length + 1):
        if i >= sz: break
        ret += chr(data[i])
    return ret  
insert(sz - len(flag) - 1, flag)
print("Flag stored!")
positions = []
while True:
    print('''
Hi! Try to get the flag...
1. Read a string
2. Store a string
3. Delete a string
    ''')
    opt = int(input())
    if opt == 2:
        s = input("Input a string to store: ").strip()
        length = len(s)
        added = False
        for i in range(sz-length):
            usable = True 
            for j in range(i, i+length+1):
                if used[j]:
                    usable = False
            if usable:
                positions.append(i)
                added = True
                insert(i, s)
                break
        if added:
            print("Success!")
        else:
            print("Insufficient space, try deleting some strings.")
    elif opt == 3:
        idx = int(input("Enter a index: "))
        if idx >= len(positions):
            print("No.")
        elif idx < 0:
            print("No.")
        else:
            remove(positions[idx])
    else:
        idx = int(input("Enter a index: "))
        if idx >= len(positions):
            print("No.")
        elif idx < 0:
            print("No.")
        else:
            print(read(positions[idx]))
