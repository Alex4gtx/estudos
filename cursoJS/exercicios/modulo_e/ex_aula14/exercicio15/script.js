let resultado = document.getElementById("iresp");

let inicio = Number(document.getElementById("iinicio").value);
let fim = Number(document.getElementById("ifim").value);
let passo = Number(document.getElementById("ipasso").value);

function verificar() {
    for (inicio; inicio <= fim; inicio += passo) {
        resultado.innerHTML += `${inicio} => `;
    }
}
