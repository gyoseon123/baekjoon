#include <iostream>
#include <vector>

using namespace std;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int INF = 1000000000;
    vector<int> attack;
    int dp[5001][5001] = {-INF,};
    int n,a,l;
    cin >> n >> a >> l;
    for (int i = 0; i < n; i++){
        int x,y;
        cin >> x >> y;
        attack.push_back((x,y));
    }
    cout << attack[0];
    
}