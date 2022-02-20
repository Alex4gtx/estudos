//escreva uma função que usa 2 numeros e retorna o maior entre eles

function retornaMaior(a,b){
    if(a > b)
        return a;
    return b;
}

let a = 8;
let b = 87;

let result = retornaMaior(a,b);

console.log(`o maior valor entre ${a} e ${b} é: ${result}`);

//ou

function max(a,b){
    return a > b ? a: b;
}
