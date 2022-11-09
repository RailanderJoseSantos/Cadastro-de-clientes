from modulos import *
from validEntry import Validadores
from frameGrad import GradientFrame
from reports import Relatorios
from Funcionalidades import  Funcs
#pyinstaller --onefile --noconsole --windowed sistema.py

class Aplicacao(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.janela = janela
        self.validaEntradas()
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
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
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = GradientFrame(self.abas,"silver","white")
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#dfe3ee")
        self.aba2.configure(background="lightgray")
        self.abas.add(self.aba1, text="Clientes")
        self.abas.add(self.aba2, text="Aba 2")

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        self.moldura_bt = Canvas(self.aba1, bd=0, bg='#1e3743',highlightbackground='gray',
                                 highlightthickness=5)
        self.moldura_bt.place(relx=0.19, rely=0.08, relwidth=0.22,  relheight=0.19)
        """Botão limpar dados"""
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=2, bg='#107db2',
                                activebackground='#108ecb', activeforeground='white',
                                fg='white', font=('verdana','8', 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão buscar dados"""
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'), command=self.busca_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg="Digite nome ou cidade do cliente que deseja pesquisar")
        """Botão novo"""
        self.bt_novo = Button(self.aba1, text="Salvar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão alterar dados"""
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        """Botão apagar dados"""
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=2, bg='#107db2',
                                fg='white', font=('verdana','8', 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)



        #criacao da label e entrada do codigo
        self.lb_codigo = Label(self.aba1, text="Código",bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.04)
        self.codigo_entry = Entry(self.aba1,validate="key", validatecommand=self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #criacao da label e entrada do nome cliente
        self.lb_nome = Label(self.aba1, text="Nome",bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.28)
        
        self.nome_entry = EntryPlaceHold(self.aba1,'Digite o nome do cliente')
        self.nome_entry.place(relx=0.05, rely=0.38, relwidth=0.4)

        #criacao da label e entrada do telefone
        self.lb_telefone = Label(self.aba1, text="Telefone",bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.52)
        
        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.62, relwidth=0.4)

        self.lb_endereco = Label(self.aba1, text="Endereço",bg='#dfe3ee', fg='#107db2')
        self.lb_endereco.place(relx=0.05,rely=0.76)
        self.endereco_entry = Entry(self.aba1)
        self.endereco_entry.place(relx=0.05,rely=0.86)

        self.btcep = Button(self.aba1, text="Buscar Cep",bd=2, bg='#107db2',fg='white',font=('verdana','7','bold'))
        self.btcep.place(relx=0.6, rely=0.37, relwidth=0.09, relheight=0.12)
        self.cep_entry = Entry(self.aba1)
        self.cep_entry.place(relx=0.70, rely=0.38, relwidth=0.155)

        self.lb_cidade = Label(self.aba1, text="Cidade",bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.6,rely=0.52)
        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.6,rely=0.62,relwidth=0.25)

        self.lb_bairro = Label(self.aba1, text="Bairro", bg='#dfe3ee', fg='#107db2')
        self.lb_bairro.place(relx=0.6, rely=0.76)
        self.bairro_entry = Entry(self.aba1)
        self.bairro_entry.place(relx=0.6, rely=0.86,relwidth=0.25)

        ### drop down button
        self.TipVar = StringVar()
        self.TipV = ("Solteiro(a)","Casado(a)","Divorciado(a)","Viúvo(a)")
        self.TipVar.set("Solteiro(a)")
        self.popupMenu = OptionMenu(self.aba2, self.TipVar, *self.TipV)
        self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)
        self.estado_civil = self.TipVar.get()

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

        #ao clicar 2x no registro chamar função:
        self.listaCli.bind("<Double-1>", self.OneDoubleClick)

        ##calendario
        self.bt_calendario = Button(self.aba2, text="Data", command=self.calendario)
        self.bt_calendario.place(relx=0.5, rely=0.02)
        self.entry_data = Entry(self.aba2, width=10)
        self.entry_data.place(relx=0.5, rely=0.2)

    def Menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu2 = Menu(menubar,tearoff=0)

        def Quit(): self.janela.destroy()
        menubar.add_cascade(label="Opções", menu = filemenu)
        menubar.add_cascade(label="Relatórios", menu=filemenu2)

        filemenu.add_cascade(label="Janela 2", command=self.janela2)
        #lambda me permite passar parametro dentro do command
        filemenu2.add_cascade(label="Rel. Cadastro", command=self.geraRelatCliente)
        filemenu2.add_cascade(label="Suporte", command=lambda: webbrowser.open('https://wa.me/+5531991335387'))
        filemenu2.add_separator()
        filemenu.add_command(label="Sair", command=Quit)

    def janela2(self):
        self.janela2 = Toplevel()
        self.janela2.title("Janela 2")
        self.janela2.configure(background='lightblue')
        self.janela2.geometry("400x200")
        self.janela2.resizable(False, False)
        #de onde vem
        self.janela2.transient(self.janela)
        self.janela2.focus_force()
        #impede digitar em outra janela
        self.janela2.grab_set()

    def validaEntradas(self):
        self.vcmd2 = (self.janela.register(self.validate_entry2), "%P")

Aplicacao()

