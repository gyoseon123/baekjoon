#include <bits/stdc++.h>
// #define ll long long
// #define int long long

using namespace std;

int t;
int arr[10101];

bool is_p(int num){
    if (num == 0 || num == 1) return false;

    for (int i = 2; i <= sqrt(num); i++){
        if (num%i == 0) return false;
    }

    return true;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> t;
    while (t--){
        int n; cin >> n;
        for (int i = 0; i < n; i++){
            cin >> arr[i];
        }

        pair<int, int> ans;
        int mn_len = 1e9;

        for (int i = 0; i < n; i++){
            int sum = arr[i];
            for (int j = i+1; j < n; j++){
                sum += arr[j];
                if (is_p(sum) && j - i < mn_len){
                    mn_len = j - i;
                    ans = {i, j};
                }
            }
        }

        if (mn_len == (int)1e9){
            cout << "This sequence is anti-primed." << '\n';
        } else {
            cout << "Shortest primed subsequence is length " << mn_len+1 << ": ";
            for (int i = ans.first; i <= ans.second; i++) cout << arr[i] << ' ';
            cout << '\n';
        }
    }

    return 0;
}