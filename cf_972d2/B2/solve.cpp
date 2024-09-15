#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(){
    int t;
    cin >> t;

    for (int i=0; i<t; i++){
        ll n,m,q;
        cin >> n >> m >> q;

        ll teachers[m];
        for (int j=0; j<m; j++)
            cin >> teachers[j];

        sort(teachers,teachers+m);

        ll david;
        for (int j=0; j<q; j++){
            cin >> david;
            
            // solve query
            if (david > teachers[m-1])
                // right wall
                cout << n-teachers[m-1] << endl;
            else if (david < teachers[0])
                // left wall
                cout << teachers[0]-1 << endl;
            else {
                // sandwiched
                // find the two teachers that sandwich him using binsearch
                ll si = 0;
                ll ei = m-1;
                ll index; // make this the number JUST lower than david
                while (si != ei) {
                    index = (si+ei)/2;

                    if (index == si)
                        break;

                    if (david > teachers[index]){
                        si = index;
                    } else {
                        ei = index-1;
                    }
                }

                ll a = teachers[si];
                ll b = teachers[si+1];
                
                ll median = (a+b)/2;
                ll ans = min(abs(a-median),abs(b-median));
                cout << ans << endl;
            }
        }


    }
}
