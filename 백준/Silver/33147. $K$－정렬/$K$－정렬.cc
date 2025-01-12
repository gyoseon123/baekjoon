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
// #define ll long long
#define int long long

using namespace std;

int gcd(int a, int b){
    if (b == 0) return a;
    else return gcd(b, a%b);
}

int arr[1000000];

signed main(){
    int n,k; cin >> n >> k;
    for (int i = 0; i < n; i++) cin >> arr[i];
    int g = gcd(n,k);
    
    int flg = 1;
    for (int i = 0; i < n; i++) if (i%g != arr[i]%g) flg = 0;

    if (flg) cout << "YES";
    else cout << "NO";
    
    return 0;
}