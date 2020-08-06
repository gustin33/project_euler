#include <iostream>

int difference(int n) {
    int i = 1;
    int result = 0;
    while (i <= n) {
        int j = 1;
        while (j < i) {
            result += 2*i*j;
            j++;
        }
        i++;
    }
    return result;
}

int main() {
    printf("For n = %d: %d\n",10, difference(10));
    printf("For n = %d: %d\n", 100, difference(100));
    return 0;
}
