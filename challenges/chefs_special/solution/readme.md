# Solution
<!-- optionally include any relevant solution files in this folder -->
To create this challenge, the flag has been parsed by many different algorithms on CyberChef. TO find the flag, all you have to do is to reverse all steps. The steps are unknown, but by trial and error, and by trying to recognize certain algorithms or feature, if should be possible to figure it out.

The steps taken to create the challenge:
- ROT13 (Amount 15)
- To Hex
- To Binary
- To Base64
- To Hex
- To Base85 (!-u Alpahbet)
- Tar
- Zip
- Gzip
- Tar
- Generate QR
- Rotate 90 degrees (doesn't do anything)

So, to find the flag, we can use CyberChef again.
- Upload the image
- Parse QR Code
- Untar
- Gunzip
- Unzip
- Untar
- From Base85
- From Hex
- From Base64
- From Binary
- From Hex
- ROT13 (Amount 11)

Decode this string to find:
```
uhctf{i_should_have_ordered_moms_spaghetti_SW-BU6keEUw}
```