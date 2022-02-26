const celular = {
    marcaCelular: 'Asus',
    tamanhoDaTela: {
        vertical: 155,
        horizontal: 75
    },
    ligar: function() {
        console.log('fazendo ligação...');
    }
}

const novoObjeto = Object.assign({
    bateria: 5000
}, celular); //Object.assign({}, ) faz uma cópia exata de um objeto, e ainda adiciona novos itens no {}
console.log(novoObjeto);

const objeto2 = {...celular}; //faz cópia de objeto usando o spread {...objeto}
console.log(objeto2);


//meus testes

const personagem = {
    vida: 1000,
    def: 200,
    atk: 789,
    atacar: function() {
        console.log('atacando');
    },
    defender: function() {
        console.log('defendendo');
    }
}

const personagem2 = {...personagem};
console.log(personagem2);

const personagem3 = Object.assign({}, personagem);
console.log(personagem3);
