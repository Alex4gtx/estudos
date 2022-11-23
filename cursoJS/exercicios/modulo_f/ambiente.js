
/*
let num = [5, 8, 4]; //array / lista
let num2 = [23, 34, 56]
num[3] = 6; //adiciona um valor a um indice
num.push(7); //adiciona um valor no ultimo indice
num.sort(); //ordena uma lista
let num3 = num.concat(num2); //cria uma nova lista concatenando outras duas
num.push('a'); //adiciona um elemento no final da lista tipo append
num.pop(); // remove o ultimo elemento da lista
num.reverse(); // torna os elementos de uma lista reverso
num.shift(); // remove o primeiro elemento de uma lista
let ul = num.slice(0, 2);

console.log(`lista ul ${ul}`);
console.log(num.indexOf('a')); // retorna o indice do elemento
console.log(num, num.length, num3);

let valores = [23,34,6,76,4,33,7,90];
for (let pos = 0;pos < valores.length; pos++) {
    console.log(`indice ${pos} = valor ${valores[pos]}`);
}
*/

let valores = [23,34,6,76,4,33,7,90];
for (let pos in valores) {
    console.log(`a posição ${pos} = ${valores[pos]}`);
}

let val1 = valores.indexOf(33); //existe retorna o indice 5
let val2 = valores.indexOf(3); // não existe retorna -1
console.log(val1, val2);