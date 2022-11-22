//precisa de atenção
function verificar() {
    let resultado = document.getElementById("iresp");
    let inicio = document.getElementById("iinicio");
    let fim = document.getElementById("ifim");
    let passo = document.getElementById("ipasso");
    let i = 1;
    let f = fim.value;
    let p = passo.value;

    resultado.innerText = '';
    for (i; i <= f; i += p) {
        resultado.innerText += `${i} => `;
    }
    resultado.innerText += 'bandeirinha :3';
}
