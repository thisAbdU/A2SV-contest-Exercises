#include <iostream>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

std::vector<int> listFactor(int a) {
    std::vector<int> factors;
    for (int i = 1; i <= sqrt(a); i++) {
        if (a % i == 0) {
            factors.push_back(i);
            if (i != a / i) {
                factors.push_back(a / i);
            }
        }
    }
    return factors;
}

long long common_divisor(std::vector<int> nums, int n) {
    std::map<int, int> divisorFreq; 

    for (int i = 0; i < n; i++) {
        std::vector<int> factors = listFactor(nums[i]);
        for (int factor : factors) {
            divisorFreq[factor]++;
        }
    }

    long long  max = 1;
    for (const auto &pair : divisorFreq) {
        if (pair.second >= 2) {
            if (pair.first > max) {
                max = pair.first;
            }
        }
    }

    return max;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    cout << common_divisor(nums, n) << endl;
    return 0;
}
