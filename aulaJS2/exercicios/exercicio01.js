//exercicios

let familia = {
    alex: ['Alex Giovani Hirsch',24,78,1.83],
    vera: ['Vera Lucia Hirsch',49,90,1.59],
    valtair: ['Valtair Hirsch',53,69,1.80],
    michelle: ['Michelle Hirsch',22,59,1.65],
    camila: ['Camila Giovana Cristo',21,56,1.75]
}

const meuNome = familia.alex[0]
const namorada = familia.camila[0]
const mãe = familia.vera[0]
const pai = familia.valtair[0]
const irmã = familia.michelle[0]

var texto = `Eu ${meuNome} namoro com a ${namorada}, o nome do meu pai é ${pai} e o nome da minha mãe é ${mãe} e eles são casados, minha irmã se chama ${irmã}`

console.log(texto)
