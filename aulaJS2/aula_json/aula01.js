// JSON = javascript object notation
// um formato de representação de dados
// mais simples que XML, que é utilizado para fins parecidos
// utiliza o formato chave e valor {"key": "value"}
// é leve para ser enviado por requisições
// muito utilizado para APIs e também arquivos de configurações

// obs:
    // deve se iniciar entre {}
    // só aceita dados, numeros, strings, arrays, objetos, boolean e dados nulos = null
    //só aceita aspas duplas {"nome": "alex"}

import { teste } from './teste.json';

const objs = [
    {
        nome: 'Alex',
        nomedoMeio: 'Giovani',
        sobrenome: 'hirsch',
        idade: 25,
        estaTrabalhando: false,
        trabalhoQueProcuro: {
            profissão: 'programador',
            empresa: 'qualquer',
            modalidades: ['home office', 'presencial', 'semipresencial'],
            nivel: 'junior'
        },
        hobbies: ['programar', 'andar de bicicleta', 'jogar videogame']
    },
    {
        nome: 'james',
        nomedoMeio: null,
        sobrenome: 'hunter',
        idade: 45,
        estaTrabalhando: true,
        trabalhoQueProcuro: {
            profissão: 'corredor de raly',
            empresa: 'redbull',
            modalidades: ['presencial'],
            nivel: 'corredor'
        },
        hobbies: ['correr', 'consertar veiculos', 'academia']
    }
]

// json
// converter objetos para JSON
const jsondados = JSON.stringify(objs);
console.log(jsondados);

// converter json para objeto
const objdados = JSON.parse(jsondados);
console.log(objdados);

console.log(teste);

