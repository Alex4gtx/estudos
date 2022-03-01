// faixa de preço (exercicio)
//crie um array de objetos de faixa de preços, para que ela possa ser usada em um site igual ao mercado livre
//faixas, tooltip,minimo,maximo

//primeira opção

let faixas = [
    {tooltip: 'Até R$700',minimo: 0,maximo: 700},
    {tooltip: 'de R$700 a R$1000',minimo: 700,maximo: 1000},
    {tooltip: 'R$1000 ou mais',minimo: 1000,maximo: 99999999}
];

//segunda opção (factory functions)
function criaFaixaPreco(tooltip,min,max) {
    return {
        tooltip,
        min,
        max
    }
}

let faixa2 = [
    criaFaixaPreco('Até R$700',0,700),
    criaFaixaPreco('de R$700 a R$1000',700,1000),
    criaFaixaPreco('R$1000 ou mais',1000,9999999999)
];

console.log(faixas);
console.log(faixa2);