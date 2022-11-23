function parimp(n) {
    if (n%2 == 0) {
        return 'par';
    } else {
        return 'impar';
    }
}

function soma(n1=0, n2=0) {
    return n1+n2;
}

let v = function(x) {
    return x*2;
}
v = v(4)

console.log(v);

console.log(`valor da soma ${soma(2, 3)}, outra soma = ${soma(7)}`)
console.log(parimp(4));
console.log(parimp(5));