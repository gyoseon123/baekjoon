#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;
using namespace std;


int n,q;
string a;

struct node {
    node *l, *r, *p;
    int sz;
    char value;
    bool inv;
} *root;

node* ptr[303030];

void Update(node *x){
    x->sz = 1;

    if (x->l){
        node *a = x->l;
        x->sz += a->sz;
    }
    if (x->r){
        node *a = x->r;
        x->sz += a->sz;
    }
}

void Rotate(node *x) {
    node *p = x->p;
    node *b;
    
    
    if (x == p->l) {
        p->l = b = x->r;
        x->r = p;
    } else {
        p->r = b = x->l;
        x->l = p;
    }
    x->p = p->p;
    p->p = x;
    if (b) b->p = p;
    (x->p ? p == x->p->l ? x->p->l : x->p->r : root) = x;
    Update(p);
    Update(x);
}

void Splay(node *x) {
    while (x->p) {
        node *p = x->p;
        node *g = p->p;
        if (g) Rotate((x == p->l) == (p == g->l) ? p : x);
        Rotate(x);
    }
}

void Kth(int k){
    node *x = root;
    k++;
    while (1){
        while (x->l && x->l->sz > k) x = x->l;
          
        if (x->l) k -= x->l->sz;
        if (!k--) break;
        x = x->r;
    }
    Splay(x);
}

void Insert(char val, int k) {
    Kth(k-1);
    node* p = root->r;
    while (p->l) p = p->l;
    p->l = new node;
    p->l->p = p;
    p = p->l;
    p->l = p->r = NULL;
    p->value = val;
    Splay(p);
}

node* Interval(int l, int r){ //입력은 0-index
    Kth(l-1);
    node *x = root;
    root = x->r;
    root->p = NULL;
    Kth(r-l);
    x->r = root;
    root->p = x;
    root = x;
    return root->r->l;
}


void Init(int n){
    node *x = new node;
    root = x;
    x->l = x->r = x->p = NULL;
    x->sz = 1;
    x->value = '!';
    x->inv = false;
    for (int i = 1; i <= n; i++){
        ptr[i] = x->r = new node;
        x->r->p = x;
        x = x->r;
        x->l = x->r = NULL;
        x->sz = 1;
        x->value = a[i-1];
        x->inv = false;
    }
    x->r = new node;
    x->r->p = x;
    x = x->r;
    x->l = x->r = NULL;
    x->sz = 1;
    x->value = '!';
    x->inv = false;
    for (int i = n; i >= 1; i--) Update(ptr[i]);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> q;
    cin >> a;
    
    Init(n);

    for (int i = 0; i < q; i++){
        int op; cin >> op;
        if (op == 1){
            char c;
            int x;
            cin >>c >> x;
            Insert(c, x-1);
        } else {
            int l,r; cin >> l >> r;
            for (int i = l; i <= r; i++){
                Kth(i-1);
                cout << root->value;
            }
            node* p = Interval(l-1, r-1)->p;
            p->sz -= p->l->sz;
            p->l->p = NULL;
            p->l = NULL;
            Splay(p);
            cout << '\n';
        }
    }

    return 0;
}