#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>

#define ll long long
using namespace std;

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> s(n);

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    ll res = LLONG_MIN;  

    for (int i = 0; i < n; i++) {
        res = max(res, s[i]);
    }

    for (int i = 0; i < n - k; i++) {
        res = max(res, s[i] + s[2 * (n - k) - 1 - i]);
    }

    cout << res << endl;

    return 0;
}
