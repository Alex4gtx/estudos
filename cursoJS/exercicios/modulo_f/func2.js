function fatorial(n) {
    let fat = 1;
    for (let c = n; c > 1; c--) {
        fat *= c;
    }
    return fat;
}

//recursividade
function fatorialNovo(n) {
    if (n==1) {
        return 1;
    } else {
        return n * fatorialNovo(n - 1);
    }
}

console.log(fatorialNovo(5));

console.log(fatorial(5));
