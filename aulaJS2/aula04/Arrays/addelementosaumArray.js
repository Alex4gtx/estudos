//Adicionando elementos
const numeros = [1,2,3];

//inicio
numeros.unshift(0); //insere um elemento no inicio do array

//meio
numeros.splice(1,0,'a'); //insere um elemento em um certo indice (indice/deletar/elemento)

//final
numeros.push(5); //insere um elemento no final do array

console.log(numeros);