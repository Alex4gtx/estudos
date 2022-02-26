//javascript aula 36 - natureza dinâmica de objetos

const mouse = {
    cor: 'red',
    marca: 'dazz'
}

mouse.velocidade = 5000; //criou um novo atributo key/value

mouse.trocarDPI = function(){
    console.log('mudando de DPI');
} // também pode adicionar metodos dessa forma

console.log(mouse);

delete mouse.velocidade; // comando delete usado para apagar atributos de objetos

console.log(mouse);

delete mouse.trocarDPI; //deletar metodos em objetos

console.log(mouse);
