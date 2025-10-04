#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,m;
int sqrtN;
int a[101010];
int ans[101010];

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

    cin >> n >> m;
    for (int i = 1; i <= n; i++) cin >> a[i];

    sqrtN = sqrt(n);
    vector<Query> qry;
    
    for (int i = 0; i < m; i++){
        int s,e; cin >> s >> e;
        qry.push_back(Query(s, e, i));
    }

    sort(qry.begin(), qry.end());

    int sum = 0;
    int s = qry[0].s;
    int e = qry[0].e;
    for (int i = qry[0].s; i <= qry[0].e; i++) sum += a[i];
    ans[qry[0].idx] = sum;

    for (int i = 1; i < m; i++){
        Query now = qry[i];
        while (s < now.s) sum -= a[s++];
        while (s > now.s) sum += a[--s];
        while (e < now.e) sum += a[++e];
        while (e > now.e) sum -= a[e--];
        ans[now.idx] = sum;
    }

    for (int i = 0; i < m; i++) cout << ans[i] << '\n';
    
    return 0;
}