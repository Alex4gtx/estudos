//precisa de atenção
function verificar() {
    let resultado = document.querySelector("div#iresp>p"); //onde será mostrado o resultado
    let inicio = document.getElementById("iinicio");
    let fim = document.getElementById("ifim");
    let passo = document.getElementById("ipasso");
    
    //variaveis transformados em numeros
    let i = Number(inicio.value);
    let f = Number(fim.value);
    let p = Number(passo.value);

    if (i === null || i == '') {
        window.alert('insira um numero de inicio!');
    } else if (f === null || f == '') {
        window.alert('insira um numero de fim!');
    } else if (i >= f) {
        window.alert('o valor do inicio não pode ser maior ou igual ao valor do fim!');
    } else {
        if (p == 0 || p ==  null) {
            window.alert('[AVISO] O passo não pode ser igual a 0, foi considerado automátimacente o passo igual a 1.');
            p = 1;
        }
        resultado.innerText = '';
        for (i; i <= f; i += p) {
            resultado.innerHTML += `${i} &#128073; `;
        }
        resultado.innerHTML += ' &#127988;';
    }
}
