//operadores lógicos

//operador lógico e(and) (&&)
// Retorna true se os dois operandos forem true

console.log(true && true);
console.log(true && false);

let maiordeIdade = true;
let possuiCarteiraDeTrabalho = true;
let podeAplicar = maiordeIdade && possuiCarteiraDeTrabalho;

console.log(podeAplicar);


//operador lógico ou(or) (||)
// Retorna true se um dos operandos forem true

console.log(true || true);
console.log(true || false);

let maiordeIdade = true;
let possuiCarteiraDeTrabalho = false;
let podeAplicar = maiordeIdade || possuiCarteiraDeTrabalho;

console.log(podeAplicar);

// operador not (!)
let candidatoRecusado = !podeAplicar;

console.log(candidatoRecusado);
