#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;

bool compare(string a, string b){
    if (a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector <string> s;
    for (int i = 0; i < n; i++){
        string a;
        cin >> a;
        s.push_back(a);
    }
    sort(s.begin(), s.end(), compare);
    string t;
    for (int i = 0; i < n; i++){
        if (s[i] != t) cout << s[i] << '\n';
        t = s[i];
    }

    return 0;
}

