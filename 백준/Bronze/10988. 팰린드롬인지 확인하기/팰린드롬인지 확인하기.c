#include <stdio.h> // 크기 200의 char 배열 str1, str2 배열 선언, %s로 str1을 입력받음, 마지막 문자가 null인지 체크해서 문자의 길이를 n변수에 저장, for문을 n-1부터 0까지 돌려서 str2에 str1을 반대로 뒤집은 문자열 저장, for문을 다시 돌면서 두 문자열이 같은지 판단
int main(){
    char str1[200], str2[200];
    int n=0;
    scanf("%s",str1);

    while (str1[n] != '\0') {
        n++; // 위에 n 0으로 초기화 하기기
    }
    for(int i = n-1; i>=0; i--) {
        str2[i] = str1[n-1-i];
    }

    int flg = 1; // flg에 답의 여부를 처리할거임, 1이면 두 문자열이 같음, 아니면 0 for문을 돌면서 서로 다른 문자가 하나라도 나오면 flg를 0으로 바꾸기기
    for(int i=0;i<n;i++) {
        if (str1[i] != str2[i]) {
            flg = 0; // 밑에 flg 출력력
            break;
        }
    }
    printf("%d", flg);

    return 0;
}