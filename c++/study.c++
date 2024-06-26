#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m, K;
vector<string> board;
vector<vector<int>> left_, right_, up, down;

void find_left(int i) {
    int continuous = 0;
    for (int j = 1; j < m; ++j) {
        if (board[i][j-1] == '.') {
            continuous += 1;
        } else {
            continuous = 0;
        }
        left_[j][0] = continuous;

        for (int k = 1; k < m; ++k) {
            if (board[i][j-1] == '*') {
                left_[j][k] = left_[j-1][k-1] + 1;
            } else {
                left_[j][k] = left_[j-1][k] + 1;
            }
        }
    }
}

void find_right(int i) {
    int continuous = 0;
    for (int j = m-2; j >= 0; --j) {
        if (board[i][j+1] == '.') {
            continuous += 1;
        } else {
            continuous = 0;
        }
        right_[j][0] = continuous;

        for (int k = 1; k < m; ++k) {
            if (board[i][j+1] == '*') {
                right_[j][k] = right_[j+1][k-1] + 1;
            } else {
                right_[j][k] = right_[j+1][k] + 1;
            }
        }
    }
}

void find_up(int j) {
    int continuous = 0;
    for (int i = 1; i < n; ++i) {
        if (board[i-1][j] == '.') {
            continuous += 1;
        } else {
            continuous = 0;
        }
        up[i][0] = continuous;

        for (int k = 1; k < n; ++k) {
            if (board[i-1][j] == '*') {
                up[i][k] = up[i-1][k-1] + 1;
            } else {
                up[i][k] = up[i-1][k] + 1;
            }
        }
    }
}

void find_down(int j) {
    int continuous = 0;
    for (int i = n-2; i >= 0; --i) {
        if (board[i+1][j] == '.') {
            continuous += 1;
        } else {
            continuous = 0;
        }
        down[i][0] = continuous;

        for (int k = 1; k < n; ++k) {
            if (board[i+1][j] == '*') {
                down[i][k] = down[i+1][k-1] + 1;
            } else {
                down[i][k] = down[i+1][k] + 1;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m >> K;
    board.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> board[i];
    }

    left_.assign(m, vector<int>(m, 0));
    right_.assign(m, vector<int>(m, 0));
    up.assign(n, vector<int>(n, 0));
    down.assign(n, vector<int>(n, 0));

    vector<vector<vector<int>>> row(n, vector<vector<int>>(m, vector<int>(m, 0)));
    vector<vector<vector<int>>> col(n, vector<vector<int>>(m, vector<int>(n, 0)));

    for (int i = 0; i < n; ++i) {
        find_left(i);
        find_right(i);
        for (int j = 0; j < m; ++j) {
            for (int k = 0; k < m; ++k) {
                for (int l = 0; l < k; ++l) {
                    row[i][j][k] = max(row[i][j][k], left_[j][k-l] + right_[j][l]);
                }
            }
        }
    }

    for (int j = 0; j < m; ++j) {
        find_up(j);
        find_down(j);
        for (int i = 0; i < n; ++i) {
            for (int k = 0; k < n; ++k) {
                for (int l = 0; l < k; ++l) {
                    col[i][j][k] = max(col[i][j][k], up[i][k-l] + down[i][l]);
                }
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (board[i][j] == '.') {
                for (int k = 0; k <= min(K, n+m-1); ++k) {
                    ans = max(ans, row[i][j][min(k, m-1)] + col[i][j][min(K-k, n-1)] - 1);
                }
            } else {
                for (int k = 0; k <= min(K-1, n+m-1); ++k) {
                    // cout << ans << ' ' << col[i][j][min(k, m-1)] << ' ' << col[i][j][min(K-k, n-1)] << '\n';
                    ans = max(ans, row[i][j][min(k, m-1)] + col[i][j][min(K-k, n-1)] + 1);
                }
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
