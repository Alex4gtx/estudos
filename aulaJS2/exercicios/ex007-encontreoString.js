//encontre o string
//criar um metodo para ler propiedades de um objeto e exibir somente as propiedades do tipo string que estão nesse objeto

function exibirPropiedades(obj) {
    for (key in obj){
        if (typeof obj[key] !== 'number'){
            console.log(key, obj[key]);
        }
    }
}

const filme = {
    titulo: 'vingadores',
    ano: 2018,
    diretor: 'robin',
    personagem: 'thor'
}

exibirPropiedades(filme);
