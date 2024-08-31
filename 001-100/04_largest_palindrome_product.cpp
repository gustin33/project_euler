#include <iostream>
#include <string>
using namespace std;

string reverse_string (string x) {
	string s = "";
	for (int i = 0; i < x.length() ;i++) {
		s = x[i] + s;
	}
	return s;
}

bool isPalindrome (long int n) {
	return to_string(n) == reverse_string(to_string(n));

}

int main() {
    long int d = 1000;
	long int k = (d-1)*(d-1);
	int flag = 0, j = 0;
	while (flag == 0) {
		if (isPalindrome(k)) {
			j = d;
			while (j > 1 && !flag) {
                cout << "k: " << k << endl;
                cout << "j: " << j << endl;
                cout << "flag: " << flag << endl;
				if (k % j == 0 && k / j < d && k/j > d/10-1) {
                    cout << "k: " << k << endl;
                    cout << "j: " << j << endl;
                    cout << "j: " << j << endl;
    				flag = 1;
				}
				j--;
			}
		}
		k--;
	}
	cout << k+1<<endl;
	return 0;
}
/*
    k: 906609
    j: 993
*/
