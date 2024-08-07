#include <stdio.h>

using namespace std;

int compute(int a, int b){
    return a *  b;
}

int main(){

    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", compute(a, b));

    return 0;
}