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

int k,n;
int id = 1;
int scc_cnt = 1;
stack<int> stk;
int parent[20202];
int visit[20202];
vector<int> graph[20202];

int oppo(int x){
    return (x&1) ? (x+1) : (x-1);
}

int find_scc(int now){
    int ret = parent[now] = id++;
    stk.push(now);

    for (auto next : graph[now]){
        if (!parent[next]) ret = min(ret, find_scc(next));
        else if (!visit[next]) ret = min(ret, parent[next]);
    }

    if (ret == parent[now]){
        while (1){
            int next = stk.top();
            stk.pop();
            visit[next] = scc_cnt;
            if (now == next) break;
        }
        scc_cnt++;
    }

    return ret;
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> k >> n;
    for (int i = 0; i < n; i++){
        int a,b,c;
        string s1,s2,s3;
        cin >> a >> s1 >> b >> s2 >> c >> s3;
        if (s1 == "R") a = a*2;
        else a = a*2-1;
        if (s2 == "R") b = b*2;
        else b = b*2-1;
        if (s3 == "R") c = c*2;
        else c = c*2-1;

        graph[oppo(a)].push_back(b);
        graph[oppo(a)].push_back(c);
        graph[oppo(b)].push_back(a);
        graph[oppo(b)].push_back(c);
        graph[oppo(c)].push_back(a);
        graph[oppo(c)].push_back(b);
    }

    for (int i = 1; i <= 2*k; i++){
        if (!parent[i]) find_scc(i);
    }

    int ans = 1;

    for (int i = 1; i <= k; i++){
        if (visit[i*2-1] == visit[i*2]) ans = 0;
    }

    if (!ans) cout << -1;
    else{
        for (int i = 1; i <= k; i++){
            if (visit[i*2-1] < visit[i*2]) cout << "B";
            else cout << "R";
        }
    }
    
    return 0;
}