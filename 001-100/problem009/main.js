var n = 1000, a = 1, b = 1, c = 1;
var flag = false;
while (b < n && !flag) {
    a = 1;
    while (a < b && c >= 0 && !flag) {
        c = n - a - b;
        if (a*a + b*b == c*c) {
            flag == true;
            console.log(a*b*c);
        }
        a++;
    }
    b++;
}
