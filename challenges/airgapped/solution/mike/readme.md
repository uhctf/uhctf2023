# airgapped 1

cyberchef

from morse

play video at 0.5 speed

read code

`..- .... -.-. - ..-. -.. .. - -....- -.. .- .... -....- -.. .- .... -....- ..-. ....- -.. . ...--`

# airgapped 2

play video at 0.2 speed

read code

`GRGRGRGRGRGBGBRGBGBRGBGRGRGRGRGBRBRGBGRGBGRBGBGRGRBRGBGRGBGRGBRGBGRGRBRGBRBGBRGBRBGRGBGBRGRGBGBRGRBGRBRB`

find solution

```py
b = ''
o1 = '1'
o2 = '0'
c = ''
for k in 'RGRGRGRGRGRGBGBRGBGBRGBGRGRGRGRGBRBRGBGRGBGRBGBGRGRBRGBGRGBGRGBRGBGRGRBRGBRBGBRGBRBGRGBGBRGRGBGBRGRBGRBRB':
    if c == '':
        c = k
    elif k == 'G':
        if c == 'B':
            b += o1
        elif c == 'R':
            b += o2
    elif k == 'R':
        if c == 'G':
            b += o1
        elif c == 'B':
            b += o2
    elif k == 'B':
        if c == 'R':
            b += o1
        elif c == 'G':
            b += o2
    c = k    
print(b)
```