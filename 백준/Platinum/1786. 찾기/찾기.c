#include <stdio.h>
#include <string.h>

int pi[1010101];
char t[1010101], p[1010101];
int ans[1010101];
int ans_cnt = 0;

void getpi(int p_len){
    int j = 0;
    for (int i = 1; i < p_len; i++){
        while (j > 0 && p[i] != p[j]) j = pi[j-1];
        if (p[i] == p[j]) j++;
        pi[i] = j;
    }
}


int main(){
    
    gets(t);
    gets(p);

    int t_len = strlen(t);
    int p_len = strlen(p);
    
    getpi(p_len);

    int j = 0;
    for (int i = 0; i < t_len; i++){
        while (j > 0 && t[i] != p[j]) j = pi[j-1];
        if (t[i] == p[j]) j++;
        if (j == p_len){
            ans[ans_cnt++] = i - p_len + 2;
            j = pi[j-1];
        }
    }

    printf("%d\n", ans_cnt);
    for (int i = 0; i < ans_cnt; i++){
        printf("%d ", ans[i]);
    }

    return 0;
}