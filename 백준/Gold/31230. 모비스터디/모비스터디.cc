#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

vector<pair<int, int>> graph[200020];
bool result[200020];
long long d[200020];
int N, M, A, B, citycount;

void dijkstra() {
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    for(int i = 1; i <= N; i++) d[i] = 10000000000000000;
    d[A] = 0;
    pq.push({0, A});
    while(!pq.empty()) {
        auto [a, b] = pq.top();
        pq.pop();
        if(a > d[b]) continue;
        for(int i = 0; i < graph[b].size(); i++) {
            auto [x, y] = graph[b][i];
            if(d[y] > a + x) {
                d[y] = a + x;
                pq.push({d[y], y});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N >> M >> A >> B;
    for(int i = 0; i < M; i++) {
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back({c, b});
        graph[b].push_back({c, a});
    }
    dijkstra();
    //역으로 계산하면 될듯
    stack<pair<long long, int>> re;
    re.push({d[B], B});
    result[B] = true;
    while(!re.empty()) {
        auto [a, b] = re.top();
        re.pop();
        // 여기서 시간초과?
        for(int i = 0; i < graph[b].size(); i++) {
            auto [x, y] = graph[b][i];
            if(d[y] == a - x && result[y] == false) {
                re.push({a - x, y});
                result[y] = true;
            }
        }
    }
    for(int i = 1; i <= N; i++) if(result[i]) citycount++;
    cout << citycount << '\n';
    for(int i = 1; i <= N; i++) if(result[i]) cout << i << " ";
    return 0;
}