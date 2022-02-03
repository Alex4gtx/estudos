from tkinter import *

def fteste():
    for a in range(0, 10):
        print(a)
        texto2['text'] = a

janela = Tk()
janela.title('testes com tkinter')
texto01 = Label(janela, text='teste teste')
texto01.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="clique aqui", command=fteste)
botao.grid(column=1, row=1)

texto2 = Label(janela, text='')
texto2.grid(column=0, row=3)

janela.mainloop()