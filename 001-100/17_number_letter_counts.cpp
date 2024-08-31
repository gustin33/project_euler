#include <iostream>
using namespace std;
/*
This was a strenuous problem:
Basically one has to note that for every n in 13 to 19 you add the number of
letters in n-10 + 4=number of letters in 'teen', with some exceptions.
For numbers of the form 10*n with n=2,...9 you do the same, this time adding 2=# letters in 'ty'.
For a random number abc you must add:
g(a) + g(100) + 3 + g(bc)
Where g is the function that takes a number and outputs the number of letters of said number.
The 3 comes from the 'and' part.
If bc=00, then g(bc) = 0.
*/

int g(int a) {
    if (a <= 99)
        if (a <= 10) {
            if (a < 3 || a == 6 || a == 10) return 3;
            else if (a == 4 || a == 5 || a == 9) return 4;
            else return 5;
        } else if (10 < a < 13 || a == 20) return 6;
        else if (a == 18 || a == 13 || a == 15) return g(a-10) + 3;
        else if (16 <= a <= 17 || a == 19 || a == 14) return g(a-10) + 4;
        else if (a == 60 || a == 70 || a == 90) return g(a/10)+2;
        else if (a == 30 || a == 80 || a == 40 || a == 50) return g(a/10) + 1;
        else return g(10*(a/10)) + g(a-10*(a/10));
    else if (a == 1000) return g(1) + 8;
    else if (a == 100 || a == 200 || a == 300 || a == 400 || a == 500 || a == 600 || a == 700 || a == 800 || a == 900) return g(int(a/100)) + 7;
    else return g(a/100) + 10 + g(a - 100*(a/100));

}
int main(){
    int s = 0;
    for(int i=0; i < 1001; i ++) s+=g(i);
    cout << s << endl;
}

