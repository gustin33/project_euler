#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int k = 0; k < 1000; k ++) {
        if (k % 3 == 0 || k % 5 == 0) {
            sum += k;
        }
    }
    printf("%d\n", sum);
    return 0;
}

