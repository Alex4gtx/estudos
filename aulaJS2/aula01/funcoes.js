//funções
let corSite = "azul";
function resetaCor(cor, tonalidade){
    corSite = cor + ' ' + tonalidade;
};

console.log(corSite)
resetaCor()
console.log(corSite)
resetaCor('vermelho')
console.log(corSite)
resetaCor('vermelho', 'claro')
console.log(corSite)


// mais sobre funções
let lstNumb = [12,34.5,'zero',true,false];

// funções 
// função que não retorna nada
function verLista(lista) {
    texto = `Mostrando lista: ${lista}`;
    console.log(texto)
};

verLista(lstNumb);

// função que retorna algo
function multiplicarPor2(valor) {
    return valor * 2
};

let result = multiplicarPor2(4);

console.log(result);
