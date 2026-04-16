#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,m;
int sqrtN;
int res = 0;
int a[101010];
int ans[101010];
int cnt[101010];
int cnt_cnt[101010];

struct Query{
    int s,e,idx;

    bool operator < (Query &other){
        if (s/sqrtN != other.s/sqrtN) return s/sqrtN < other.s/sqrtN;
        else return e < other.e;
    }

    Query(int s, int e, int idx) : s(s), e(e), idx(idx) {}
};

void Plus(int x){
    cnt_cnt[cnt[x]]--;
    cnt[x]++;
    cnt_cnt[cnt[x]]++;
    res = max(res, cnt[x]);
}

void Minus(int x){
    cnt_cnt[cnt[x]]--;
    if (cnt[x] == res && !cnt_cnt[cnt[x]]) res--;
    cnt[x]--;
    cnt_cnt[cnt[x]]++;
}

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

    int s = 0, e = 0;
    cnt_cnt[0] = n;

    for (int i = 0; i < m; i++){
        Query now = qry[i];
        while (s < now.s) Minus(a[s++]);
        while (s > now.s) Plus(a[--s]);
        while (e < now.e) Plus(a[++e]);
        while (e > now.e) Minus(a[e--]);
        ans[now.idx] = res;
    }

    for (int i = 0; i < m; i++) cout << ans[i] << '\n';
    
    return 0;
}