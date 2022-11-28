// promises são como promessas da vida real, ele está esperando algum retorno
// para criar uma promessa instanciamos a classe Promise
// que leva dois argumentos, resolve (solução) e reject(erro)
// para encadear mais processos utilizamos o método then;
// alguns rwcursos de JS (fetch API) e bibliotecas retornam promises

const promessa = new Promise((resolve, reject) => {
    const nome = 'james'

    if(nome === 'alex') {
        resolve(`usuário ${nome} encontrado`)
    } else {
        reject(`usuário ${nome} não encontrado!`)
    }
})

promessa.then((dado) => {console.log(dado);});

// encadeamento de thens
const promessa2 = new Promise((resolve, reject) => {
    const nome = 'Jack';

    if(nome === 'alex') {
        resolve(`Usuário ${nome} Encontrado`);
    } else {
        reject(`Usuário ${nome} não Encontrado!`);
    }
});

promessa2.then((dado) => {return dado.toLowerCase()}).then(stringMod => {console.log(stringMod);});