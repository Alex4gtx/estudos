function criarPlacaDeVideo(marca,modelo,memoria,conector,preco) {
    return {
        marca,
        modelo,
        memoria,
        conector,
        preco,
        quantidade: 10,
        showDetails() {
            console.log(`Marca: ${marca}\nModelo: ${modelo}\nMemória: ${memoria}\nConector: ${conector}\nPreço: ${'R$ ' + preco}`)
        },
        addQuantidade(quant) {
            this.quantidade = quant
        }
    }
}

const placa1 = criarPlacaDeVideo('Nvidia','RTX 3080','16gb','PCI-e',5678.76);
const placa2 = criarPlacaDeVideo('AMD','HD 1800','8gb','PCI',2300.00);

let a1 = placa1.marca
let b1 = placa2.marca
var texto1 = `Comparação entre a placa de video ${a1} e ${b1}`
console.log(texto1);
console.log();
placa1.showDetails();
console.log();
placa2.showDetails();
