#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_set>
#include <cmath>

using namespace std;

int k;
stack <int> stk;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> k;

    for (int i = 0; i < k; i++){
        int x; cin >> x;
        if (x == 0) stk.pop();
        else stk.push(x);
    }
    int ans = 0;
    int s = stk.size();
    for (int i = 0; i < s; i++){
        ans += stk.top();
        stk.pop();
    }

    cout << ans;

    return 0;
}