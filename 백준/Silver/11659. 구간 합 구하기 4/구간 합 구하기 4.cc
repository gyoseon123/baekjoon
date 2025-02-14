#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;
using namespace std;


int n,m;
int a[101010];

struct node {
    node *l, *r, *p;
    int sz, mn, mx, value, sum;
} *root;

node *ptr[101010];

void Update(node *x){
    x->sz = 1;
    x->sum = x->mn = x->mx = x->value;

    if (x->l){
        node *a = x->l;
        x->sz += a->sz;
        x->sum += a->sum;
        x->mn = min(x->mn, a->mn);
        x->mx = max(x->mx, a->mx);
    }
    if (x->r){
        node *a = x->r;
        x->sz += a->sz;
        x->sum += a->sum;
        x->mn = min(x->mn, a->mn);
        x->mx = max(x->mx, a->mx);
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

node* Interval(int l, int r){
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

int Sum(int l, int r){
    node *x = Interval(l,r);
    return x->sum;
}

int Min(int l, int r){
    node *x = Interval(l,r);
    return x->mn;
}

int Max(int l, int r){
    node *x = Interval(l,r);
    return x->mx;
}

void Init(int n){
    node *x = new node;
    ptr[0] = root = x;
    x->l = x->r = x->p = NULL;
    x->sz = 1;
    x->value = -inf;
    for (int i = 1; i <= n; i++){
        ptr[i] = x->r = new node;
        x->r->p = x;
        x = x->r;
        x->l = x->r = NULL;
        x->sz = 1;
        x->value = a[i-1];
    }
    x->r = new node;
    x->r->p = x;
    ptr[n+1] = x = x->r;
    x->l = x->r = NULL;
    x->sz = 1;
    x->value = inf;
    for (int i = n+1; i >= 0; i--) Update(ptr[i]);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> a[i];
    Init(n);

    for (int i = 0; i < m; i++){
        int a,b; cin >> a >> b;
        cout << Sum(a-1, b-1) << '\n';
    }

    return 0;
}