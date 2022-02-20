// laço FOR/LOOP for
// existem 5 tipos de laços no java script
// 1.For
// 2.While  | verifica primeiro e executa depois
// 3.Do..while  | executa primeiro e verifica depois
// 4.For..In
// 5.For..of

// 1.for
//crescente
for(let i = 0;i < 5; i++) {
    console.log('estou aprendendo!',i);
}

//decrescente
for(let i = 5;i > 1; i--) {
    console.log('estou aprendendo!',i);
}


//while loop
let i = 5;

while(i >= 1){
    if(i % 2 !== 0){
        console.log(i);
    }
    i--
}


// do..while
i = 0;
do {
    console.log('digitando',i);
    i++;
} while (i < 10)


//for-in
const pessoa = {
    nome: 'alex',
    idade: 25
};
//key-value
for(let chave in pessoa){
    console.log(chave,pessoa.nome);
};

const cores = ['vermelho','azul','verde'];

// para indice no array cores = mostra a cor no indice
for(let indice in cores){
    console.log(indice,cores[indice]);
};


//for-of
// para cor de cores = mostra a cor
for(let cor of cores){
    console.log(cor);
}
