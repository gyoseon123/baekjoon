#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <cmath>

using namespace std;

int convert(int x) {
    int ret = 0;
    for (int i = 0; i < (int)log2(x) + 1; i++) {
        if (i == (int)log2(x) && (x & (1 << (int)log2(x)))) {
            ret += (1 << i);
        } else {
            bool fir = (x & (1 << i)) > 0;
            bool sec = (x & (1 << (i + 1))) > 0;
            if (fir ^ sec) {
                ret += (1 << i);
            }
        }
    }
    return ret;
}

vector<int> make_gray(int n) {
    vector<int> ret;
    for (int i = 0; i < (1 << n); i++) {
        ret.push_back(convert(i));
    }
    ret.push_back(ret[0]);
    return ret;
}

int find_diff(int a, int b) {
    int x = a ^ b;
    for (int i = 0; i < (int)log2(x) + 1; i++) {
        if (x & (1 << i)) return i;
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    int target = 1;
    bool flg = false, flg2 = false;
    vector<int> gray;
    int idx = 0, max_val = 0;
    vector<int> save;

    while (true) {
        if (flg2) {
            flg2 = false;
            unordered_map<int, int> cnt;
            unordered_set<int> rec;
            for (int x : save) cnt[x]++;
            for (auto &p : cnt) {
                if (p.second % 2 != 0) rec.insert(p.first);
            }

            bool end = false;
            while (!rec.empty()) {
                int qry;
                cin >> qry;
                if (qry == n || qry == max_val) {
                    end = true;
                    break;
                }
                cout << target << " " << *rec.begin() << endl;
                rec.erase(rec.begin());
            }
            if (end) break;
            target++;
        }

        if (!flg) {
            int fir_state;
            cin >> fir_state;
            if (fir_state == n) break;
            max_val = fir_state;

            save.clear();
            flg = true;
            gray = make_gray(n - target + 1);
            idx = 0;
        } else {
            int qry;
            cin >> qry;
            if (qry == n) break;
            if (qry >= max_val) {
                max_val = qry;
                save.clear();
            }
        }

        int ntarget = find_diff(gray[idx], gray[idx + 1]);
        cout << target << " " << target + ntarget << endl;
        save.push_back(target + ntarget);
        idx++;

        if (idx == (int)gray.size() - 1) {
            flg = false;
            flg2 = true;
        }
    }

    return 0;
}
