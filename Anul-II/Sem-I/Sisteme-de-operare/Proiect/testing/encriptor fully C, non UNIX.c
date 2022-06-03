#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void Encryptor(char *text)
{

    char *text_nou = malloc(strlen(text));
    char litera, lista_perm[] = "";
    /// perm is the permutation in which we permute a single char on ASCII

    //de facut random in UNIX si adaugat in fisier
    int perm = 5;

    for (int i = 0; i < strlen(text); ++i)
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

    }
    printf("%s\n", text_nou);
}

void Decryptor(int asciiPerm, char *encryptedWord)
{
    char *newText = malloc(strlen(encryptedWord));
    char litera;
    for (int i = 0; i < strlen(encryptedWord); ++i)
    {

        //32 is the first possible character in ASCII
        if((encryptedWord[i] + asciiPerm) <= 122)
        {
            litera = encryptedWord[i] + asciiPerm;
        }
        else
        {
            //we start the ASCII code from the end like this
            litera = (encryptedWord[i] + asciiPerm) - 26;

        }

        //we append the encrypted letter to newText
        newText[i] = litera;
    }

    printf("%s\n", newText);

}

int main(int argc, char* arcv[])
{

    return 0;
}
