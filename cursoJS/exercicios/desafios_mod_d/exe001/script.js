window.document.getElementsByTagName("body").addEventListener("onload", carregar());

function carregar() {
    let msg = window.document.getElementById("msg");
    let img = window.document.getElementById("imagem");
    let data = new Date();
    let hora = data.getHours();
    let minutos = data.getMinutes();

    msg.innerHTML = `Agora são ${hora} horas e ${minutos} minutos.`;

    if (hora >= 0 && hora < 12) {
        //bom dia
        img.src = 'imagens/manha.jpg';
        document.body.style.background = "#e2cd9f";
    } else if (hora >= 12 && hora <= 18) {
        // boa tarde
        img.src = 'imagens/tarde.jpg';
        document.body.style.background = "#b9846f";
    } else {
        //boa noite
        img.src = 'imagens/noite.jpg';
        document.body.style.background = "#515154";
    }
}
