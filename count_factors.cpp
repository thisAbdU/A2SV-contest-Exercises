#include <iostream>
#include <map>
using namespace std;

int count(int n)
{
    map<int, int> factors;
    int count = 1;

    int i = 2;
    while (i * i <= n)
    {
        while (n % i == 0)
        {
            factors[i]++;
            n /= i;
        }
        i++;
    }

    if (n > 1)
    {
        factors[n]++;
    }

    for (auto &pair : factors)
    {
        count *= (pair.second + 1);
    }

    return count;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int num;
        cin >> num;
        cout << count(num) << endl;
    }

    return 0;
}
