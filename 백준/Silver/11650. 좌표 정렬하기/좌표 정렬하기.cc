#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <unordered_set>
using namespace std;

int n;
vector<pair<int, int>> point;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++){
        int a,b; cin >> a >> b;
        point.push_back({a,b});
    }

    sort(point.begin(), point.end());

    for (int i = 0; i < n; i++){
        cout << point[i].first << ' ' << point[i].second << '\n';
        
    }

    return 0;
}