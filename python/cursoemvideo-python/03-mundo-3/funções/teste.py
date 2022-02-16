with open("output.txt", 'a', buffering=100000) as o_obj:
    arquivo = 'Top109Million-probable-v2.txt'
    with open(arquivo, 'r', encoding='ansi', buffering=100000) as fileobj:
        linhas = fileobj.readlines(300)
        c = 3000
        for l in linhas:
            o_obj.writelines(linhas)
            c -= 1
            if c == 0:
                break
