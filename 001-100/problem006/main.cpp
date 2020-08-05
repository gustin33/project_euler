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
  int n = 100;
  std::cout << difference(n)<<std::endl;
  return 0;
}
