#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

const long long INF = 1e12;
vector<vector<int>> graph;
vector<int> a;
vector<bool> visited;

long long dfs(int now, int val) {
    visited[now] = true;

    long long ret = INF;
    for (int next : graph[now]) {
        if (!visited[next]) {
            ret = min(ret, dfs(next, a[next - 1]));
        }
    }

    if (now == 1) {
        if (ret == INF) {
            return val;
        } else {
            return val + ret;
        }
    }

    if (ret == INF) {
        return val;
    }

    if (ret > val) {
        return val + (ret - val) / 2;
    } else {
        return ret;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        a.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        graph.assign(n + 10, vector<int>());
        visited.assign(n + 10, false);

        vector<int> p(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            cin >> p[i];
            graph[p[i]].push_back(i + 2);
            graph[i + 2].push_back(p[i]);
        }

        cout << dfs(1, a[0]) << endl;
    }

    return 0;
}