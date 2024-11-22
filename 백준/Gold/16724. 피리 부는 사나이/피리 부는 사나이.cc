#include <iostream>
#include <set>

using namespace std;

pair<int, int> parent[1010][1010];
set<pair<int, int>> s;

pair<int, int> find(pair<int, int> a) {
    if(a == parent[a.first][a.second]) return a;
    else return parent[a.first][a.second] = find(parent[a.first][a.second]);
}

void uni(pair<int, int> a, pair<int, int> b) {
    a = find(a);
    b = find(b);
    if(a != b) parent[b.first][b.second] = a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, m; cin >> n >> m;
    for(int i = 1; i <= n; i++) for(int j = 1; j <= m; j++) parent[i][j] = {i, j};
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            char x; cin >> x;
            if(x == 'U') uni({i, j}, {i - 1, j});
            else if(x == 'D') uni({i, j}, {i + 1, j});
            else if(x == 'L') uni({i, j}, {i, j - 1});
            else if(x == 'R') uni({i, j}, {i, j + 1});
        }
    }
    for(int i = 1; i <= n; i++) for(int j = 1; j <= m; j++) s.insert(find(parent[i][j]));
    cout << s.size();
    return 0;
}