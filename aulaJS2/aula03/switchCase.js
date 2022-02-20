//switch, case
//uma das formas de fazer comparações

let permissao = 'gerente'; // comum,gerente,diretor

switch (permissao) {
    case 'comum': //caso
        console.log('usuario comum'); //codigo a ser executado
        break; // quebra, não continua a executar as outras condições

    case 'gerente':
        console.log('usuario gerente');
        break;

    case 'diretor':
        console.log('usuario gerente');
        break;

    default: //caso todos os casos acima não forem verdadeiros
        console.log('usuario não reconhecido');
}
