#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <cstring>
#include <math.h>
// #define ll long long
#define int long long

using namespace std;

int now = 0;
int n;
int nl;
bool flg = 0;

int check(int a, int b){
    int cnt[10] = {0,};
    while (a){
        cnt[a%10]++;
        a /= 10;
    }
    while (b){
        cnt[b%10]++;
        b /= 10;
    }

    for (int i = 0; i < 10; i++) if (cnt[i] > 1) return 0;
    return 1;
}

int check1(int x, int tgt){
    while (x){
        if (x%10 == tgt) return 1;
        x /= 10;
    }
    return 0;
}

int solve(int cnt){
    if (flg) return 0;

    if (cnt == nl){
        if (now >= n || now <= 0 || n - now >= n || n - now <= 0) return 0;

        if (check(now, n - now)){
            cout << now << " + " << n - now;  
            flg = 1;
        } 
        
        return 0;
    }

    for (int i = 0; i < 10; i++){
        if (check1(now, i)) continue;
        now += (i*(pow(10, nl-cnt-1)));
        solve(cnt+1);
        now -= (i*(pow(10, nl-cnt-1)));
    }

    return 0;
}

signed main(){
    cin >> n;
    int x = n;
    while (x){
        nl++;
        x /= 10;
    }

    solve(0);
    if (!flg) cout << -1;

    return 0;
}