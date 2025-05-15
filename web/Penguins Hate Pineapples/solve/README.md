the email box is a decoy which redirects to /# (hopefully everyone noticed lol)

in fact, all invalid links all redirect back to the main page

if we inspect element, we see this

```php
<!-- include('do_not_visit.php'); GASP! How could you have found this? -->
```

lets go to /do_not_visit.php

but we are now faced with this :(

```
Access denied.
```

whatever shall we do?

recall that developers might leave backup files in on accident, with the file extensions .phps, .php.bak, .php~

in this case, do_not_visit.php~ gives us the following

```
<?php
// developer backup, remember to obfuscate on production

echo "<h2>The Forbidden Knowledge Lies Here</h2>";
echo "<p hidden>RmxhZzogZGVhZGJlZWZ7cDNuR3UxbnNfZDNTM3J2M19iM3R0M3JfZlJ1MXR9</p>";
?>
```

decoding the value in the hidden tag in base64, we get the flag

flag: deadbeef{p3nGu1ns_d3S3rv3_b3tt3r_fRu1t}
