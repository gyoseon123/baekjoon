#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

struct Uf{
    int n;
    vector<int> parent;
    vector<int> rank;
    
    Uf(int n){
        this->n = n;
        parent.resize(n+1);
        rank.resize(n+1);
        for (int i = 0; i <= n; i++) parent[i] = i;
    }
    
    int find(int x){
        if (parent[x] != x) return parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void merge(int a, int b){
        a = find(a);
        b = find(b);
        
        if (a == b) return;
        
        if (rank[a] < rank[b]) swap(a,b);
        parent[b] = a;
        
        if (rank[a] == rank[b]) rank[a]++;
    }
};

int n,m,q;
int board[1010][1010];
vector<vector<pair<int, int>>> query(10101);

int convert(int x, int y){
    return (x-1) * m + y-1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> q;
    for (int i = 1; i <= q; i++){
        int x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
        for (int x = x1; x <= x2; x++){
            for (int y = y1; y <= y2; y++){
                if (!board[x][y]){
                    board[x][y] = 1;
                    query[i].push_back({x,y});
                }
            }
        }
    }

    Uf uf(n * m);

    int dx[4] = {0,0,1,-1};
    int dy[4] = {1,-1,0,0};
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            if (!board[i][j]){
                for (int k = 0; k < 4; k++){
                    int ni = i + dx[k];
                    int nj = j + dy[k];
                    if (ni < 1 || ni > n || nj < 1 || nj > m) continue;
                    if (board[ni][nj]) continue;
                    uf.merge(convert(i, j), convert(ni, nj));
                }
            }
        }
    }

    set<int> s;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){
            if (!board[i][j]) s.insert(uf.find(convert(i, j)));
        }
    }

    int cnt = s.size();

    vector<int> ans;
    ans.push_back(cnt);

    for (int i = q; i >= 2; i--){
        for (auto [x,y] : query[i]){
            set<int> adj;
            vector<pair<int, int>> mg;
            for (int k = 0; k < 4; k++){
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (nx < 1 || nx > n || ny < 1 || ny > m) continue;
                if (!board[nx][ny]) {
                    adj.insert(uf.find(convert(nx, ny)));
                    mg.push_back({nx, ny});
                }
            }

            if (!adj.size()) cnt++;
            else {
                cnt -= (adj.size() - 1);
            }

            for (auto [nx,ny] : mg) uf.merge(convert(x, y), convert(nx, ny));
            board[x][y] = 0;
        }
        ans.push_back(cnt);
    }

    for (int i = q-1; i >= 0; i--) cout << ans[i] << '\n';
    
    return 0;
}