//comparações não boleanas

//Falsy
//undefined
//null
// 0 
// false
// ''
// NaN - not a number

//truthy

let corP = 'vermelho';
let corPadrao = 'azul';
let corPerfil = corP || corPadrao;
console.log(corPerfil);
