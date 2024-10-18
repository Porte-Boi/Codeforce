#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end(), greater<int>());

    cout << a[(n + 1) / 2 - 1] << endl;
}

int main(){
    int t;
    cin >> t;
    while (t--){
        solve();
    }
    return 0;
}
