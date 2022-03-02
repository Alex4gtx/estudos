//aula 57 - combinando arrays
const numeros = [1,2,3,4,5];

const combinado = numeros.join('.');
console.log(combinado);

const frase = "ola bem vindo ao curso";
const resultado = frase.split(' ');
console.log(resultado);

console.log(resultado.join('-'));
//slug


//exercicios
//exemplo join
const frase1 = ['olá','meu','nome','é','Alex'];

const jfras = frase1.join('-');
console.log(jfras);

//exemplo split
const jfrasS = jfras.split('-');
console.log(jfrasS);