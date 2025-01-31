#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <cstring>
#include <cmath>
#define ll long long
#define int long long

using namespace std;

int n;
int a,b,d;
int dir = 0;
int obst[101][101];
int visit[101][101][4];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    while (1){
        memset(obst, 0, sizeof obst);
        memset(visit, -1, sizeof visit);
        dir = 0;

        cin >> n;
        if (n == 0) break;

        cin >> a >> b >> d;
        for (int i = 0; i < n; i++){
            int x,y; cin >> x >> y;
            obst[x][y] = 1;
        }

        int now_x = a;
        int now_y = b;
        int cnt = 0;
        int flg = 0;

        while (1){
            int nx = now_x + dx[dir];
            int ny = now_y + dy[dir];

            if (nx < 0 || nx > 100 || ny < 0 || ny > 100){
                cout << now_x + dx[dir]*d << ' ' << now_y + dy[dir]*d << '\n';
                break;
            }

            if (obst[nx][ny]){
                if (visit[nx][ny][dir] == -1){
                    visit[nx][ny][dir] = cnt;
                } else {
                    if (!flg){
                        flg = 1;
                        d %= (cnt - visit[nx][ny][dir]);
                    }
                }
                if (d == 0){
                    cout << now_x << ' ' << now_y << '\n';
                    break;
                }
                dir += 1;
                dir %= 4;
                continue;
            }

            cnt++;
            d--;
            now_x = nx;
            now_y = ny;

            if (d == 0){
                cout << now_x << ' ' << now_y << '\n';
                break;
            }
        }
    }   

    return 0;
}