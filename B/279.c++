#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using ll = long long;

using namespace std;

int main(){
    ll n, t;
    cin >> n >> t;

    vector<ll> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    ll ans = 0;
    for (int i = 0; i < n; i++){
        if (t - a[i] >= 0){
            ans++;
            t -= a[i];
        } else {
            break;
        }
    }
    cout << ans << endl;
    return 0;

}