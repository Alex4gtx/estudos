function gerarTabuada() {
    let resultado = document.getElementById("result");
    let entrada = document.getElementById("valor");

    let input = Number(entrada.value);

    if (entrada.value.length == 0) {
        window.alert('digite um número!');
    } else {
        resultado.innerHTML = '';
        for (let i = 0; i <= 10; i++) {
            let r = i * input;
            let paragrafo = document.createElement('p');
            paragrafo.innerText = `${i} X ${input} = ${r}`;
            resultado.appendChild(paragrafo);
        }
    }
}