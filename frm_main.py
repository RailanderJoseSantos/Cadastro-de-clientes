from tkinter import *
janela = Tk()
class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        #necessario looping pra manter janela aberta
        janela.mainloop()
    def tela(self):
        """Config da tela"""
        self.janela.title("Cadastro de Clientes")
        self.janela.configure(background='#1e3743')
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)
    def frames_tela(self):
        self.frame1 = Frame(self.janela,bd=4,bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)
        #POSICAO DO FRAME NA TELA: esquerda= mais prox de 0, dir.=longe de 0
        self.frame1.place(relx=0.02,rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.janela,bd=4,bg='#dfe3ee',highlightbackground='#759fe6', highlightthickness=3)
        #altura começa em 50%: 0.5
        self.frame2.place(relx=0.02,rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        """Botão limpar dados"""
        self.bt_limpar = Button(self.frame1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão buscar dados"""
        self.bt_buscar = Button(self.frame1, text="Buscar")
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão novo"""
        self.bt_novo = Button(self.frame1, text="Novo")
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão alterar dados"""
        self.bt_alterar = Button(self.frame1, text="Alterar")
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão apagar dados"""
        self.bt_apagar = Button(self.frame1, text="Apagar")
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #criacao da label e entrada do codigo
        self.lb_codigo = Label(self.frame1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #criacao da label e entrada do nome cliente
        self.lb_nome = Label(self.frame1, text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.35)
        
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        #criacao da label e entrada do telefone
        self.lb_telefone = Label(self.frame1, text="Telefone")
        self.lb_telefone.place(relx=0.05, rely=0.6)
        
        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        #criacao da label e entrada da cidade
        self.lb_cidade = Label(self.frame1, text="Cidade")
        self.lb_cidade.place(relx=0.5, rely=0.6)
        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

Aplicacao()

