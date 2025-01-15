#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;


long long n,m;
int tree[1000000];

long long cal_tree(int height){
    long long ret = 0;
    for (int i = 0; i < n; i++){
        ret += max(0, tree[i] - height);
    }
    return ret;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> tree[i];
    int low = -1;
    int hi = 1000000001;
    while (low + 1 < hi){
        int mid = (low+hi)/2;
        if (cal_tree(mid) >= m){
            low = mid;
        } else {
            hi = mid;
        }
    }
    cout << low;

    return 0;
}

