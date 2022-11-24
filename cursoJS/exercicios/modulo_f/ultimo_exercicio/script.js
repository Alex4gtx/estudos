let number = document.getElementById("impnum"); //captura os numeros
let tela = document.getElementById("bloco2"); //tela que mostra dados
let resultado = document.getElementById("bloco3");

let arrayNumb = []; //armazena os numeros

function addNumb() {
    let n = Number(number.value); //numero capturado

    // condições para gravar na arrayNumb
    if (number.value == '') {
        window.alert('[ERRO] campo vazio, adicione um número!');
    } else if (n < 1 || n > 100) {
        window.alert('[ERRO] adicione números entre 1 e 100!');
    } else {
        if (arrayNumb.length == 0) {
            arrayNumb.push(n);
        } else if (arrayNumb.indexOf(n) !== -1) {
            window.alert('[ERRO] o número ja existe!');
        } else {
            arrayNumb.push(n);
        }
    }

    mostrarDados('bloco2');
}

function mostrarDados(strId) {
    // atualiza a tela lateral
    if (strId === 'bloco2') {
        tela.innerHTML = '';
        for (let key in arrayNumb) {
            let addDadosnaTela = document.createElement('p');
            addDadosnaTela.innerText = `Número ${arrayNumb[key]} adicionado.`;
            tela.appendChild(addDadosnaTela);
        }
    }

    if (strId === 'bloco3') {
        resultado.style.display = 'block';
        resultado.innerHTML = '';
    }
}

function finalizar() {
    if (arrayNumb.length == 0) {
        window.alert('Por favor adicionar algum numero na lista!');
    
    } else {
        mostrarDados('bloco3');
        let min = Number(Math.min(...arrayNumb));
        let max = arrayNumb.reduce(function(prev, current) {
            return prev > current ? prev : current
        });
        let media = mediaAritm(arrayNumb);
        let quantItens = arrayNumb.length;
        let soma = function() {
            let count = 0;
            for (let numb in arrayNumb) {
                count += arrayNumb[numb];
            }
            return count;
        }
        
        let itens = document.createElement('p');
        itens.innerText = `A media aritmética é ${media}`;
        resultado.appendChild(itens);
        resultado.innerHTML += `<p>Existem ${quantItens} itens na lista.</p>`;
        resultado.innerHTML += `<p>O menor número da lista é ${min}</p>`
        resultado.innerHTML += `<p>O maior número da lista é ${max}</p>`
        resultado.innerHTML += `<p>A soma de todos os itens da lista é ${soma()}</p>`;
    }
}


function mediaAritm(array) {
    //media
    let soma = 0;
    for (let numb in array) {
        soma += array[numb];
    }
    return soma/array.length;
}