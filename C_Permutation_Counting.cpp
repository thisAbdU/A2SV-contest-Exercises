#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int permutation_string(int n, int k, vector<int>& arr) {
    priority_queue<int, vector<int>, greater<int>> min_heap(arr.begin(), arr.end());

    while (k > 0) {
        int min_val = min_heap.top();
        min_heap.pop();
        min_heap.push(min_val + 1);
        k--;
    }

    int min_val = min_heap.top();
    int ans = 1;

    for (int i : arr) {
        if (i > min_val) {
            ans += min_val;
        } else {
            ans += min_val - 1;
        }
    }

    return ans;
}

int main() {
    int test;
    cin >> test;

    for (int t = 0; t < test; t++) {
        int n, k;
        cin >> n >> k;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cout << permutation_string(n, k, arr) << endl;
    }

    return 0;
}
