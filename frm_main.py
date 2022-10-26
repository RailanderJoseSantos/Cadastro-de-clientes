from tkinter import *
from tkinter import  ttk
import sqlite3

janela = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_db(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor()
    def desconecta_db(self):
        self.conn.close()
    def montaTabelas(self):
        self.conecta_db()
        print('Conectando ao banco de dados')
        ### criar tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
            );
            """)
        self.conn.commit();
        print("Banco de dados criado")
        self.desconecta_db()
class Aplicacao(Funcs):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
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
        self.bt_limpar = Button(self.frame1, text="Limpar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão buscar dados"""
        self.bt_buscar = Button(self.frame1, text="Buscar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão novo"""
        self.bt_novo = Button(self.frame1, text="Novo", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão alterar dados"""
        self.bt_alterar = Button(self.frame1, text="Alterar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão apagar dados"""
        self.bt_apagar = Button(self.frame1, text="Apagar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)



        #criacao da label e entrada do codigo
        self.lb_codigo = Label(self.frame1, text="Código",bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.frame1,bg='lightgray', fg='#000')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #criacao da label e entrada do nome cliente
        self.lb_nome = Label(self.frame1, text="Nome",bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)
        
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        #criacao da label e entrada do telefone
        self.lb_telefone = Label(self.frame1, text="Telefone",bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)
        
        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        #criacao da label e entrada da cidade
        self.lb_cidade = Label(self.frame1, text="Cidade",bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)
        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        """LISTA DE EXIBICAO"""
        style = ttk.Style(janela)
        style.theme_use('clam')
        self.listaCli = ttk.Treeview(self.frame2, height=3, column=("col1","col2","col3","col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        """PERCENTUAL PROPORCIONAL DA TELA"""
        #o frame tem 500px e foi passado um percentual pra cada campo> 50= 10% dos 500.. 200=40% dos 500
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        #BARRAA DE ROLAGEM
        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        #x = encostado a direita
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
Aplicacao()

