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
	cout << smallest_multiple(10)<<endl;
	cout << smallest_multiple(20)<<endl;
	return 0;
}