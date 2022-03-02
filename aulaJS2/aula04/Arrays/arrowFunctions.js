//javascript aula 56 arrow functions
const marcas = [
    {id: 1, nome: 'a'},
    {id: 2, nome: 'b'}
];

let encontrar = marcas.find((marca) => {
    return marca.nome === 'a';
}); // usado para retornar apenas um valor

let encontrar2 = marcas.find(marca => marca.nome === 'a'); // usado para retornar apenas um valor/ metodo simplificado


console.log(encontrar);