#include <iostream>
#include <algorithm>
using namespace std;

long int smallest_multiple (int n) {
	long int init = 2;
	for (long int num = 3; num < n+1; num ++) {
		init *= num / (__gcd(init, num));
	}
	return init;
}

int main () {
    printf("The smallest multiple up to %d is : %ld\n",10,smallest_multiple(10));
    printf("The smallest multiple up to %d is : %ld\n",20,smallest_multiple(20));
	return 0;
}
