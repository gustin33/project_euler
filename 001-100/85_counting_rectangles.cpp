#include <cmath>
#include <stdio.h>

int main() {
    int m = 2e6;
    int n = 1;
    int min_n = 0, min_k = 0;
    int min_diff = m;
    while (n <= 2000) {
        int k = 1;
        do {
            if (abs((n*(n+1)/2)*(k*(k+1)/2) - m) < min_diff) {
                min_n = n;
                min_k = k;
                min_diff = abs((n*(n+1)/2)*(k*(k+1)/2) - m);
            }
            k++;
        } while ((n*(n+1)/2)*(k*(k+1)/2) < m);
        n++;
    }
    printf("%d\n", min_n*min_k);
}
