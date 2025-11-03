#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;

using namespace std;

int isSame(vector<int> a, vector<int> b, int n){
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int ans = 1;
    for (int i = 0; i < n; i++){
        if (a[i] != b[i]){
            ans = 0;
            break;
        }
    }

    return ans;
}

struct Node{
    int val, idx;
    Node *left;
    Node *right;

    Node(int val, int idx){
        left = right = NULL;
        this->val = val;
        this->idx = idx;
    }
};

struct Tree{
    Node *root;
    vector<int> nodes;

    Tree(int v){
        root = new Node(v, 1ll);
        nodes.push_back(1ll);
    }

    void insert(int x){
        Node *now = root;
        int now_idx = 1;
        while (1){
            if (x < now->val){
                if (now->left){
                    now = now->left;
                    now_idx = now_idx*2;
                } else {
                    Node *nxt = new Node(x, now_idx*2);
                    now->left = nxt;
                    nodes.push_back(nxt->idx);
                    break;
                }
            } else {
                if (now->right){
                    now = now->right;
                    now_idx = now_idx*2 + 1;
                } else {
                    Node *nxt = new Node(x, now_idx*2+1);
                    now->right = nxt;
                    nodes.push_back(nxt->idx);
                    break;
                }
            }
        }
    }
};

int n,k;
vector<Tree*> trees;

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    for (int i = 0; i < n; i++){
        int x; cin >> x;
        Tree *t = new Tree(x);
        for (int j = 0; j < k-1; j++){
            cin >> x;
            t->insert(x);
        }
        trees.push_back(t);
    }

    int ans = 0;
    for (int i = 0; i < n; i++){
        int flg = 1;
        for (int j = i+1; j < n; j++){
            if (isSame(trees[i]->nodes, trees[j]->nodes, k)){
                flg = 0;
                break;
            }
        }
        ans += flg;
    }

    cout << ans << '\n';
    
    return 0;
}