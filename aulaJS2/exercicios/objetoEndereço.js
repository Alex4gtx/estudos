// Objeto endereço

//criar um objeto endereço que contém:
//Rua
//Cidade
//CEP
//exibirEndereço(endereço)

let endereco = {
    rua: 'Tilápia',
    cidade: 'Porto Alegre',
    cep: 96832000
};

function exibirEndereco(endereco) {
    console.log('Mostrando endereço:')
    for (key in endereco) {
        let info = `${key}: ${endereco[key]}`;
        console.log(info);
    }
}

exibirEndereco(endereco);