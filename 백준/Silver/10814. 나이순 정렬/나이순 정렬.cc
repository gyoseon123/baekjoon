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

int n;
vector <pair<pair<int, int>, string>> arr;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++){
        int a; string s; cin >> a >> s;
        arr.push_back({{a,i},s});
    }

    sort(arr.begin(), arr.end());


    for (int i = 0; i < n; i++){
       cout << arr[i].first.first << ' ' << arr[i].second << '\n'; 
    }

    return 0;
}