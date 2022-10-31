#!/bin/python
from random import randint

flag = "uhctf{A Hasselt City Shuffle is when everybody looks right, you go left.-14c7109529D3E74feD8c}"
swapped_flag = flag

header = """
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node
{
	char c;
	struct node *n;
};

struct node *loadMessage(char *message)
{
	struct node *head = NULL;
	struct node *p = head;
	for (int i = 0; i < strlen(message); i++)
	{
		struct node *t = (struct node *)malloc(sizeof(struct node));
		t->c = message[i];
		t->n = NULL;

		if (p == NULL)
		{
			head = t;
			p = t;
		}
		else
		{
			p->n = t;
			p = t;
		}
	}
	return head;
}

void printFlag(struct node *flag, FILE *fp)
{
	struct node *p = flag;
	while (p != NULL)
	{
		fprintf(fp, \"%c\", p->c);
		p = p->n;
	}
	fprintf(fp, \"\\n\");
	return;
}
"""

good_swap = """
void swap(struct node **h, int x, int y)
{
	if (x == y)
	{
		return;
	}

	int xi = 0;
	struct node *px = NULL, *cx = *h;
	while (cx && xi != x)
	{
		px = cx;
		cx = cx->n;
		xi++;
	}

	int yi = 0;
	struct node *py = NULL, *cy = *h;
	while (cy && yi != y)
	{
		py = cy;
		cy = cy->n;
		yi++;
	}

	if (cx == NULL || cy == NULL)
	{
		return;
	}

	if (px != NULL)
	{
		px->n = cy;
	}
	if (py != NULL)
	{
		py->n = cx;
	}
	if (px == NULL)
	{
		*h = cy;
	}
	if (py == NULL)
	{
		*h = cx;
	}

	struct node *t = cx->n;
	cx->n = cy->n;
	cy->n = t;

	return;
}
"""

bad_swap = """
void swap(struct node **h, int x, int y)
{
	if (x == y)
	{
		return;
	}

	int xi = 0;
	struct node *px = NULL, *cx = *h;
	while (cx && xi != x)
	{
		px = cx;
		cx = cx->n;
		xi++;
	}

	int yi = 0;
	struct node *py = NULL, *cy = *h;
	while (cy && yi != y)
	{
		py = cy;
		cy = cy->n;
		yi++;
	}

	if (cx == NULL || cy == NULL)
	{
		return;
	}

	if (px != NULL)
	{
		px->n = cy;
	}
	if (py != NULL)
	{
		py->n = cx;
	}
	if (px == NULL)
	{
		*h = cy;
	}
	if (py == NULL)
	{
		*h = cx;
	}

	cx->n = cy->n;
	cy->n = cx->n;

	return;
}
"""

flag_header = "#define FLAG "

main = """
int main(int argc, char const *argv[])
{
	fprintf(stdout, \"Let's do the ✨🎶Hasselt City Shuffle🕺🌟!\\n\");

	struct node *flag = loadMessage(FLAG);
	struct node **fh = &flag;
"""

footer = """
	printFlag(flag, stdout);

	return 0;
}
"""

swaps = []
swap_amount = 999
min = 0
max = len(flag)-1

def swap(str, i, j):
   list1 = list(str)
   list1[i], list1[j] = list1[j], list1[i]
   return ''.join(list1)

for i in range(swap_amount):
	x = randint(min,max)
	y = randint(min,max)

	swapped_flag = swap(swapped_flag, x, y)
	
	swaps.append("\tswap(fh, {}, {});\n".format(x,y))

with open("encrypt.c", 'w') as fd:
	fd.write(header)
	fd.write(good_swap)
	fd.write(flag_header + '"' + flag + '"')
	fd.write(main)
	for s in swaps:
		fd.write(s)
	fd.write(footer)

with open("decrypt.c", 'w') as fd:
	fd.write(header)
	fd.write(bad_swap)
	fd.write(flag_header + '"' + swapped_flag + '"')
	fd.write(main)
	swaps.reverse()
	for s in swaps:
		fd.write(s)
	fd.write(footer)