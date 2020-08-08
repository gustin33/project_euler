#include <iostream>
using namespace std;
#define DEBUG 1 // change this to 0 to disable DEBUG mode
#if DEBUG == 1
#define DBG(x) do {cerr << #x << ": " << x << endl; } while (0)
#else
#define DBG(x)
#endif

bool isPrime(int n) {
    if (n == 1) return false;
    else if (n < 4) return true;
    else if (n % 2 == 0) return false;
    else if (n < 9) return true;
    else if (n % 3 == 0) return false;
    else {
        int f = 5;
        while (f*f <= n) {
            if (n % f == 0 || n % (f+2) == 0) return false;
            f+=6;
        }
    }
    return true;
}

int main() {
    int limit = 10001, count = 1, cand = 1;
    do {
        cand += 2;
        if (isPrime(cand)) count++;
    }while (count < limit);
    printf("%d\n", cand);
}
