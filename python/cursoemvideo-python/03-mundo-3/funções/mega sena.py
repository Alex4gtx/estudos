with open('megaoutput2.txt', 'r') as f_obj:
    lines = f_obj.readlines()
    d1 = d2 = d3 = d4 = d5 = d6 = n1 = n8 = 0 # variaveis de dezenas

    for c, line in enumerate(lines):
        lst = list(line.strip().split())

        # dezenas a serem adicionadas nas variaveis
        d1 += int(lst[0])
        d2 += int(lst[1])
        d3 += int(lst[2])
        d4 += int(lst[3])
        d5 += int(lst[4])
        d6 += int(lst[5])

    n = c+1 # numero de linhas/apostas
    lst_resul_media = [int(d1/n), int(d2/n), int(d3/n), int(d4/n), int(d5/n), int(d6/n)]

    # print mostra media
    print(f'A media de todos os {n} sorteios é igual a: ', end='')
    for dez in lst_resul_media:
        print(f'{dez} ', end='')
    print()

    numbdict = dict()
    for c in range(1, 61):
        x = 0
        for line in lines:
            lst = list(line.strip().split())
            for i, dez in enumerate(lst):
                if int(lst[i]) == int(c):
                    x += 1
        numbdict[c] = x
        #print(f'O numero {c} apareceu {x} vezes.')
    print(numbdict)

    lst_pop = list()
    for k, v in numbdict.items():
        if k == 8 or k == 17 or k == 26 or k == 35 or k == 43 or k == 52:
            lst_pop.append(v)
    print(lst_pop)
