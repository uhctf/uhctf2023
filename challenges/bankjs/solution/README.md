# Writeup

By browsing through the source, you can see that you can get the flag from sending a tip to the admin.

The catch is that parseInt takes a string as input, but we gave it a number, which will trigger automatic type conversion.
Now, if you try 0.00000005, you'll see that the string conversion for that yields "5e-8". Now, that same string is fed as input to parseInt, which will take the first integer part, being 5.
