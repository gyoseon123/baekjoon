#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

int main() {
    long long n, k;
    cin >> n >> k;

    vector<vector<long long>> board(n, vector<long long>(n));
    vector<vector<pair<long long, long long>>> point(k + 1);

    // 보드 입력 및 숫자 위치 저장
    for (long long i = 0; i < n; i++) {
        for (long long j = 0; j < n; j++) {
            cin >> board[i][j];
            point[board[i][j]].emplace_back(i, j);
        }
    }

    // 모든 숫자가 존재하는지 확인
    for (long long i = 1; i <= k; i++) {
        if (point[i].empty()) {
            cout << -1 << endl;
            return 0;
        }
    }

    const long long inf = numeric_limits<long long>::max();
    vector<long long> row(n, inf), col(n, inf);

    // 첫 번째 숫자에 대한 초기화
    for (long long i = 0; i < n; i++) {
        for (auto &[x, y] : point[1]) {
            row[i] = min(row[i], (i - x) * (i - x));
            col[i] = min(col[i], (i - y) * (i - y));
        }
    }

    // 각 숫자에 대해 최솟값 계산
    for (long long num = 2; num <= k; num++) {
        vector<tuple<long long, long long, long long>> stk;

        for (auto &[x, y] : point[num]) {
            stk.emplace_back(min(row[x], col[y]), x, y);
        }

        vector<long long> newRow(n, inf), newCol(n, inf);

        for (long long i = 0; i < n; i++) {
            for (auto &[val, x, y] : stk) {
                newRow[i] = min(newRow[i], min(newRow[i], (i - x) * (i - x)) + val);
                newCol[i] = min(newCol[i], min(newCol[i], (i - y) * (i - y)) + val);
            }
        }

        row = newRow;
        col = newCol;
    }

    // 마지막 숫자의 위치에서 최솟값 찾기
    long long ans = inf;
    for (auto &[x, y] : point[k]) {
        ans = min(ans, min(row[x], col[y]));
    }

    cout << ans << endl;
    return 0;
}
