#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char* Encryptor(char *text)
{

    char *text_nou = malloc(strlen(text));
    char litera, lista_perm[] = "";
    printf("%s\n", text);
    /// perm is the permutation in which we permute a single char on ASCII

    //de facut random in UNIX
    int perm = 5;

    for (int i = 0; i < strlen(text); i++)
    {
        //32 is the first possible character in ASCII
        if((text[i] - perm) >= 97)
        {
            litera = text[i] - perm;
        }
        else
        {
            //we start the ASCII code from the end like this
            litera = (text[i] - perm) + 26;

        }

        //we append the encrypted letter to text_nou
        text_nou[i] = litera;
        printf("%c\n", litera);

    }
    printf("%s\n", text_nou);
    return text_nou;
}

int main(int argc, char *argv[])
{
    //if(argc == 2)
    //{
    /// read from mere.txt
    FILE* filePointer = fopen("mere.txt", "r");

    //verify if we can found the file
    if(filePointer == NULL)
    {
        printf("%s", "Can't open/find file!\n");
        return 1;
    }

    // to hold the text
    char buffer[512];

    // copy the content of mere.txt in buffer
    fgets(buffer, sizeof(buffer), filePointer);

    printf("\n%s\n", Encryptor("si"));
    //printf("%s%c", "\n", &c);
    //}
    return 0;
}
