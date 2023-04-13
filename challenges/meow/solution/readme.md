# Solution
<!-- optionally include any relevant solution files in this folder -->
To solve this challenge, open the PDF-file in the attachment. After the title page, every page is filled with "MEOW"'s, or a variation of it. The solution is fairly simple: count the amount of "MEOW"'s on a page. The resulting numbers are ASCII values: find the accompanying character. Combine all to find a base64-encoded string. Decode this string, and you'll find the answer.

```
d: 100
W: 87
h: 104
j: 106
d: 100
G: 71
Z: 90
7: 55
b: 98
T: 84
N: 78
v: 118
V: 86
1: 49
9: 57
t: 116
N: 78
E: 69
t: 116
l: 108
X: 88
1: 49
R: 82
I: 73
N: 78
H: 72
R: 82
f: 102
d: 100
G: 71
g: 103
z: 122
X: 88
0: 48
1: 49
l: 108
M: 77
H: 72
d: 100
f: 102
Y: 89
z: 122
R: 82
U: 85
X: 88
1: 49
c: 99
x: 120
N: 78
T: 84
N: 78
f: 102
b: 98
T: 84
M: 77
w: 119
d: 100
3: 51
0: 48
=: 6
```

This results in the base64-string:
```
dWhjdGZ7bTNvV19tNEtlX1RINHRfdGgzX01lMHdfYzRUX1cxNTNfbTMwd30=
```

Decode this string to find:
```
uhctf{m3oW_m4Ke_TH4t_th3_Me0w_c4T_W153_m30w}
```