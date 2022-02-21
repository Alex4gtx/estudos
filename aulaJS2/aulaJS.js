//numeros primos

//primos
//compostos

//ex: 10, 11
exibirNumerosPrimos(15);

function exibirNumerosPrimos(limite) {
    for (let i = 1; i <= limite; i++) {
        if (limite % i === 0) {
            console.log(i);
        };
    }
}