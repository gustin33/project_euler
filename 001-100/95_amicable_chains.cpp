#include <bits/stdc++.h>
using namespace std;

#define DEBUG 1 // change this to 0 to disable DEBUG mode
#if DEBUG == 1
#define DBG(x) do {cerr << #x << ": " << x << endl; } while (0)
#else
#define DBG(x)
#endif

int main() {
    int n = 16000;
    int a[n+1];
    fill_n(a, n+1, 1);
    for (int i = 2; i < n+1; i++) {
        for (int j = 2; i*j < n+1; j++) {
            a[i*j] += i;
        }
    }
    for (int i = 0; i < n+1; i++) {
        if (a[i] >= n+1) a[i] = 1;
    }
    int max_count = 0, max_element = 0;
    int i = 12496;
    // for (int i = 0; i < n+1; i++) {
        // if (a[i] != 1) {
            int count = 1, x = a[a[i]], cycle = 1;
            a[x] = 1;
            while (x != a[i] && cycle) {
                DBG(x);
                DBG(a[x]);
                DBG(a[i]);
                DBG(n+1);
                if(x == 1 || x >= n+1) {
                    cycle = 0;
                    break;
                }
                int y = x;
                x = a[x];
                a[y] = 1;
                count++;
            }
            if (count > max_count) {
                max_count = count;
                max_element = a[i];
            }
            a[i] = 1;
        // }
    // }


    // for (int i = 0; i < n+1; i++) {
    //     cout << "i: " << i << " c: " << a[i] << endl;
    // }
    DBG(max_element);
    DBG(max_count);
}
