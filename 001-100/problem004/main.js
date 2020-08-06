function reverse_string (x) {
    var s = "";
    for (var i = 0; i < x.length; i++) {
        s = x[i] + s;
    }
    return s;
}

function isPalindrome(n) {
    return n.toString() == reverse_string(n.toString());
}
var d = 1000;
var k = (d-1)*(d-1);
var flag = 0, j = 0;
while (flag == 0) {
    if (isPalindrome(k)) {
        j = d;
        while (j > 1) {
            if (k%j == 0 && k/j < d && k/j > (d-10)/10){
                flag = 1;
            }
            j--;
        }
    }
    k--;
}
console.log(k+1);
