//usando apis, essa api retorna ddados do usuario do github

const username = 'Alex4gtx'

fetch(`https://api.github.com/users/${username}`, {
    method: 'GET',
    headers: {
        Accept: 'application/vnd.github.v3+json'
    }
}).then((response) => {
    console.log(typeof(response));
    console.log(response);
    return response.json()
}).then((data) => {
    console.log(`o nome do usuário é ${data.name}`);
}).catch(err => {
    console.log('houve algum erro: ' + err);
})