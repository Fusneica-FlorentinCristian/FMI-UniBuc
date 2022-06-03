#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
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

    unsigned int word_nr = 0;
    char newText[500][100];
    for(unsigned int i = 0; i < strlen(buffer); i++)
    {
        if(strchr(", ./;'\[]`1234567890-=~!@#$%^&*()_+{}:|<>?\"", buffer[i]) != NULL)
        {
            if(strlen(newText[word_nr]) > 0)
            {
                word_nr++;
            }
        }
        else
        {
            strncat(newText[word_nr], &buffer[i], 1);
        }
    }

    printf("%s", newText[1]);
    return 0;
}
