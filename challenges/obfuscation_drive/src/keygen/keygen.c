#include <openssl/sha.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ptrace.h>
#include <elf.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

char const INSANELY_SECURE_KEY_PARAM[17] = "owo_secwet_kwey?";
char const TEXT_SEGMENT_HASH[65] = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"; // replaced post-compilation

void out_of_scope_anti_debug()
{
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1)
    {
        printf("Debugging detection triggered!\n");
        exit(1);
    }
}

void out_of_scope_sha256(char const* const input_bytes, size_t const amount_bytes, char hashed_bytes[65])
{
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX    sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, input_bytes, amount_bytes);
    SHA256_Final(hash, &sha256);

    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf(hashed_bytes + (i * 2), "%02x", hash[i]);
    }
    hashed_bytes[64] = '\0';
}

// load .text segment of self, hash it, and compare to stored hash.
// https://stackoverflow.com/questions/18418839/how-can-i-get-the-offset-and-size-of-the-text-section-of-a-binary
void out_of_scope_anti_tamper(char const * const program_file)
{
    int const self_file = open(program_file, O_RDONLY);

    struct stat self_file_attributes;
    fstat(self_file, &self_file_attributes);
    char* const self_file_base_ptr = mmap(NULL, self_file_attributes.st_size, PROT_READ, MAP_SHARED, self_file, 0);

    Elf32_Ehdr * const elf_header = (Elf32_Ehdr *)self_file_base_ptr;
    Elf32_Shdr * const sections_header = (Elf32_Shdr *)(self_file_base_ptr + elf_header->e_shoff);
    int const sections_amount = elf_header->e_shnum;
    int const string_table_index_in_section_header = elf_header->e_shstrndx;

    Elf32_Shdr *string_table_section = &sections_header[string_table_index_in_section_header];
    char const * const string_table = self_file_base_ptr + string_table_section->sh_offset;

    for(size_t i = 0; i < sections_amount; i++) {
        if(!strcmp(string_table + sections_header[i].sh_name, ".text")) {
            char hashed_check_password[65];
            out_of_scope_sha256(self_file_base_ptr + sections_header[i].sh_offset, sections_header[i].sh_size, hashed_check_password);

            if (strcmp(TEXT_SEGMENT_HASH, hashed_check_password))
            {
                printf("Tamper detection triggered!\n");
                exit(1);
            }

            break;
        }
    }
}

void check_password(char const password[8])
{
    FILE* const password_file_ptr = fopen("./password", "r");
    if (NULL == password_file_ptr)
    {
        printf("Password file (`./password`) not found!\n");
        exit(1);
    }

    for (size_t i = 0; i < 8; i++)
    {
        char const c = fgetc(password_file_ptr);

        if (c != password[i])
        {
            printf("Password incorrect!\n");
            exit(1);
        }
    }
}

void keygen(char const param1[32], char const param2[16])
{
    char result[33];

    for (size_t i = 0; i < sizeof(result) - 1; i++)
    {
        size_t const j   = i % 16;
        char const   tmp = param1[i] & param2[j] ^ (255 - j);
        result[i]        = tmp;
    }

    result[32] = '\0';
    printf("%s", result);
}

int main(int const argc, char const * const argv[])
{
    out_of_scope_anti_debug();
    out_of_scope_anti_tamper(argv[0]);

    if (argc != 3)
    {
        printf("Usage: %s password filename_to_decrypt\n", argv[0]);
        exit(1);
    }

    check_password(argv[1]);

    char filename[32];
    memset(filename, 'x', sizeof(filename));
    memcpy(filename, argv[2], strlen(argv[2]));

    keygen(filename, INSANELY_SECURE_KEY_PARAM);

    return 0;
}
