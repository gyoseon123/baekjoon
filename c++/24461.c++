#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;

    vector<int> indegree(n+1, 0);
    vector<vector<int>> graph(n+1);

    for (int i = 1; i < n; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
        indegree[a]++;
        indegree[b]++;
    }

    queue<vector<int>> q;
    int more_three_edge = 0;

    for (int i = 0; i <= n; i++) {
        if (indegree[i] >= 3) {
            more_three_edge++;
        }
    }

    if (more_three_edge == 0) {
        for (int i = 0; i < n; i++) {
            cout << i << ' ';
        }
        cout << endl;
        return 0;
    }

    vector<int> erase;
    for (int i = 0; i <= n; i++) {
        if (indegree[i] == 1) {
            erase.push_back(i);
            indegree[i] = 0;
        }
    }
    q.push(erase);
    bool sig = false;
    
    vector<bool> visited(n+1, false);
    while (!q.empty()) {
        vector<int> node_list = q.front();
        q.pop();

        vector<int> next_erase;
        for (int node : node_list) {
            visited[node] = true;
        }
        for (int node : node_list) {
            for (int next : graph[node]) {
                if (indegree[next] == 3) {
                    more_three_edge--;
                    if (more_three_edge == 0) {
                        sig = true;
                        break;
                    }
                }
                indegree[next]--;
                if (indegree[next] == 1) {
                    indegree[next] = 0;
                    next_erase.push_back(next);
                }
            }
            if (sig == true) {
                break;
            }
        }
        if (sig == true) break;
        q.push(next_erase);
    }

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            cout << i << ' ';
        }
    }


    return 0;
}

