// aula 45 - objeto postagem de blog (exercicio)
// eu quero que você crie nese exercicio um objeto de postagem de blog que vai conter as seguintes propiedades
//titulo,mensagem,autor,vizualizações, comentários(autor,mensagem)/array , estaAoVivo

let postagem = {
    titulo: '',
    mensagem: '',
    autor: '',
    vizualizações: 0,
    comentários: [
    ],
    estaAoVivo: false,
}

postagem.autor = 'alex';
postagem.titulo = 'armored core';
postagem.mensagem = 'usar a peça da mão esquerda como arma de curto alcance o moonlight';
postagem.vizualizações = 230;
postagem.comentários = [{autor: 'james',mensagem: 'eu uso e é muito forte'},{autor: 'john',mensagem: 'prefiro o elf pelo menor peso!'}];
postagem.estaAoVivo = true;
console.log(postagem);