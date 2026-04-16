#include <bits/stdc++.h>
#define ll long long
//#define int long long
const int inf = 1e9;

using namespace std;

int n,m,t;
char dna[1010101], marker[101];
char tmp[101];

int wrap(char c){
    if (c == 'A') return 0;
    else if (c == 'G') return 1;
    else if (c == 'C') return 2;
    else return 3;
}

struct Node{
    Node* go[4];
    Node* fail;
    int output;
    
    Node(){
        fill(go, go+4, nullptr);
        output = 0;
    }
    ~Node(){for (int i = 0; i < 4; i++) delete go[i];}
    
    void insert(const char* s){
        if (*s == '\0'){
            output++;
            return;
        }
        
        int nxt = wrap(*s);
        if (!go[nxt]) go[nxt] = new Node();
        go[nxt]->insert(s+1);
    }
};

void bfs(Node* root){
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()){
        Node* now = q.front(); q.pop();
        
        for (int i = 0; i < 4; i++){
            if (!now->go[i]) continue;

            Node* nxt = now->go[i];
            if (now == root) nxt->fail = root;
            else {
                Node* tmp = now->fail;
                while (tmp != root && !tmp->go[i]) tmp = tmp->fail;
                if (tmp->go[i]) tmp = tmp->go[i];
                nxt->fail = tmp;
                if (nxt->fail->output) nxt->output += nxt->fail->output;
            }
            q.push(nxt);
        }
    }
}


void solve(){
    cin >> n >> m;
    cin >> dna;
    cin >> marker;
    Node* root = new Node();

    set<string> s;
    for (int i = 0; i < m; i++){
        for (int j = i+1; j <= m; j++){
            strcpy(tmp, marker);
            reverse(tmp + i, tmp + j);
            if (s.count(tmp)) continue;
            root->insert(tmp);
            s.insert(tmp);
        }
    }

    bfs(root);

    Node* now = root;
    int ans = 0;
    for (int i = 0; i < n; i++){
        int nxt = wrap(dna[i]);
        while (now != root && !now->go[nxt]) now = now->fail;
        if (now->go[nxt]) now = now->go[nxt];
        ans += now->output;
    }

    cout << ans << '\n';
    delete root;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> t;
    while (t--) solve();
    
    return 0;
}