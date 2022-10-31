# Solution
<!-- optionally include any relevant solution files in this folder -->

## build

`python hcs.py` will create two files

- `encrypt.c`: takes the flag and swaps the characters until it unreadable
- `decrypt.c`: takes the swapped flag and swaps the characters into the original flag, however, it includes a faulty swap operation

`decrypt.c` is the only file that should be given to the contestants 

## solve

`decrypt.c` has a faulty swap operation

```c
95		cx->n = cy->n;
96		cy->n = cx->n;
97
98		return;
```
this swap will not correctly set `cy->n`, both pointers will point to the same node

the fix:
```c
95		struct node *t = cx->n;
96		cx->n = cy->n;
97		cy->n = t;
98
99		return;
```
run the fixed version, and the flag will be shown