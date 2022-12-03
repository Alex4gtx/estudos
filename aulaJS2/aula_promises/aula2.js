// retorno do catch
//cath retorna um erro personalizado no lugar de um erro padrão

const promessa = new Promise((resolve, reject) => {
    const nome = 'marcos';

    if(nome === 'alex') {
        resolve(`Usuário ${nome} encontrado`);
    } else {
        reject(`Usuário ${nome} não encontrado!`);
    }
})

promessa.then(dado2 => dado2.toLowerCase()).then(dado => console.log(dado)).catch(erro => console.log('aconteceu um erro: ' + erro));

// resolver várias promessas com all
// captura apos todas as promessas se completarem
const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('p1 ok')
    }, 2000)
})

const p2 = new Promise((resolve, reject) => {
    resolve('p2 ok')
})

const p3 = new Promise((resolve, reject) => {
    resolve('p3 ok')
})

const resolveAll = Promise.all([p1, p2, p3]).then(dados => console.log(dados))

// varias promessas com race
// resolve aquela que ganha a corrida, a que é mais rapida
const p4 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('p4 ok')
    }, 2000)
})

const p5 = new Promise((resolve, reject) => {
    resolve('p5 ok')
})

const p6 = new Promise((resolve, reject) => {
    resolve('p6 ok')
})

const resolveRace = Promise.race([p4, p5, p6]).then((dados) => {
    console.log(dados);
})