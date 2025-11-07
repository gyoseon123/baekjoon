#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n;
int a[101010];

int find_idx(vector<stack<int>> &stk_list, int val){
    int left = -1;
    int right = stk_list.size();
    while (left + 1 < right){
        int mid = (left + right)/2;
        if (stk_list[mid].top() < val) left = mid;
        else right = mid;
    }
    return right;
}

int check(int x){
    vector<int> b;
    vector<int> sort_b;
    for (int i = 1; i <= x; i++){
        b.push_back(a[i]);
        sort_b.push_back(a[i]);
    }

    sort(sort_b.begin(), sort_b.end());

    int s_idx = 0;
    vector<stack<int>> stk_list;
    for (auto val : b){
        int idx = find_idx(stk_list, val);
        if (idx == stk_list.size()){
            stack<int> stk;
            stk.push(val);
            stk_list.push_back(stk);
        } else {
            stk_list[idx].push(val);
        }

        while (!stk_list[0].empty() && stk_list[0].top() == sort_b[s_idx]){
            stk_list[0].pop();
            s_idx++;
            if (stk_list[0].empty()){
                stk_list.erase(stk_list.begin());
            }
        }
    }

    int flg = 1;
    for (int i = 0; i < stk_list.size(); i++){
        while (!stk_list[i].empty()){
            int nxt = stk_list[i].top(); stk_list[i].pop();
            if (nxt != sort_b[s_idx++]) flg = 0;
        }
    }

    return flg;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];

    int left = 1;
    int right = n+1;
    while (left + 1 < right){
        int mid = (left+right)/2;
        if (check(mid)) left = mid;
        else right = mid;
    }

    cout << left << '\n';
    
    return 0;
}