//média de notas escolares
// obter a média a partir de um array

// 0-59: f
// 60-69: d
// 70-79: c
// 80-89: b
// 90-100: a

function mediaDoAluno(notas) {
    let sum = 0;
    for (let i = 0; i < notas.length; i++) {
        sum += notas[i]; 
    }
    const media = sum / notas.length;
    if (media >= 0 && media <= 59) {
        return 'F';
    }
    else if (media >= 60 && media <= 69) {
        return 'D';
    }
    else if (media >= 70 && media <= 79) {
        return 'C';
    }
    else if (media >= 80 && media <= 89) {
        return 'B';
    }
    else {
        return 'A';
    };
}

const array = [70,70,100];

console.log(mediaDoAluno(array));


// segunda forma mais clean
function mediaDoAluno2(array) {
    const soma = 0;
    for (const valor of array) {
        soma += valor;
    }
    const media = soma / (array.length);

    if (media <= 59) return 'F';
    if (media <= 69) return 'D';
    if (media <= 79) return 'C';
    if (media <= 89) return 'B';
    return 'A';
}