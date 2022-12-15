#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;

int gcd(int a,int b)
{
    while (b != 0)
    {
        int r = a%b;
        a = b; 
        b = r;
    }
    return a;
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout << fixed;
    cout.precision(10);
    double xa,ya,xb,yb,xc,yc;
    cin >> xa >> ya >> xb >> yb >> xc >> yc;
    int na = abs(yb-ya),nb = abs(xb-xa),nc = abs(yc-yb),nd = abs(xc-xb);
    int x = gcd(na,nb), y = gcd(nc,nd);
    na /= x;
    nb /= x;
    nc /= y;
    nd /= y; 
    if ((xa == xb && xb == xc) || (ya == yb && yb == yc) || ((na == nc)&&(nb == nd)))
    {
        cout << -1.0;
        return 0;
    } 
    double a,b,c;
    a = sqrt(pow(abs(xa-xb),2)+pow(abs(ya-yb),2));
    b = sqrt(pow(abs(xb-xc),2)+pow(abs(yb-yc),2));
    c = sqrt(pow(abs(xa-xc),2)+pow(abs(ya-yc),2));
    double shape_a,shape_b,shape_c;
    shape_a = (a+b)*2;
    shape_b = (b+c)*2;
    shape_c = (c+a)*2;
    cout << max(shape_a,max(shape_b,shape_c)) - min(shape_a,min(shape_b,shape_c));
}