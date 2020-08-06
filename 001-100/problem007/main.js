
function isPrime (n) {
    if (n % 2 == 0) {
        if (n > 2) {
            return false;
        }
        return true;
    }
    var m = 3;
    while (m * m <= n) {
        if (n % m == 0) {
            return false;
        }
        m += 2;
    }
    return true;
}

function nth_prime(n) {
    if (n == 1) {
        return 2;
    }
    var counter = 2;
    var number = 3;
    while (counter <= n) {
        if (isPrime(number)) {
            counter ++;
        }
        number += 2;
    }
    return number-2;
}

var n = 10001;
console.log(nth_prime(n));
