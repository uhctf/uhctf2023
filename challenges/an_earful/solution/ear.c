#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    char pass[] = "";
    char str[80];
    char flag[] = "uhctf{c00l-st0ry-br0_000000}";

    printf("tell me something fun!\n");
    scanf("%79s", str);

    if (strcmp(pass, str) == 0)
    {

        flag[26] = 'a';
        flag[24] = '6';
        flag[23] = '3';
        flag[22] = 'e';
        flag[21] = 'c';
        flag[25] = '6';
        flag[23] = '3';
        flag[22] = 'e';
        flag[21] = 'c';
        flag[23] = '3';
        flag[22] = 'e';
        flag[21] = 'c';
        flag[25] = '6';
        printf("Alsmost as interesting as: %s\n", flag);
    }
    else
    {
        printf("I excepted something...better\n");
    }

    return 0;
}
