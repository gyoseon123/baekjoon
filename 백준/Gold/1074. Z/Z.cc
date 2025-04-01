#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n,r,c;
int ans = 0;

void f(int i, int j, int cnt){ // 2^cnt * 2^cnt 
    if (cnt == 0){
        return;
    }

    int diff = (1<<(cnt-1));
    if (i + diff > c && j + diff > r){ // 왼쪽 위 사각형
        f(i, j, cnt-1);
    } else if (i + diff <= c && j + diff > r){ // 오른쪽 위 사각형
        ans += (diff * diff);
        f(i+diff, j, cnt-1);
    } else if (i + diff > c && j + diff <= r){ // 왼쪽 아래 사각형
        ans += (diff*diff*2);
        f(i, j+diff, cnt-1);
    } else { // 오른쪽 아래 사각형
        ans += (diff*diff*3);
        f(i+diff, j+diff, cnt-1);
    }
}

int main(){

    cin >> n >> r >> c;
    f(0, 0, n);
    cout << ans;

    return 0;
}