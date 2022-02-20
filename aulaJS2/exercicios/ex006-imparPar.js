//par ou impar
//receber uma quantidade de valor para avaliar
//função exibe se cada valor é par ou impar

function exibirTipo(numero) {
    for (let i = 1; i <= numero; i++){
        if (i % 2 === 0){
            console.log(i + " " + "Par");
        }
        else {
            console.log(i + " " + "Impar");
        }
    };
}

exibirTipo(10);