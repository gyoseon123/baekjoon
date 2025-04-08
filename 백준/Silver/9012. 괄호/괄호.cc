/* BOJ 9012 - 괄호 문제 */

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    bool flag = true;
    int t;
    string str;
    
    cin >> t;
    while (t--) {
        stack<char> st;
        flag = true;
        cin >> str;
        for (auto& val : str) {
           if (val == '(')
              st.push(val);
           else if (!st.empty())
              st.pop();
           else
              flag = false;
        }
        if (flag && st.empty())
           cout << "YES" << '\n';
        else
           cout << "NO" << '\n';
   }

   return 0;
}