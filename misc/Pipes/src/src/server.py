import random
flag = 'deadbeef{1_l0v3_p1p1ng}'
not_the_flag = ["This is a string", "This is also a string", "The flag isn't here guys", "Neither is the flag here"]
for i in range(0,5000):
    x = random.randint(0,3)
    print(not_the_flag[x])
print(flag)
for i in range(0,5000):
    x = random.randint(0,3)
    print(not_the_flag[x])
