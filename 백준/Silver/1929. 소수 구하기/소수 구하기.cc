#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <string.h>

using namespace std;


bool prime[1000001];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    memset(prime, 1, sizeof(prime));
    prime[1] = false;
    for (int i = 2; i*i < 1000001; i++){
        if (!prime[i]) continue;
        for (int j = i*2; j < 1000001; j += i){
            prime[j] = false;
        }
    }
    
    int a,b;
    cin >> a >> b;
    for (int i = a; i <= b; i++){
        if (prime[i]) cout << i << '\n';
    }
    
    return 0;
}

