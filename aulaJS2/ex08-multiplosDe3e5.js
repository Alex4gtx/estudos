//multiplos de 3 e 5
//criar função somar que retorna a soma de todos os multiplos de 3 e 5

function somar(limite) {
    let div3e5 = 0
    for (i = 0; i <= limite; i++){
        if (i % 3 === 0 || i % 5 === 0) {
            div3e5 += i;
        }
    }
    console.log(div3e5);
}

somar(6);
