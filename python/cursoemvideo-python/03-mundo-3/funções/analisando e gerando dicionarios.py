def notas(*nota, sit=False):
    """
    -> Cria um dicionario com as notas de um aluno e adiciona info referente a elas.
    :param nota: (obrigatório) recebe varios valores (float) de notas do aluno.
    :param sit: (opcional) se o parametro for verdadeiro, mostra a situação do aluno.
    :return: retorna um dicionario com informações de um aluno e mostra na tela.
    """
    lst_notas = list(nota)
    media = sum(lst_notas) / len(lst_notas)
    aluno = {'total': len(lst_notas), 'maior': max(lst_notas), 'menor': min(lst_notas), 'media': media}
    if sit:
        if media < 6:
            aluno['situação'] = 'RUIM'
        elif media < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'BOA'
    return aluno


print(f'vera = {notas(6.7, 8.9, 3.1, 9.0, 10, 6.8, sit=True)}')
