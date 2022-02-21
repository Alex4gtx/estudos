//contador de asteriscos
//criar uma função que exibe a quantidade de * que aquela linha possui.

function exibirAsteriscos(linhas) {
    let padrao = '';
    for (let index = 1; index <= linhas; index++) {
        padrao += '*';
        console.log(padrao);
    }
}

exibirAsteriscos(5);


//outra forma
function exibirAsteriscos2(linhas) {
    for (let index = 1; index <= linhas; index++) {
        let padrao = '';
        for (let i = 0; i < linhas; i++){
            padrao += '*';
        }
    }
}

exibirAsteriscos2(5);