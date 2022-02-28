//tipo primitivo
const mensagem = ' minha primeira mensagem ';

//tipo objeto
const outraMensagem = new String('bom dia');

console.log(outraMensagem.length);
console.log(mensagem.length);
console.log(outraMensagem[2]);
console.log(mensagem[2]);
console.log(mensagem.includes('primeira'));
console.log(mensagem.startsWith('minha'));
console.log(mensagem.endsWith('mensagem'));
console.log(mensagem.indexOf('primeira'));

let nm1 = mensagem.replace('minha','sua');
console.log(nm1);

console.log(mensagem.trim());

console.log(mensagem.split(' '));
