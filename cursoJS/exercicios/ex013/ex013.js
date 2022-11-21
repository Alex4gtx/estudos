const agora = new Date();
var diaSem = agora.getDay();

//0 = dom, 1 = seg, 2 = ter, 3 = qua, 4 = qui, 5 = sex, 6 = sab

switch (diaSem) {
    case 0:
        console.log('domingo');
        break;
    case 1:
        console.log('segunda');
        break;
    case 2:
        console.log('terça');
        break;
    case 3:
        console.log('quarta');
        break;
    case 4:
        console.log('quinta');
        break;  
    case 5:
        console.log('sexta');
        break;   
    case 6:
        console.log('sábado');
        break;    
    default:
        console.log('[ERRO] dia inválido!');
        break;
}
