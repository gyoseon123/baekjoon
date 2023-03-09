#include <iostream>
#include <vector>
using namespace std;

int max_num;
int min_num;


int cal(int now, int index,  int a, int b, int c, int d){
    if (index >= n) return 0;
    max_num = max(max_num, now);
    min_num = min(min_num, now);
    if (a >= 1){
        cal(now + nums[index], index+1, a-1,b,c,d);
    }
    if (b >= 1){
        cal(now - nums[index], index+1, a,b-1,c,d);
    }
    if (c >= 1){
        cal(now * nums[index], index+1, a,b,c-1,d);
    }
    if (d >= 1){
        cal(now / nums[index], index+1, a,b,c,d-1);
    }
    return 0;
}


vector<int> nums;
int n;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++){
        int a;
        cin >> a;
        nums.push_back(a);
    }
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    cal(nums[0], 1, a,b,c,d);
    cout << max_num << '\n';
    cout << min_num;
}