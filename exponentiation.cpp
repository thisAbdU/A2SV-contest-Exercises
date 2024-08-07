#include <iostream>

using namespace std;

const long long MOD = 1000000007LL;

long long mod_exponentiation(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    
    return result;
}

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        long long a, b;
        cin >> a >> b;
        cout << mod_exponentiation(a % MOD, b, MOD) << endl;
    }

    return 0;
}
