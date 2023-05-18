#include <stdio.h>

void flag(int access) {
    if (access == 0x0079656b) {
        printf("Knight: My apologies. Please enter.\n");
        puts("/!\\ Repeat the attack on the server to get the flag. /!\\");
    } else {
        printf("Knight: Begone!\n");
    }
}

void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main() {
    setup();

    printf("Knight: Halt! We will not let you trample upon the majesty's magical number.\n");
    printf("DM: The castle guard stops you. What will you do?\n");
    printf(">>> ");

    char input[32];
    int key = 0x00636261;
    gets(input);

    flag(key);

    return 0;
}