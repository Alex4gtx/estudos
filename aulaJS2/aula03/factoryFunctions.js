//JS aula 34 - factory functions (função de fábrica)

const celular = {
    marcaCelular: 'ASUS',
    tamanhoTela: {
        vertical: 155,
        horizontal: 75
    },
    capacidadeBateria: 5000,
    ligar: function(){
        console.log('fazendo ligação...')
    }
}

// funções de fabrica se assemelham muito com classes em python
function criarCelular(marcaCelular,tamanhoTela,capacidadeBateria){
    return {
        marcaCelular,
        tamanhoTela,
        capacidadeBateria,
        ligar() {
            console.log('fazendo ligação...')
        }
    }
}

const celular1 = criarCelular('zenfone',5.5,5000);
console.log(celular1);
celular1.ligar();