#include <stdio.h>
#include <stdlib.h>

int main(void) {

    int soma = 0;
    for(int i = 1; i <= 999; i++) {

        if( ((i%3) == 0) || ((i%5) == 0) ) {

            soma += i;

        }

    }

    printf("\nA soma é: %d \n", soma);


    return 0;
}