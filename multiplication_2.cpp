#include <iostream>

using namespace std;

    const long long LIMIT = 1000000000000000000LL;

    long long compute(int arr[], int n)
    {   
        long long res = 1;
        for (int i = 0; i < n; ++i)
        {
            if (res > LIMIT / arr[i])
            {
                return -1;
            }
            res *= arr[i];
        }
        return res;
    }

    int main()
    {
        int n;
        std::cin >> n;

        int* arr = new int[n];
        for (int i = 0; i < n; ++i)
        {
            std::cin >> arr[i];
        }

        long long res = compute(arr, n);
        std::cout << res << std::endl;

        delete[] arr;
        return 0;
    }


