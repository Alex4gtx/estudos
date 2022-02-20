//fizzbuzz

// divisivel por 3 => Fizz
// divisivel por 5 => Buzz
// Divisivel por 3 e 5 => FizzBuzz
// não divisivel por 3 ou 5 => entrada
// não é um numero => 'não é um numero' 

function fizzBuzz(numb) {
    if (typeof numb !== 'number') {
        return 'Não é um número'
    }
    else if (numb % 3 === 0 && numb % 5 === 0) {
        return 'FizzBuzz'
    }
    else if (numb % 3 === 0) {
         return 'Fizz';
    }
    else if (numb % 5 === 0) {
         return 'Buzz';
    }
    return numb;
 }

 let inp = 10
 console.log(fizzBuzz(inp));
