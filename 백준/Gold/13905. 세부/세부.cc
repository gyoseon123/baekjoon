#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
#define MAX 2

using namespace std;

int n,m,s,e;
vector<pair<int, int>> graph[101010]; //

void deb2(int arr[][MAX], int r, int c){
    for (int i = 0; i < r; i++){
        for (int j = 0; j < c; j++){
            cout << arr[i][j] << ' ';
        }
        cout << '\n';
    }
}

void deb1(int arr[], int n){
    for (int i = 0; i < n; i++){
        cout << arr[i] << ' ';
    }
    cout << '\n';
}

bool bfs(int start, int end, int target){
    queue <int> q;
    q.push(start);
    bool visited[101010] = {0,};
    visited[start] = true;

    while (!q.empty()){
        int now = q.front();
        q.pop();

        for (auto &edge : graph[now]){
            int next = edge.first;
            int cst = edge.second;
            if (!visited[next] && cst >= target){
                visited[next] = true;
                q.push(next);
            }
        }
    }
    
    return visited[end];
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    cin >> s >> e;

    for (int i = 0; i < m; i++){
        int u,v,c; cin >> u >> v >> c;
        graph[u].emplace_back(v, c);
        graph[v].emplace_back(u, c);
    }

    int left = 0; 
    int right = 1000001;

    while (left + 1 < right){
        int mid = (left+right)/2;

        if (bfs(s,e,mid)) left = mid;
        else right = mid;
        
    }
    
    cout << left;

    return 0;
}

