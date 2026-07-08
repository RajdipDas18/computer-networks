#include <stdio.h>
#include <string.h>

#define MAX_DATA 100
#define MAX_DIVISOR 20

int main(void)
{
    char data[MAX_DATA];
    char divisor[MAX_DIVISOR];
    char temp[MAX_DATA];
    char codeword[MAX_DATA];
    char remainder[MAX_DIVISOR];
    char quotient[MAX_DATA];

    int dataLen, divisorLen;
    int i, j;

    printf("Enter Data: ");
    scanf("%99s", data);

    printf("Enter Divisor: ");
    scanf("%19s", divisor);

    dataLen = strlen(data);
    divisorLen = strlen(divisor);

    /* Copy data to temporary array */
    strcpy(temp, data);

    /* Append zeros */
    for (i = 0; i < divisorLen - 1; i++)
    {
        temp[dataLen + i] = '0';
    }
    temp[dataLen + divisorLen - 1] = '\0';

    /* Perform CRC Division */
    for (i = 0; i < dataLen; i++)
    {
        quotient[i] = temp[i];

        if (temp[i] == '1')
        {
            for (j = 0; j < divisorLen; j++)
            {
                temp[i + j] = (temp[i + j] == divisor[j]) ? '0' : '1';
            }
        }
    }
    quotient[dataLen] = '\0';

    /* Extract remainder */
    for (i = 0; i < divisorLen - 1; i++)
    {
        remainder[i] = temp[dataLen + i];
    }
    remainder[divisorLen - 1] = '\0';

    /* Create codeword */
    strcpy(codeword, data);
    strcat(codeword, remainder);

    printf("\nQuotient : %s\n", quotient);
    printf("CRC      : %s\n", remainder);
    printf("Codeword : %s\n", codeword);

    return 0;
}