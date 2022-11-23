let number = document.getElementById("impnum"); //captura os numeros
let tela = document.getElementById("bloco2"); //tela que mostra dados

let arrayNumb = []; //armazena os numeros

function addNumb() {
    let n = Number(number.value);
    let igual = arrayNumb.findIndex(n);

    if (number.value == '') {
        window.alert('[ERRO] campo vazio, adicione um número!');
    } else if (n < 1 || n > 100) {
        window.alert('[ERRO] adicione números entre 1 e 100!');
    } else if () {
        window.alert('[ERRO] o número ja existe!');
    } else {
        arrayNumb.push(n)
    }
    tela.innerHTML = '';
    for (let key in arrayNumb) {
        let addDadosnaTela = document.createElement('p');
        addDadosnaTela.innerText = `Número ${arrayNumb[key]} adicionado.`;
        tela.appendChild(addDadosnaTela);
    }
    

}