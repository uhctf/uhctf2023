// Kim- Jong Un C++ skills.
// We have managed to extract Kim-Jong Un's nuclear power door code by using Github's co-pilot function.
// We are 100% certain that the North Korean system runs exactly the same code. 
// But we do need the right secret key to call the function openNuclearPowerDoor()!
// Tip: There is only 1 way to get a valid secret key. Brute-forcing is not necessary, and highly discouraged.

#include <iostream>
#include <windows.h>


void foundKey(unsigned char* key)
{
    std::cout << "Congratulations, the secret key is '" << std::string((char*)key) << "'\n";
	openNuclearPowerDoor();
}

unsigned char table[28] = {0x10, 0, 0x10, 0,0,0,0x10,0x10,
                           0x10,0x10,0,0,0,0x10,0, 0x10,
                          0x10,0x10,0x10,0,0,0,0x10,0
                            ,0,0,0x10,0 };

	

int main(int argc, char* argv[])
{
    if (argc != 2)
        return -1;

    unsigned char* input = (unsigned char*) argv[1];
    if (strlen((char*)input) != 8)
        return -1;

    bool a = (input[0] >= 97 && input[1] <= 122 && ((input[0] & 0x1F) == 24));
    bool b = (((input[7] >> 1) & ~0x18) | 0x20) == input[1];
    if (a && b)
    {
        if (((input[7]*2) + 20) == (input[0]))
        {
            bool c = (input[2] & 0x155) == 0x14;
            bool d = (input[2] & 0xAA) == 0x20;
            if (!c || !d) return -1;

            uint32_t value = (input[3] << 24) | (input[4] << 16) | (input[5] << 8) | input[6];
            if ((value & 0xF) != 0xE) return -1;
            int index = 0;
            int oldValue = value;
            while (true)
            {
                if ((value & 16) != table[index]) {
                    index = 0;
                    value = oldValue;
                    continue;
                }
                value >>= 1;
                index++;
                if (index == 28)
                    break;
            }
            foundKey(input);
            return 0;
        }
        else
            return -1;
    }
    else
    {
        uint32_t sum = 0;
        if (input[4] == 0 || input[3] == 0)
            return -1;
        int g = 1;
        while (g < 1000)
        {
            g++;
            sum += (g / input[4]) + ((g - 1) / input[4]) + input[2] / input[3];
            if (sum < 10)
                g = 0;
        }
        if (sum == 0) {
            foundKey(input);
            return 0;
        }
        else
            return -1;
    }
        
}

