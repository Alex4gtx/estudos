// encontrando elementos (primitivos)
const numeros = [1,2,3,1,4];

let a = numeros.indexOf(2); //mostra o indice dos elementos
let b = numeros.lastIndexOf(1); //procura a ultima ocorrencia do elemento e retorna seu indice
let c = numeros.includes(2); // retorna verdadeiro se o elemento estiver na lista

console.log(a, b, c);