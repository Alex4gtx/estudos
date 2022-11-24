let produtos = [
    {id: 1, nome: 'pão', valor: 2.0, categoria: 'alimento'},
    {id: 2, nome: 'queijo', valor: 34.0, categoria: 'alimento'},
    {id: 3, nome: 'amaciante', valor: 4.34, categoria: 'limpeza'},
    {id: 4, nome: 'shampoo', valor: 2.5, categoria: 'beleza'},
    {id: 5, nome: 'bolo', valor: 9.0, categoria: 'alimento', sabor: {sabor1:'chocolate'}}
]

let id = produtos.map(produto => produto.id);
console.log(id);

let produto = produtos.map(produto => produto.sabor == undefined ? 0 : produto.sabor);

console.log(produto);

let num = [2,3,8,9,4,5,6,34,67,8,1,45];

let max = num.map(x => x*2);
console.log(max);

let maximum = num.reduce((numbant, numb) => numb > numbant ? numbant = numb : numbant);

console.log(maximum);

let produto2 = produtos.filter(produto => produto.categoria === 'alimento');

console.log(produto2);