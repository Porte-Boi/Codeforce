#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using ll = long long;
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<ll>a(n);

    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end());
    int possibleValue = 0;

    for(int i = 0; i < n; i++){
        if (i == 0){
            possibleValue += a[i];
        }
        possibleValue += a[i];
        possibleValue /= 2;
    }
    cout << possibleValue << endl;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--){
        solve();
    }
    return 0;
}