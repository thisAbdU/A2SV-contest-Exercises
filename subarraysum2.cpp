#include <iostream>
#include <unordered_map>
#include <vector>

int main()
{
    using namespace std;

    int n, x;
    cin >> n >> x;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }

    int prefix = 0;
    unordered_map<int, int> check;
    check[0] = 1;
    int cnt = 0;

    for (int num : arr)
    {
        prefix += num;
        cnt += check[prefix - x];
        check[prefix]++;
    }

    cout << cnt << endl;

    return 0;
}
