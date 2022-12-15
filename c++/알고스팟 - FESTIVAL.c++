#include <iostream>
using namespace std;

int main()
{
    cout << fixed;
    cout.precision(10);
    int c;
    cin >> c;
    while (c--)
    {
        int n,l;
        cin >> n >> l;
        int cost[1001] = {};
        double min = 101;
        for (int i = 0; i < n; ++i) cin >> cost[i];
        for(int i = 0; i < n-l+1; ++i)
        {
            int sum = 0;
            for (int j = i; j < n; ++j)
            {
                sum += cost[j];
                if(j-i+1 >= l)
                {
                    double avg = sum*1.0/(j-i+1);
                    if (avg < min) min = avg;
                }
            }
        }
        cout << min << '\n';
    }
}