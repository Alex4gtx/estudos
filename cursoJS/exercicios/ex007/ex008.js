let a = {console: 'é um .log'}
const x = 56
let array = [21, 'rato', 'gta', x]
console.log(array)
const objeto01 = new Date(2022,09,02);
console.log(objeto01)

let obj02 = {
    ano: objeto01.getFullYear(),
    mes: objeto01.getMonth(),
    dia: objeto01.getDate(),
    calc(obj) {
        console.log(obj);
    }
}

obj02.calc(obj02.ano);

const vel = 77;
if (vel > 60) {
    console.log('passou a velocidade permitida!');
} else {
    console.log('você esta andando nomal');
}