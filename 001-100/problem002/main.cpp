#include <iostream>
using namespace std;

int main () {
    int a = 1, b = 2, sum = 0;
    while (a < 4e+6) {
        if (a % 2 == 0) {
            sum += a;
        }
        int c = a;
        a = b;
        b = c + b;
   }
    cout << sum;
    return 0;
}
