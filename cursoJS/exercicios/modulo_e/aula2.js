//estrutura de repetição com variavel de controle
// inicialização / teste lógico / incremento

// for
for (let i = 1;i <= 6;i++) {
    console.log(`o i é igual a ${i}`);
}

// for each = para cada elemento
let array = ['alex', 234, 'mila'];
array.forEach(element => {
    console.log(element);
});

let obj1 = {nome: 'alex', sobrenome: 'hirsch', idade: 25, tamanho: 1.83}
let arr = [1,2,3,4,5,6,'jjj']

for (const key in obj1) {
    console.log(key);
}

for (const key of arr) {
    console.log(key);
}