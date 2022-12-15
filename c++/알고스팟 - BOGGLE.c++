#include <iostream>

using namespace std;

bool check_word(int x, int y, string s)
{

}


int main()
{
    const int dx[8] = {1,1,1,-1,-1,-1,0,0};
    const int dy[8] = {1,0,-1,1,0,-1,1,-1};
    int test_case; cin >> test_case;
    char board[5][5];
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            cin >> board[i][j];
        }
    }
    int n; cin >> n;
    for (int i = 0; i < n; ++i)
    {
        string s; cin >> s;
        for(int j = 0; j < 5; ++j)
        {
            for(int k = 0; k < 5; ++k)
            {
                bool visited[5][5];
                check_word(j,k,s);
            }
        }
    }
}