//aula 58 - esvaziando um array
let numeros = [1,2,3,4,5,6];
let outros = numeros; //referência de numeros

//solução 1
//numeros = []; //usado para limpar array reinstanciando, mas não limpa outras referencias

//solução 2 meio mais limpo de fazer isso
numeros.length = 0;
console.log(numeros);
console.log(outros);

//solução 3
//numeros.splice(0,numeros.length);
//console.log(numeros);
//console.log(outros);

//solução 4
//while (numeros.length > 0) {
//    numeros.pop();
//}
