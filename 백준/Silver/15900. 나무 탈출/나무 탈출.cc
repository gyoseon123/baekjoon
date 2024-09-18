#include <iostream>
#include <vector>
#include <cstring> // For memset
using namespace std;

const int MAX = 1000000;
vector<int> graph[MAX + 1];
bool visited[MAX + 1];
int turn[MAX + 1];
bool is_leafnode[MAX + 1];

void dfs(int now, int depth) {
    visited[now] = true;
    turn[now] = depth;
    for (int next : graph[now]) {
        if (!visited[next]) {
            is_leafnode[now] = false;
            dfs(next, depth + 1);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    memset(visited, false, sizeof(visited));
    memset(turn, 0, sizeof(turn));
    memset(is_leafnode, true, sizeof(is_leafnode));

    is_leafnode[1] = false;
    dfs(1, 0);

    int res = 0;
    for (int i = 1; i <= n; ++i) {
        if (is_leafnode[i]) {
            res += turn[i];
        }
    }

    if (res & 1) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
