#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n;
int a[101010];

int solve(int left, int right){
    if (left == right) return a[left];

    int mid = (left+right)/2;
    int r_ret = solve(left, mid);
    int l_ret = solve(mid+1, right);    

    int l_max = -inf;
    int r_max = -inf;
    int sum = 0;

    for (int l = mid; l >= left; l--){
        sum += a[l];
        l_max = max(l_max, sum);
    }

    sum = 0;
    for (int r = mid+1; r <= right; r++){
        sum += a[r];
        r_max = max(r_max, sum);
    }

    return max(l_max + r_max, max(l_ret, r_ret));
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << solve(0, n-1);

    return 0;
}