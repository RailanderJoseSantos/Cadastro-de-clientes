from tkinter import *
janela = Tk()
class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_tela()
        #necessario looping pra manter janela aberta
        janela.mainloop()
    def tela(self):
        """Config da tela"""
        self.janela.title("Cadastro de Clientes")
        self.janela.configure(background='#1e3743')
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=400, height=300)
    def frames_tela(self):
        self.frame1 = Frame(self.janela,bd=4,bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)
        #POSICAO DO FRAME NA TELA: esquerda= mais prox de 0, dir.=longe de 0
        self.frame1.place(relx=0.02,rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.janela,bd=4,bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)
        #altura começa em 50%: 0.5
        self.frame2.place(relx=0.02,rely=0.5, relwidth=0.96, relheight=0.46)
Aplicacao()

