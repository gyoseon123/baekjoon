#include <stdio.h> // for 문 돌려서 출력, i는 1부터 n까지 , 변수는 N으로 선언 후 입력
int main(){
    int N;
    scanf("%d",&N);

    for (int i = 1; i < N + 1; ++i) {
        printf("%d\n", i);
    }
}