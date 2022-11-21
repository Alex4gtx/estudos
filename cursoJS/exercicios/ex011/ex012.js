var agora = new Date();
var hora = agora.getHours();

if (hora >= 9 && hora <= 12) {
    console.log('bom dia!');
} else if (hora >= 13 && hora <= 18) {
    console.log('boa tarde!');
} else if (hora >= 19 && hora < 24) {
    console.log('boa noite!');
} else {
    console.log('boa madrugada kkkkkk');
}