//numeros primos

//primos
//compostos

//ex: 10, 11
exibirNumerosPrimos(15);

function exibirNumerosPrimos(limite) {
    let count = 0
    for (let i = 2; i <= limite; i++) {
        if (limite % i === 0) {
            console.log(i);
            count++;
        }
    }
    let primo = true;
        if (count > 1) {
            primo = false;
        }
        console.log(primo);
}


//outra forma
function exibirNumerosPrimos2(limite) {
    for(let numero = 2; numero <= limite; numero++){
        let ehPrimo = true;

        for(let divisor = 2; divisor < numero; divisor++){
            if(numero % divisor === 0){
                ehPrimo = false;
                break;
            }
        }

        if(ehPrimo) console.log(numero);
    }
}


//quebra de função
function exibirNumerosPrimos3(limite) {
    for(let numero = 2; numero <= limite; numero++){
        if(numeroPrimo(numero)) console.log(numero);
    }
}

function numeroPrimo(numero) {
    for(let divisor = 2; divisor < numero; divisor++){
        if(numero % divisor === 0){
            return false;
        }
    }
    return true;
}
