function difference(n) {
    var i = 1;
    var result = 0;
    while (i <= n) {
        var j = 1;
        while (j < i) {
            result += 2*i*j;
            j++;
        }
        i++;
    }
    return result;
}

console.log("For n = " + 10 + ": " + difference(10));
console.log("For n = " + 100 + ": " + difference(100));
