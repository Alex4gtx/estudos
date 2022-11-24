let carros = {
    marca: 'bmw',
    nome: 'm3',
    tração: 'traseira',
    ligarCarro: function() {
        console.log(`ligando carro... [${carros.marca} ${carros.nome}]`);
    },
    frear(bool=false) {
        if (bool) {
            console.log('freando...');
        } else {
            console.log('freio inativo...');
        }
    }
}

carros.ligarCarro();
carros.frear();
carros.frear(true);

carros.marca = 'ferrari';
console.log(carros);

console.log(carro2);