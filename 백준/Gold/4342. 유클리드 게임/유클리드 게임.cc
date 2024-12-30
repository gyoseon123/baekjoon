#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>

using namespace std;

int a,b;

bool solve(int x, int y){
    int cnt = 0;
    
    while (y != 0){
        if (x < y){
            int tmp = x;
            x = y;
            y = tmp;
        }

        if (y == 0) break;
        if (x/y > 1) break;
        cnt++;
        x -= y;
    }

    return cnt&1;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    while (1){
        cin >> a >> b;
        if (a == 0 && b == 0) break;
        if (a == b){
            cout << "A wins" << '\n'; 
            continue;
        }
        
        if (solve(a,b)) cout << "B wins" << '\n';
        else cout << "A wins" << '\n';
    }
    
    return 0;
}