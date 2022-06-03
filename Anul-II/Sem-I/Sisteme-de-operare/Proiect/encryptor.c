#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <time.h>
#include <ctype.h>

int RandomNumber(int nr)
{
    srand(time(NULL) + nr);   // Initialization, should only be called once.
    int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
    return r % 25 +1;
}



char* Encryptor(char *text, int perm)
{

    char *text_nou = malloc(strlen(text));
    char litera, lista_perm[] = "";
    /// perm is the permutation in which we permute a single char on ASCII

    //de facut random in UNIX si adaugat in fisier

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
    return text_nou;
}

char* Decryptor(char *encryptedWord, int asciiPerm)
{
    char *newText = malloc(strlen(encryptedWord));
    char litera;
    for (int i = 0; i < strlen(encryptedWord); ++i)
    {

        //32 is the first possible character in ASCII
        if(encryptedWord[i] == ' ')
            litera = ' ';
        else if((encryptedWord[i] + asciiPerm) <= 122)
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

    return newText;

}

int main(int argc, char* argv[])
{
    /// Encryptor ------------------------------------------------------------
    if(argc == 2)
    {
        /// read from mere.txt
        int fisier1_id = open(argv[1], O_RDONLY);
        int fisier2_id = open("encrypted.txt", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
        int fisier3_id = open("permutation.txt", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);

        //verify if we can found the file
        if(fisier1_id == -1 || fisier2_id == -1 || fisier3_id == -1)
        {
            printf("Eroare, frate!\n");
            return 0;
        }



        // to hold the text
        char* buffer = malloc(100);
        char* caracter_alocat = (char*)malloc(sizeof(char));
        while(read(fisier1_id, caracter_alocat, 1) != 0)
        {
            strncat(buffer, caracter_alocat, 1);
        }

        int j = 0;
        while(buffer[j])
        {
            buffer[j] = tolower(buffer[j]);

            j++;
        }

        unsigned int word_nr = 0;
        char newText[500][100];
        for(unsigned int i = 0; i < strlen(buffer); i++)
        {
            if(strchr("abcdefghijklmnopqrstuvwxyz", buffer[i]) != NULL)
            {
                strncat(newText[word_nr], &buffer[i], 1);
            }
            else if(strlen(newText[word_nr]) > 0)
            {
                word_nr++;
            }

            //printf("- %i - %s -\n", word_nr, newText[word_nr]);
        }
        word_nr--;

        //printf("\n\n\n");
        int perm, nr = 10;
        for(int i = 0; i <= word_nr; i++)
        {
            perm = RandomNumber(nr);
            char* someNumber = malloc(4);
            sprintf(someNumber, "%d", perm);
            write(fisier3_id, someNumber, strlen(someNumber));
            write(fisier3_id, " ", sizeof(char));
            nr++;

            char* encryptedWord = malloc(strlen(newText[i] + 1));
            encryptedWord = Encryptor(newText[i], perm);
            //printf("-%i-%s-%s-\n", perm, newText[i], encryptedWord);

            write(fisier2_id, encryptedWord, sizeof(char) * strlen(encryptedWord));
            write(fisier2_id, " ", sizeof(char));

            free(encryptedWord);
            free(someNumber);
        }

        free(caracter_alocat);
        free(buffer);
        close(fisier1_id);
        close(fisier2_id);
        close(fisier3_id);
    }

    /// Decryptor ---------------------------------------------
    else if(argc == 3)
    {
        int fisier1_id = open(argv[1], O_RDONLY);
        int fisier2_id = open(argv[2], O_RDONLY);
        int fisier3_id = open("decrypted.txt", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);

        if(fisier1_id == -1 || fisier2_id == -1 || fisier3_id == -1)
        {
            printf("Eroare, frate!\n");
            return 1;
        }

        char* buffer = malloc(100);
        char* bufferNumber = malloc(100);
        char* caracter_alocat = (char*)malloc(sizeof(char));
        while(read(fisier1_id, caracter_alocat, 1) != 0)
        {
            strncat(buffer, caracter_alocat, 1);
        }

        while(read(fisier2_id, caracter_alocat, 1) != 0)
        {
            strncat(bufferNumber, caracter_alocat, 1);
        }

        unsigned int word_nr = 0;
        char newText[500][100];
        for(unsigned int i = 0; i < strlen(buffer); i++)
        {
            if(strchr(" ", buffer[i]) != NULL)
            {
                word_nr++;
            }
            else
                strncat(newText[word_nr], &buffer[i], 1);
        }

        unsigned int word_nrNr = 0;
        char newTextNr[500][100];
        for(unsigned int i = 0; i < strlen(bufferNumber); i++)
        {
            if(strchr(" ", bufferNumber[i]) != NULL)
            {
                word_nrNr++;
            }
            else
                strncat(newTextNr[word_nrNr], &bufferNumber[i], 1);
        }

        word_nrNr--;
        word_nr--;

        for(int i = 0; i <= word_nr; i++)
        {
            int perm = atoi(newTextNr[i]);
            char* beforeDecryptedWord = malloc(strlen(newText[i] + 1));
            char* decryptedWord = malloc(strlen(newText[i] + 1));
            beforeDecryptedWord = newText[i];
            decryptedWord = Decryptor(beforeDecryptedWord, perm);
            //printf("%i\t%s\t%s\n", perm, beforeDecryptedWord, decryptedWord);
            //printf("%s\t%s\n", decryptedWord, newText[i]);

            if(i == word_nr)
                write(fisier3_id, decryptedWord, sizeof(char) * strlen(decryptedWord));
            else
            {
                write(fisier3_id, decryptedWord, sizeof(char) * strlen(decryptedWord));
                write(fisier3_id, " ", sizeof(char));
            }

            free(decryptedWord);
        }

        free(caracter_alocat);
        free(buffer);
        free(bufferNumber);
        close(fisier1_id);
        close(fisier2_id);
        close(fisier3_id);
    }
    return 0;
}

