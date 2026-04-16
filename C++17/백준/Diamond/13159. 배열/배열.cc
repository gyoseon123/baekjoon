#include <bits/stdc++.h>
// #define ll long long
#define int long long
const int inf = 1e9;
using namespace std;


int n,q;
int a[303030];

struct node {
    node *l, *r, *p;
    int sz;
    int mn, mx, value, sum;
    bool inv;
} *root;

node *ptr[303030];

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

void Lazy(node *x){
    if (!x->inv) return;
    node *tmp = x->l;
    x->l = x->r;
    x->r = tmp;
    x->inv = false;
    if (x->l) x->l->inv = !x->l->inv;
    if (x->r) x->r->inv = !x->r->inv;
}


void Rotate(node *x) {
    node *p = x->p;
    node *b;
    
    Lazy(p);
    Lazy(x);
    
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
    Lazy(x);
    k++;
    while (1){
        while (x->l && x->l->sz > k) x = x->l, Lazy(x);
          
        if (x->l) k -= x->l->sz;
        if (!k--) break;
        x = x->r;
        Lazy(x);
    }
    Splay(x);
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

void Reverse(int l, int r){
    node *x = Interval(l,r);
    x->inv = !x->inv;
}

void Shift(int l, int r, int x){
    int k = r - l + 1;
    if (x > 0){
        x %= k;
        if (!x) return;
        Reverse(l, r-x);
        Reverse(r-x+1, r);
        Reverse(l, r);
    } else {
        x = -x;
        x %= k;
        if (!x) return;
        Reverse(l, l+x-1);
        Reverse(l+x, r);
        Reverse(l, r);
    }
}

void Init(int n){
    node *x = new node;
    root = x;
    x->l = x->r = x->p = NULL;
    x->sz = 1;
    x->value = 0;
    x->inv = false;
    for (int i = 1; i <= n; i++){
        ptr[i] = x->r = new node;
        x->r->p = x;
        x = x->r;
        x->l = x->r = NULL;
        x->sz = 1;
        x->value = a[i];
        x->inv = false;
    }
    x->r = new node;
    x->r->p = x;
    x = x->r;
    x->l = x->r = NULL;
    x->sz = 1;
    x->value = 0;
    x->inv = false;
    for (int i = n; i >= 1; i--) Update(ptr[i]);
}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> q;
    for (int i = 1; i <= n; i++) a[i] = i;
    Init(n);

    for (int i = 0; i < q; i++){
        int op; cin >> op;
        if (op == 1){
            int a,b; cin >> a >> b;
            cout << Min(a-1, b-1) << ' ' << Max(a-1, b-1) << ' ' << Sum(a-1, b-1) << '\n';
            Reverse(a-1, b-1);
        } else if (op == 2){
            int a,b,c; cin >> a >> b >> c;
            cout << Min(a-1, b-1) << ' ' << Max(a-1, b-1) << ' ' << Sum(a-1, b-1) << '\n';
            Shift(a-1, b-1, c);
        } else if (op == 3){
            int a; cin >> a;
            Kth(a-1);
            cout << root->value << '\n';
        } else {
            int a; cin >> a;
            Splay(ptr[a]);
            cout << root->l->sz << '\n';
        }
    }

    for (int i = 1; i <= n; i++){
        Kth(i-1);
        cout << root->value << ' ';
    }

    return 0;
}