#include <iostream>
#include <cmath>

using namespace std;
typedef long long ll;

int main(){
    int t;
    cin >> t;

    for (int i=0; i<t; i++){
        ll n,m,q;
        cin >> n >> m >> q;

        ll a,b;
        cin >> a >> b;

        ll david;
        cin >> david;
           
        // find the distance between david and the two closest wall/teacher 
        if ((a < david && david < b) || (b < david && david < a)){
            // sandwiched
            ll median = (a+b)/2;
            ll ans = min(abs(a-median),abs(b-median));
            cout << ans << endl;

        } else if (a < david && b < david)
            // david at right wall
            cout << n-max(a,b) << endl;

        else if (david < a && david < b)
            // david at left wall
            cout << min(a,b)-1 << endl;
    }
}
