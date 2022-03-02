// aula 56 - iterando um array
const numeros = [1,2,3,4,5];

//foreach
numeros.forEach((numero,indice) => console.log(numero,indice))

//exe
const arr1 = [12,45,'asd',true];
arr1.push({id:1});
arr1.splice(2,0,'alex');

arr1.forEach((value,index) => console.log(index,value))