#define _CRF_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>

const int MaxN = 210;
const int MaxM = 210;
const int MaxK = 55;

int n, m, k;
char map[MaxN][MaxM];
char map2[MaxN][MaxN];

short column[MaxM][MaxN][MaxK];
short row[MaxN][MaxM][MaxK];

short left[MaxN][MaxK];
short right_[MaxN][MaxK];

short max(short a, short b) { return a > b ? a : b; }
short min(short a, short b) { return a < b ? a : b; }

void CalculateRow(int m, char *map, int _k, short row[MaxN][MaxK])
{
    // left
    left[0][0] = map[0] == '.';
    for (int i = 1; i < m; ++i) {
        if (map[i] == '*') left[i][0] = 0;
        else left[i][0] = left[i - 1][0] + 1;
    }

    for (int k = 1; k <= _k; ++k) {
        left[0][k] = 1;
        for (int i = 1; i < m; ++i) {
            if (map[i] == '*') left[i][k] = left[i - 1][k - 1] + 1;
            else left[i][k] = left[i - 1][k] + 1;
        }
    }

    // right
    right_[m - 1][0] = map[m - 1] == '.';
    for (int i = m - 2; i >= 0; --i) {
        if (map[i] == '*') right_[i][0] = 0;
        else right_[i][0] = right_[i + 1][0] + 1;
    }

    for (int k = 1; k <= _k; ++k) {
        right_[m - 1][k] = 1;
        for (int i = m - 2; i >= 0; --i) {
            if (map[i] == '*') right_[i][k] = right_[i + 1][k - 1] + 1;
            else right_[i][k] = right_[i + 1][k] + 1;
        }
    }

    // merge
    for (int i = 0; i < m; ++i) {
        if (map[i] == '*') row[i][0] = 0;
        else row[i][0] = left[i][0] + right_[i][0] - 1;
    }

    for (int k = 1; k <= _k; ++k) {
        row[0][k] = right_[0][k];
        row[m - 1][k] = left[m - 1][k];

        for (int i = 1; i < m - 1; ++i) {
            int newK = k;
            if (map[i] == '*') newK = k - 1;

            for (int leftK = 0; leftK <= newK; ++leftK) {
                int rightK = newK - leftK;
                row[i][k] = max( row[i][k], left[i - 1][leftK] + right_[i + 1][rightK] + 1 );
            }
        }

    }
}

int main()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < n; ++i) {
        scanf("%s", map[i]);
    }

    // rotate matrix (columns to rows)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            map2[j][i] = map[i][j];
    }

    for (int i = 0; i < n; ++i)
        CalculateRow(m, map[i], k, row[i]);
    for (int i = 0; i < m; ++i)
        CalculateRow(n, map2[i], k, column[i]);

    short oldret = -1;
    short retR = -1;
    short retC = -1;
    short rowObstacles = -1;
    short columnObstacles = -1;

    short ret = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int rowK = 0; rowK <= k; ++rowK) {
                int columnK = k - rowK;

                if (map[i][j] == '*') {
                    if (rowK != 0)
                        ret = max(ret, row[i][j][rowK] + column[j][i][columnK + 1] - 1);
                    if (columnK != 0)
                        ret = max(ret, row[i][j][rowK + 1] + column[j][i][columnK] - 1);
                }
                else {
                    ret = max(ret, row[i][j][rowK] + column[j][i][columnK] - 1);
                }

                if (oldret < ret) {
                    oldret = ret;
                    retR = i;
                    retC = j;
                    rowObstacles = rowK;
                    columnObstacles = columnK;
                }
            }
        }
    }

    printf("%d\n", ret);

    /*
    printf("Row = %d\n", retR);
    printf("Column = %d\n", retC);
    printf("Mapa[%d][%d] = %c\n", retR, retC, map[retR][retC]);
    printf("Row obstacles = %d\n", rowObstacles);
    printf("Column obstacles = %d\n", columnObstacles);
    */

    return 0;
}