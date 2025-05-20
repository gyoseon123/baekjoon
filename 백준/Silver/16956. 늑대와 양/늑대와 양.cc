#include <iostream>
#include <vector>

using namespace std;

inline void fastIo() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int main(){
    int n, m;
    bool flag = true;
    vector<string> v;

    fastIo();

    cin >> n >> m;

    v.resize(n);

    for (auto &val: v)
        cin >> val;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (v[i][j] == '.')
                v[i][j] = 'D';
            else if (v[i][j] == 'S') {
                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k], ny = j + dy[k];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m && v[nx][ny] == 'W')
                        flag = false;
                }
            }
        }
    }

    if (flag) {
        cout << 1 << '\n';
        for (const auto &val: v)
            cout << val << '\n';
    }
    else
        cout << 0 << '\n';

    return 0;

}