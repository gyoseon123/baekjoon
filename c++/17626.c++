#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> squared_1;
    vector<int> squared_2;
    int n; cin >> n;
    for (int i = 1; i < int(sqrt(50000))+1; ++i)
    {
        int x = pow(i,2);
        if (x == n)
        {
            cout << 1;
            return 0;
        }
        squared_1.push_back(pow(i,2));
    }
    for (int i = 0; i < squared_1.size(); ++i)
    {
        for(int j = 0; j < squared_1.size(); ++j)
        {
            int x = squared_1[i]+squared_1[j];
            if (x == n)
            {
                cout << 2;
                return 0;
            }
            if (x < 50000) squared_2.push_back(x);
        }
    }
    for (int i = 0; i < squared_1.size(); ++i)
    {
        for (int j = 0; j < squared_2.size(); ++j)
        {
            int x = squared_1[i] + squared_2[j];
            if (x == n)
            {
                cout << 3; 
                return 0;
            }
        }
    }
    cout << 4;
}