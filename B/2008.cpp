#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int i = 0;

    while (i < n && a[i] == 1) {
        i++;
    }

    if (i == n) {
        if (n == 4) {  
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
        return;
    }
   
    if (i * i == n) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
