//encontrando elementos (tipos de referĂȘncia)

const marcas = [
    {id: 1,nome: 'a'},
    {id: 2,nome: 'b'}
];

console.log(marcas.find(function(marca){
    return marca.nome === 'a';
}))