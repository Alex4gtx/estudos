def leiaint(prompt):
    """
    -> lê apenas int sem gerar erro que interrompe o programa
    :param prompt: recebe string de apresentação de entrada
    :return: retorna um numero inteiro
    """
    while True:
        entrada = input(prompt)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("\033[1:31mErro! Digite um número inteiro válido.\033[m")


# programa principal
print(f"Você acabou de digitar o número {leiaint('Digite um número: ')}")
