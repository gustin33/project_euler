#include <iostream>
using namespace std;

int main() {
    unsigned long long number = 600851475143, prime = 1;  // number is not divisible by 2
    while (number != 1) {
        prime += 2;  // all primes above 2 are odd
        if (number % prime == 0) {
            while (number % prime == 0) {
                number /= prime;
            }
        }
    }
    cout << prime;
    return 0;
}
