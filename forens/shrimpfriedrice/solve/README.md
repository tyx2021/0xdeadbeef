# Shrimp Fried Rice
> Are you seriously trying to convince me that this dish of rice was prepared by a shrimp? A shrimp, as in a small, aquatic crustacean with a shell and antennae? A shrimp, as in an animal that lives in the ocean and feeds on plankton and algae? A shrimp, as in a creature that has no hands, no fingers, no opposable thumbs, and no ability to manipulate tools or fire? 

Shrimp has just opened his new Restaurant named Base-64!
Herring decided to visit his friend's new restaurant, so Shrimp cooked up some fried rice for his friend.
This fried rice contains red shrimp and herring (Shrimp and Herring engages in cannibalism).
Can you ignore the red herrings, and find the ~~flag~~ shrimp?


1. Upon initial inspection, there seem to be a lot of requests to a `/flag` endpoint. Each request shows a different flag so this must be a red herring (a distraction).
2. After searching through the file we find many DNS requests for various subdomains of `reddshrimpandherring.com`. This appears to be the traffic we are looking for (as hinted in the prompt).
3. A lot of the DNS queries have a destination of 8.8.8.8. However, a subset have a destination for 18.217.1.57, which stands out like a **red** shrimp.
4. We can apply the filter `dns && ip.dst==18.217.1.57` to only see DNS requests to this IP address. 
5. If we extract each subdomain (everything before .reddshrimpandherring.com) and append them in the order they appear, we get: `ZGVhZHNocmx0c3NvIGEgNWhyMW1wIGZzMXNzMHIxczM/fQ==`
6. Since Shrimp's restaurant is named Base-64 (so all his food would be encoded in base64) and this appears to be a base 64 encoded string, we can decode the string as base64 to obtain the flag.

**Flag**: `deadshrimp{so a 5hr1mp fr13d th1s r1c3?}`




