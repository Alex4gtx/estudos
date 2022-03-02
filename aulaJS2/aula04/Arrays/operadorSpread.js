//aula 55 - operador spread
const primeiro = [1,2,3];
const segundo = [4,5,6];

//const combinado = primeiro.concat(segundo);
const combinado = [...primeiro,'a',...segundo];
console.log(combinado);

//const cortado = combinado.slice;
const clonado = [...combinado];
console.log(clonado);
//spread

//1,2,3,'%',4,5,6
const clone1 = [...primeiro,'%',...segundo];
console.log(clone1);