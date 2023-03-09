#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    if (accumulate(arr.begin(), arr.end(), 0) & 1) {
        cout << -1 << endl;
        exit(0);
    }
    
    vector<vector<int>> graph(n, vector<int>(n));
    vector<pair<int, int>> edges;
    for (int i = 0; i < n; i++) {
        edges.push_back(make_pair(arr[i], i));
    }
    sort(edges.rbegin(), edges.rend());
    
    for (auto& p : edges) {
        int cost = p.first;
        int i = p.second;
        
        while (true) {
            bool updated = false;
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                if (arr[j] > 0 && graph[i][j] == 0) {
                    arr[i]--;
                    arr[j]--;
                    graph[i][j] = 1;
                    graph[j][i] = 1;
                    updated = true;
                }
                if (arr[i] == 0) break;
            }
            if (!updated) break;
        }
    }
    
    for (auto& row : graph) {
        for (int x : row) {
            cout << x << ' ';
        }
        cout << '\n';
    }
    
    return 0;
}