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
#include <cmath>
// #define ll long long
#define int long long

using namespace std;

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    int t; cin >> t;

    while (t--){
        int s,x; cin >> s >> x;
        if ((s - x)&1 || s < x || (x & ((s-x)/2))){
            cout << 0 << '\n';
            continue;
        }
    
        int ans = 1;
        for (int i = 0; i <= 60; i++){
            if (x & (1ll << i)) ans <<= 1;
        }
    
        cout << ans << '\n';
    }

    return 0;
}