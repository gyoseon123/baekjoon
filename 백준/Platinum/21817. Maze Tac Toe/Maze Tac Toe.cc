#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <math.h>

using namespace std;

int n;
vector<string> board;
vector<vector<string>> board1;
vector<vector<vector<bool>>> visited;
vector<bool> use;
unordered_map<char, int> conv = {{'O', 1}, {'M', 2}};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int ans = 0;

int check(int state) {
    if (use[state]) return -1;

    vector<int> line(8);
    line[0] = ((state / (1)) % 3) * 100 + ((state / (3)) % 3) * 10 + ((state / (9)) % 3);
    line[1] = ((state / (27)) % 3) * 100 + ((state / (81)) % 3) * 10 + ((state / (243)) % 3);
    line[2] = ((state / (729)) % 3) * 100 + ((state / (2187)) % 3) * 10 + ((state / (6561)) % 3);
    line[3] = ((state / (1)) % 3) * 100 + ((state / (27)) % 3) * 10 + ((state / (729)) % 3);
    line[4] = ((state / (3)) % 3) * 100 + ((state / (81)) % 3) * 10 + ((state / (2187)) % 3);
    line[5] = ((state / (9)) % 3) * 100 + ((state / (243)) % 3) * 10 + ((state / (6561)) % 3);
    line[6] = ((state / (1)) % 3) * 100 + ((state / (81)) % 3) * 10 + ((state / (6561)) % 3);
    line[7] = ((state / (9)) % 3) * 100 + ((state / (81)) % 3) * 10 + ((state / (729)) % 3);

    for (int l : line) {
        if (l == 211 || l == 112) {
            use[state] = true;
            return 1;
        }
    }
    return 0;
}

void solve(int x, int y, int state) {
    visited[x][y][state] = true;

    int c = check(state);
    if (c == 1) {
        ans++;
        return;
    }
    if (c == -1) {
        return;
    }

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && board1[nx][ny] != "###") {
            if (board1[nx][ny] != "...") {
                int nxt = (board1[nx][ny][1] - '1') * 3 + (board1[nx][ny][2] - '1');
                int next_state = pow(3, nxt) * conv[board1[nx][ny][0]];

                if ((state / (int)pow(3, nxt)) % 3 == 0 && !visited[nx][ny][state + next_state]) {
                    solve(nx, ny, state + next_state);
                }
                if ((state / (int)pow(3, nxt)) % 3 != 0 && !visited[nx][ny][state]) {
                    solve(nx, ny, state);
                }
            } else {
                if (!visited[nx][ny][state]) solve(nx, ny, state);
            }
        }
    }
}

int main() {
    cin >> n;
    board.resize(n);
    board1.resize(n, vector<string>(n));
    visited.assign(n, vector<vector<bool>>(n, vector<bool>(19683, false))); // 3^9 = 19683
    use.assign(19683, false);

    for (int i = 0; i < n; i++) {
        cin >> board[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n * 3; j += 3) {
            board1[i][j / 3] = board[i].substr(j, 3);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board1[i][j] == "BBB") {
                board1[i][j] = "...";
                solve(i, j, 0);
                break;
            }
        }
    }

    cout << ans << endl;
    return 0;
}
