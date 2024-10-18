#include <bits/stdc++.h>
#include <string>
#include <algorithm>

using namespace std;

void solve(){
    string s, t;
    cin >> s >> t;

    int m = 0;
    int len_s = s.length();
    int len_t = t.length();

    for (int i = 1; i <= min(len_s, len_t); i++){
        if (s.substr(0, i) == t.substr(0, i)){
            m = i;
        }
    }

    cout << len_s + len_t - max(m, 1) + 1 << endl;
}

int main(){
    int n;
    cin >> n;
    while (n--){
        solve();
    }
    return 0;
}