//medidor de velocidade

//velocidade maxima de até 70km/h
//a cada 5km/h acima do limite vc ganha 1pt na carteira
//math.floor()
//caso pontos maior que 12 -> "carteira suspendida"


function verificarVelocidade(velocidade) {
    if (velocidade <= 70){
        return 'Ok';
    }
    else {
        const pontos = Math.floor((velocidade - 70) / 5);
        let result = pontos <= 12 ? pontos : 'Carteira suspendida';
        return result;
    };
}

let vv = verificarVelocidade(70);

console.log(vv);