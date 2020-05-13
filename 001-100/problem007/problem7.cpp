#include <iostream>

bool isPrime (int n) {
  if (n % 2 == 0) {
    if (n > 2) {
      return false;
    }
    return true;
  }
  int m = 3;
  while (m * m <= n) {
    if (n % m == 0) {
      return false;
    }
    m += 2;
  }
  return true;
}

int nth_prime(int n) {
  if (n == 1) {
    return 2;
  }
  int counter = 2;
  int number = 3;
  while (counter <= n) {
    if (isPrime(number)) {
      counter ++;
    }
    number += 2;
  }
  return number-2;
}

int main() {
  int n = 10001;
  std::cout << nth_prime(n) << std::endl;
  return 0;
}
