#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    long long prefix = 0;
    long long cnt = 0;
    unordered_map<int, int> mp;
    mp[0] = 1;

    for (int num : arr)
    {   
        prefix += num;
        int mod = ((prefix % n) + n) % n;

        cnt += mp[mod];
        mp[mod]++;
    }

    cout << cnt << endl;
    return 0;
}
