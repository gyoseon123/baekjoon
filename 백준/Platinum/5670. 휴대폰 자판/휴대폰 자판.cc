#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,t;
string s;

struct Node{
    vector<Node*> nodes;
    char val;
    int end;

    Node(char c){
        val = c;
        end = 0;
    }
}*root;

void insert(Node* now, string s, int dep){
    if (s.length() == dep) return;

    for (auto nxt : now->nodes){
        if (nxt->val == s[dep]){
            if (dep == s.length()-1) nxt->end |= 1;
            insert(nxt, s, dep+1);
            return;
        }
    }

    Node* tmp = new Node(s[dep]);
    now->nodes.push_back(tmp);
    if (dep == s.length()-1) tmp->end |= 1;
    insert(tmp, s, dep+1);
}

int search(Node* now, string s, int dep, int cnt){
    if (s.length() == dep) return cnt;

    for (auto nxt : now->nodes){
        if (nxt->val == s[dep]) return search(nxt, s, dep+1, cnt + (((now->nodes.size() > 1) || now->end) && (now != root)));
    }

    return 0;
}

void solve(int n){
    root = new Node('!');;
    vector<string> strs;
    for (int i = 0; i < n; i++){
        cin >> s;
        strs.push_back(s);
        insert(root, s, 0);
    }

    int sum = 0;
    for (auto st : strs) {
        sum += search(root, st, 0, 0) + 1;
    }

    cout << (double)sum / n << '\n';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << fixed;
    cout.precision(2);

    while (cin >> n){
        solve(n);
    }
    
    return 0;
}