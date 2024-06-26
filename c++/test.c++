#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<vector<int>> sudoku;

bool row(int y) {
    int cnt = 0;
    set<int> nums;
    for (int i = 0; i < 9; i++) {
        if (sudoku[y][i] == 0) {
            cnt += 1;
        }
        else {
            nums.insert(sudoku[y][i]);
        }
    }

    if (nums.size() + cnt == 9) {
        return true;
    }
    return false;
}

bool column(int x) {
    int cnt = 0;
    set<int> nums;
    for (int i = 0; i < 9; i++) {
        if (sudoku[i][x] == 0) {
            cnt += 1;
        }
        else {
            nums.insert(sudoku[i][x]);
        }
    }

    if (nums.size() + cnt == 9) {
        return true;
    }
    return false;
}

int dx[9] = {0,0,0,1,1,1,2,2,2};
int dy[9] = {0,1,2,0,1,2,0,1,2};
bool block(int x, int y) {
    x = (x/3)*3;
    y = (y/3)*3;
    int cnt = 0;
    set<int> num;
    for (int i = 0; i < 9; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (sudoku[nx][ny] == 0) {
            cnt += 1;
        }
        else {
            num.insert(sudoku[nx][ny]);
        }
    }

    if (num.size() + cnt == 9) {
        return true;
    }
    return false;
}

vector<pair<int, int>> blank;
int mc = 0;

void f(int cnt) {
    mc = max(mc, cnt);
    if (cnt == blank.size()) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cout << sudoku[i][j] << " ";
            }
            cout << endl;
        }
        exit(0);
    }

    int x = blank[cnt].first;
    int y = blank[cnt].second;
    for (int i = 1; i <= 9; i++) {
        sudoku[x][y] = i;
        if (row(x) && column(y) && block(x, y)) {
            f(cnt + 1);
        }
        sudoku[x][y] = 0;
    }
}

int main() {
    sudoku.resize(9, vector<int>(9));

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> sudoku[i][j];
        }
    }

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (sudoku[i][j] == 0) {
                blank.push_back(make_pair(i, j));
            }
        }
    }

    f(0);
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << sudoku[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}