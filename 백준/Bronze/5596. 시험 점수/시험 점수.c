#include <stdio.h> // a1, b1, c1, d1, a2, b2, c2, d2 선언 후 입력, x1 에 a1 ~ d1까지 합 더하기, x2에 a2 ~ d2까지의 합 더하기, 둘 중 큰 수 출력
int main(){
    int a1, b1, c1, d1, a2, b2, c2, d2;
    scanf("%d %d %d %d %d %d %d %d",&a1,&b1,&c1,&d1,&a2,&b2,&c2,&d2);
    int x1 = a1+b1+c1+d1;
    int x2 = a2 + b2 + c2 + d2;
    printf("%d", ((x1 > x2) ? x1 : x2));
    
}