function Pessoa(nome,nomeDoMeio,sobrenome,idade) {
    opcionalA1 = function(cpf,cnh,rg,carro) {
        let confcpf = String(cpf);
        this.cpf = `0${confcpf.slice(0,3)}`;
        this.rg = rg;
        this.cnh = cnh;
        this.carro = carro;
    };
    this.nome = nome;
    this.nomeDoMeio = nomeDoMeio;
    this.sobrenome = sobrenome;
    this.idade = idade;
    this.maioridade = this.idade >= 18 ? true : false;
    this.cpf = 0;
    this.rg = 0;
    this.cnh = 0;
    this.carro = 0;
}

const pessoa1 = new Pessoa('Alex','Giovani','Hirsch',24);
let teste = pessoa1.opcionalA1(778877880,09090909,5454545454,true);
console.log(pessoa1.cpf);
console.log(pessoa1.maioridade);
console.log(pessoa1.rg)