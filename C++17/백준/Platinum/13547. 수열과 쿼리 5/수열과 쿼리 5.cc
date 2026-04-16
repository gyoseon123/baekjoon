#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,m;
int sqrtN;
int a[101010];
int ans[101010];
int cnt[1010101];

struct Query{
    int s,e,idx;

    bool operator < (Query &other){
        if (s/sqrtN != other.s/sqrtN) return s/sqrtN < other.s/sqrtN;
        else return e < other.e;
    }

    Query(int s, int e, int idx) : s(s), e(e), idx(idx) {}
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];

    sqrtN = sqrt(n);
    vector<Query> qry;
    
    cin >> m;
    for (int i = 0; i < m; i++){
        int s,e; cin >> s >> e;
        qry.push_back(Query(s, e, i));
    }

    sort(qry.begin(), qry.end());

    int res = 0;
    int s = 0, e = 0;

    for (int i = 0; i < m; i++){
        Query now = qry[i];
        while (s < now.s){
            cnt[a[s]]--;
            if (cnt[a[s++]] == 0) res--;
        }
        while (s > now.s){
            if (cnt[a[--s]] == 0) res++;
            cnt[a[s]]++;
        }
        while (e < now.e){
            if (cnt[a[++e]] == 0) res++;
            cnt[a[e]]++;
        }
        while (e > now.e){
            cnt[a[e]]--;
            if (cnt[a[e--]] == 0) res--;
        } 
        ans[now.idx] = res;
    }

    for (int i = 0; i < m; i++) cout << ans[i] << '\n';
    
    return 0;
}