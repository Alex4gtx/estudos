let idade = 12;

if (idade < 16) {
    console.log('não vota');
} else if (idade >= 16 && idade < 18) {
    console.log('voto opcional');
} else {
    if (idade >= 18 && idade < 60) {
        console.log('voto obrigatório');
    } else {
        console.log('voto opcional');
    }
}
