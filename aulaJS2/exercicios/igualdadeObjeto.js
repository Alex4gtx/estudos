// exercicio 43 - igualdade de objetos (exercicio)

function Endereco(rua,cidade,cep) {
    this.rua = rua;
    this.cidade = cidade;
    this.cep = cep;
}

const endereco1 = new Endereco('a','b','c');
const endereco2 = new Endereco('a','b','c');

function saoIguais(endereco1,endereco2) {
    const a1 = endereco1.rua === endereco2.rua ? true : false;
    const a2 = endereco1.cidade === endereco2.cidade ? true : false;
    const a3 = endereco1.cep === endereco2.cep ? true : false;
    const result = a1 === a2 === a3 ? true : false;
    return result;
}

function temEnderecoMemoriaIguais(endereco1,endereco2) {
    if (endereco1 === endereco2) {
        return true;
    }
    return false;
}


console.log(saoIguais(endereco1,endereco2));
console.log(temEnderecoMemoriaIguais(endereco1,endereco2));
console.log(temEnderecoMemoriaIguais(endereco1,endereco1));