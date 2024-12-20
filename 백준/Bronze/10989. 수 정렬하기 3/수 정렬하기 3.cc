#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>

using namespace std;

int n;
int num[10001] = {0,}; 

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++){
        int x; cin >> x;
        num[x]++;
    }

    for (int i = 1; i <= 10000; i++){
        for (int j = 0; j < num[i]; j++) cout << i << '\n';
    }

    return 0;
}