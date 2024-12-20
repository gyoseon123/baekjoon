#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <unordered_set>

using namespace std;

int n;
stack <int> stk;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++){
        int q1;
        cin >> q1;
        if (q1 == 1){
            int q2;
            cin >> q2;
            stk.push(q2);
        } else if (q1 == 2){
            if (!stk.empty()){
                cout << stk.top() << '\n';
                stk.pop();
            } else {
                cout << -1 << '\n';
            }
        } else if (q1 == 3){
            cout << stk.size() << '\n';
        } else if (q1 == 4){
            if (stk.empty()) cout << 1 << '\n';
            else cout << 0 << '\n';
            // cout << (1 ? stk.empty() : 0) << '\n';
        } else {
            if (!stk.empty()){
                cout << stk.top() << '\n';
            } else {
                cout << -1 << '\n';
            }
        }
    }

    return 0;
}