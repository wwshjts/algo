#include <stdio.h>

int div(int a, int b);
void printb(int a){
    if(a >> 1) 
        printb(a>>1);
    printf("%d", (a&1) ? 1 : 0);
}

int main(void){
    int a, b;
    scanf("%d %d", &a, &b);
    int res = div(a, b);
    printf("%d\n", res);
    return 0;
}

int div(int a, int b){
    if (a < b){
       return 0; 
    }
    int exp = 0;
    while(a - (b<<exp) >= 0)
        exp ++;
    exp--;
    return (1 << exp) + div(a - (b<<exp), b);
}