#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>
// #define ll long long
#define int long long
#define MAX 101010

using namespace std;

int n;
int pos[MAX];
int cost[MAX];

bool check(int x){
    int rem = 0;
    for (int i = 0; i < n-1; i++){
        int now = cost[i] + rem;
        if (now < x) rem = now - x - (pos[i+1] - pos[i]);
        else rem = max(0ll, now - x - (pos[i+1] - pos[i]));   
    }
    return (cost[n-1] + rem) >= x;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> pos[i] >> cost[i];
    int left = 0;
    int right = 1e9+1;

    while (left + 1 < right){
        int mid = (left+right)/2;
        if (check(mid)) left = mid;
        else right = mid;
    }

    cout << left;


    return 0;
}