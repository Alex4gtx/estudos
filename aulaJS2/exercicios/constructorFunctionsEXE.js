//JavaScript aula 46 - constructor functions (exercicio)

//criar objeto postagem
//titulo,mensagem,autor,vizualizações,comentarios(autor,mensagem)array, estáaovivo

function Postagem(titulo,mensagem,autor,visualizacoes,comentarios,estaAoVivo) {
    this.titulo = titulo;
    this.mensagem = mensagem;
    this.autor = autor;
    this.visualizacoes = visualizacoes;
    this.comentarios = comentarios;
    this.estaAoVivo = estaAoVivo;
};

let coments = [{autor: 'james',mensagem: 'olá eu sou o james'},{autor: 'john',mensagem: 'tenho 3 armamentos nivel 2'}];

const postagem1 = new Postagem('battlefield 4','me conte suas armas e seus niveis','Alex',345,coments,true);

console.log(postagem1);