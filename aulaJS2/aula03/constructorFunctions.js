// constructor functions
//camelCase - umDoisTresQuatro

//Pascal Case - UmDoisTresQuatro
function Celular(marcaCelular,tamanhoDaTela,capacidadeBateria){
    this.marcaCelular = marcaCelular,
    this.tamanhoDaTela = tamanhoDaTela,
    this.capacidadeBateria = capacidadeBateria,
    this.ligar = function() {
        console.log('fazendo ligação...');
    }
}

const celular1 = new Celular('Asus',5.5,5000);
console.log(celular1.marcaCelular)

function PlacaDeVideo(marca,modelo,memoria){
    this.marca = marca;
    this.modelo = modelo;
    this.memoria = memoria;
    this.quantidade = 5;
    this.preco = 1000;

    this.estoquePreco = function(qnt,preco){
        this.quantidade = qnt;
        this.preco = preco;
    };

    this.show = function(){
        let info = `Marca: ${this.marca}\nModelo: ${this.modelo}\nMemória: ${this.memoria}\nQuantidade: ${this.quantidade}\nPreço: ${this.preco}`;
        console.log(info);
    };
}

const placa1 = new PlacaDeVideo('Nvidia','RTX 3080 TI',16);
placa1.estoquePreco(14,7000);
placa1.show();
