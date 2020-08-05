/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

var number = 600851475143,
    prime = 3;

while (number % 2 == 0) {
    number /= 2;
}

while (number != 1) {
    if (number % prime == 0) {
        while (number % prime == 0) {
            number /= prime;
        }
    }
    prime += 2
};
console.log(prime-2)