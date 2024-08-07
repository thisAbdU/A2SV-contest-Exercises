#include <iostream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

vector<pair<int, int>> factorize(int num, int k) {
    vector<pair<int, int>> factors;
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            int count = 0;
            while (num % i == 0) {
                num /= i;
                count++;
            }
            if (count % k != 0) {
                factors.push_back({i, count % k});
            }
        }
    }
    if (num > 1) {
        factors.push_back({num, 1});
    }
    return factors;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    map<vector<pair<int, int>>, int> factorCount;
    int result = 0;

    for (int i = 0; i < n; ++i) {
        vector<pair<int, int>> factors = factorize(a[i], k);

        vector<pair<int, int>> requiredFactors;
        for (const auto& factor : factors) {
            requiredFactors.push_back({factor.first, k - factor.second});
        }

        result += factorCount[requiredFactors];
        factorCount[factors]++;
    }

    cout << result << endl;

    return 0;
}
