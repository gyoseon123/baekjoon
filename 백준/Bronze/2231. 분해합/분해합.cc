#include <iostream>
#include <algorithm>

using namespace std;

int n;

int f(int num){ // 자리수 더해서 return
    int ret = 0;

    while (num){
        ret += num%10;
        num /= 10;
    }

    return ret;
}

int main(){
    cin >> n;

    int flg = 0;

    for (int i = 1; i <= 1000000; i++){
        if (i + f(i) == n){
            cout << i;
            flg = 1;
            break;
        }
    }

    if (!flg){
        cout << 0;
    }

    return 0;
}