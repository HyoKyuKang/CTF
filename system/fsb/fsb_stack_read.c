#include<stdio.h>

int main(){
    char format[0x100];

    printf("Format: ");
    scanf("%s",format);
    printf(format);

    return 0;
}