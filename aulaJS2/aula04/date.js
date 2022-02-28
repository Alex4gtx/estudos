// Date
const data1 = new Date();
const data2 = new Date('march 06 2019 09:30');
const data3 = new Date(2019,02,06,9,30,23);

data3.setFullYear(2030);
data2.toDateString(); // transforma em string
data2.toTimeString(); // transforma em string com formato de tempo
data2.toISOString(); //formato de data de banco de dados


// exercicio
const diaHJ = new Date();
console.log(diaHJ);
const dia1 = new Date('february 28 2022 20:25');
console.log(dia1);
const dia2 = new Date(2022,01,28,20,28);
console.log(dia2);

console.log(dia1.setFullYear(2030));
console.log(dia2.toDateString());
console.log(dia2.toTimeString());
console.log(dia2.toISOString());