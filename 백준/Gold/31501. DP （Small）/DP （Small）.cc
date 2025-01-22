#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
#include <map>
#define ll long long
// #define int long long

using namespace std;

int n,q;
int arr[3030];
int dp1[3030];
int dp2[3030];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> arr[i];

    dp1[0] = 1;
    for (int i = 1; i < n; i++){
        int maxx = 0;
        for (int j = 0; j < i; j++){
            if (arr[j] < arr[i]) maxx = max(maxx, dp1[j]);
        }
        dp1[i] = maxx + 1;
    }

    dp2[n-1] = 1;
    for (int i = n-2; i >= 0; i--){
        int maxx = 0;
        for (int j = n-1; j > i; j--){
            if (arr[j] > arr[i]) maxx = max(maxx, dp2[j]);
        }
        dp2[i] = maxx + 1;
    }

    for (int i = 0; i < q; i++){
        int x; cin >> x;
        cout << dp1[x-1] + dp2[x-1] - 1 << '\n';
    }

    return 0;
}