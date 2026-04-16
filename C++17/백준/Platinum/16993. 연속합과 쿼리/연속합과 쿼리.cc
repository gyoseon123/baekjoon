#include <bits/stdc++.h>
// #define ll long long
// #define int long long
const int inf = 1e9;

using namespace std;

struct Node{
    int lmax;
    int rmax;
    int allmax;
    int psum;

    Node(){}

    Node(int v){
        lmax = rmax = allmax = psum = v;
    }
};


int n,m;
int a[101010];
Node tree[404040];

Node init(int node, int start, int end){
    if (start == end){
        tree[node] = Node(a[start]);
        return tree[node];
    }

    int mid = (start+end)/2;
    Node left = init(node*2, start, mid);
    Node right = init(node*2+1, mid+1, end);
    tree[node].lmax = max(left.lmax, left.psum + right.lmax);
    tree[node].rmax = max(right.rmax, right.psum + left.rmax);
    tree[node].allmax = max(left.rmax + right.lmax, max(left.allmax, right.allmax));
    tree[node].psum = left.psum + right.psum;
    return tree[node];
}

Node qry(int node, int start, int end, int left, int right){
    if (right < start || end < left) {
        Node tmp = Node(-inf);
        tmp.psum = 0;
        return tmp;
    }
    if (left <= start && end <= right) return tree[node];

    int mid = (start+end)/2;
    Node leftN = qry(node*2, start, mid, left, right);
    Node rightN = qry(node*2+1, mid+1, end, left, right);
    Node nd;
    nd.lmax = max(leftN.lmax, leftN.psum + rightN.lmax);
    nd.rmax = max(rightN.rmax, rightN.psum + leftN.rmax);
    nd.allmax = max(leftN.rmax + rightN.lmax, max(leftN.allmax, rightN.allmax));
    nd.psum = leftN.psum + rightN.psum;
    return nd;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    init(1, 0, n-1);

    cin >> m;
    for (int i = 0; i < m; i++){
        int l, r; cin >> l >> r;
        Node q = qry(1, 0, n-1, l-1, r-1);
        cout << q.allmax << '\n';
    }
    
    return 0;
}