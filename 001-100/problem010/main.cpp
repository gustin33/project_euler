#include <vector>
#include <iostream>
int sum(std::vector<int> v){
  int result = 0;
  for (int i = 0; i < v.size(); i ++) {
    result += v[i];
  }
  return result;
}

int summation_of_primes(int n) {
  std::vector<int> primes = {2};
  int num = 3, flag = 1;
  while (num < n) {
    for (int i = 0; i < primes.size(); i ++) {
      if (num % primes[i] == 0) {
        flag = 0;
        break;
      }
    }
    if (flag == 1) {
      primes.push_back(num);
    }
  num += 2;
  }
  return sum(primes);
}

int main () {
  long int n = 2*10^6;
  std::cout << summation_of_primes(n)<<std::endl;
  return 0;
}
