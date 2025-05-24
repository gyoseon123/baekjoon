#include <stdio.h> // 변수 n 선언 후 입력받기,  2중 for문을 사용, 첫번째 for문은 i 1부터 n까지 두 번째 for문은 j 0부터 i까지해서 별을 j개 출력, 두 번째 for문 끝 난 후 줄바꿈
int main(){
    int n;
    scanf(" %d",&n);
    for(int i = 1; i <= n; i++) {
        for(int j=0;j<i;j++)
        {
            printf("*");
        }
        printf("\n");
        

    }

    return 0;
}