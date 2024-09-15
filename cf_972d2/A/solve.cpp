#include <iostream>
#include <string>

using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i=0; i<t; i++){
        int n;
        cin >> n;

        int m = n/5;
        int an,en,in,on,un;

        switch (n % 5){
            case 0:
                an=m;
                en=m;
                in=m;
                on=m;
                un=m;
                break;
            case 1:
                an=m+1;
                en=m;
                in=m;
                on=m;
                un=m;
                break;
            case 2:
                an=m+1;
                en=m+1;
                in=m;
                on=m;
                un=m;
                break;
            case 3:
                an=m+1;
                en=m+1;
                in=m+1;
                on=m;
                un=m;
                break;
            case 4:
                an=m+1;
                en=m+1;
                in=m+1;
                on=m+1;
                un=m;
                break;
        }

        string a(an,'a');
        string e(en,'e');
        string i(in,'i');
        string o(on,'o');
        string u(un,'u');

        cout << a+e+i+o+u << endl;
    }
}
