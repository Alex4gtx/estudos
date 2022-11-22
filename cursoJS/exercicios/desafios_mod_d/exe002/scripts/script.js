window.document.getElementById("verificar").addEventListener("click", verificar);

function verificar() {
    let data = new Date();
    let ano = data.getFullYear();
    let fano = document.getElementById("iano");
    let res = document.getElementById("res");

    if (fano.value.length == 0 || fano.value > ano) {
        window.alert('Verifique os dados e tente novamente');
    } else {
        let fsex = document.getElementsByName("radsex");
        let idade = ano - Number(fano.value);
        var genero = '';
        var img = document.createElement('img');
        img.setAttribute('id', 'foto');
        img.style.width = '250px';
        img.style.height = '250px';
        img.style.borderRadius = '50%';

        if (fsex[0].checked) {
            genero = 'homem';
            if (idade >= 0 && idade < 10) {
                //criança
                img.setAttribute('src', 'imagens/bebe_menino.jpg');
            } else if (idade < 21) {
                //jovem
                img.setAttribute('src', 'imagens/jovem_homem.jpg');
            } else if (idade < 50) {
                //adulto
                img.setAttribute('src', 'imagens/homem_adulto.jpg');
            } else {
                //idoso
                img.setAttribute('src', 'imagens/homem_idoso.jpg');
            }
        } else if (fsex[1].checked) {
            genero = 'mulher';
            if (idade >= 0 && idade < 10) {
                //criança
                img.setAttribute('src', 'imagens/bebe_menina.jpg');
            } else if (idade < 21) {
                //jovem
                img.setAttribute('src', 'imagens/jovem_mulher.jpg');
            } else if (idade < 50) {
                //adulta
                img.setAttribute('src', 'imagens/mulher_adulta.jpg');
            } else {
                //idosa
                img.setAttribute('src', 'imagens/mulher_idosa.jpg');
            }
        }
        res.style.textAlign = 'center';
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`;
        res.appendChild(img);
    }
}