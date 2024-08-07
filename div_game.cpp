#include <iostream>
#include <map>

using namespace std;

int count_prime(int a){
    map<int, int> factors;

    long long count = 0;

    long long i = 2;
    while (i * i <= a){
        while (a%i == 0){
            factors[i]++;
             a /= i;
        }
        
        i++;
    }

    if (a > 1){
        factors[a]++;
    }

    for(auto &pair : factors){
        long long j = 1;
        while(pair.second - j >= 0){
            count++;
            pair.second -= j;
            j += 1;
        }
    }

    return count;
}

int main(){
    int n;
    cin >> n;
    cout << count_prime(n) << endl;
    return 0;
}