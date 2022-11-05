from datetime import date
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import  letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from tkinter import  tix
janela = tix.Tk()
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

class Validadores():
    def validate_entry2(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return  0 <= value <=100




#pyinstaller --onefile --noconsole --windowed sistema.py

class GradientFrame(Canvas):
    def __init__(self, parent, color1="#C6CCFF", color2="gray35", **kwargs):
        Canvas.__init__(self,parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._graw_gradient)
    def _graw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1)/limit
        g_ratio = float(g2-g1)/limit
        b_ratio = float(b2-b1)/limit
        for i in range(limit):
            nr = int(r1 +(r_ratio *i))
            ng = int(g1 +(g_ratio *i))
            nb = int(b1 +(b_ratio *i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradiente")


class Relatorios():
    def printCliente(self,nomeCliente):
        webbrowser.open(nomeCliente+".pdf")
    def geraRelatCliente(self):
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.layoutRelatorio = canvas.Canvas(self.nomeRel+".pdf")
        self.layoutRelatorio.setFont("Helvetica-Bold", 20)
        self.layoutRelatorio.drawString(200, 790, " Relatório Cliente ")

        self.layoutRelatorio.setFont("Helvetica-Bold",14)
        self.layoutRelatorio.drawString(50, 700, 'Código: ')
        self.layoutRelatorio.drawString(50, 670, 'Nome: ')
        self.layoutRelatorio.drawString(50, 640, 'Cidade: ')
        self.layoutRelatorio.drawString(50, 610, 'Telefone: ')
        #SEPARANDO PARA A INFORMAÇÃO NÃO SAIR NEGRITO (SE COLOCASSE CONTATENADO ACIMA)
        self.layoutRelatorio.setFont("Helvetica",14)
        self.layoutRelatorio.drawString(110, 700, self.codigoRel)
        self.layoutRelatorio.drawString(110, 670, self.nomeRel)
        self.layoutRelatorio.drawString(110, 640, self.cidadeRel)
        self.layoutRelatorio.drawString(120, 610, self.telefoneRel)
        #cria moldura de retanngulo: começa em X a esquerda vai ate X1, e compromento Y a Y1, Z espessura
        # self.layoutRelatorio.rect(Espessura, altura1, largura, AuturAiNICIO, fill=False, stroke=True)
       # self.layoutRelatorio.rect(20, 720, 550, 200, fill=0, stroke=1)
        self.layoutRelatorio.showPage()
        self.layoutRelatorio.save()
        nomeCli = self.nomeRel
        self.printCliente(nomeCli)

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
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cidade = self.cidade_entry.get()
        self.telefone = self.telefone_entry.get()
    def add_cliente(self):
        self.variaveis()
        if self.nome_entry.get() == "" or self.cidade_entry.get() == "":
            msg = "Para cadastrar o cliente é necessário inserir o nome e cidade"
            messagebox.showinfo("Cadastro de clientes - Aviso!",msg)
        else:
            self.conecta_db()
            self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
             VALUES(?, ?, ?)""",(self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconecta_db()
            self.select_lista()
            self.limpa_tela()
    def select_lista(self):
        #limpando a lista de exibição
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("",END, values=i)
        self.desconecta_db()
    def OneDoubleClick(self, event):
        self.limpa_tela()
        #RECUPERA O REGISTRO CLICADO 2X E ALIMENTA OS ENTRYS
        self.listaCli.selection()
        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n,'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        escolha = messagebox.askyesno(
            title='Exclusão de registro',
            message='Você realmente deseja realizar a exclusão do registro?',
            detail=''
        )
        if escolha:
            self.variaveis()
            self.conecta_db()
            #deletando registro
            self.cursor.execute("""DELETE FROM clientes WHERE cod= ? """,(self.codigo,))
            self.conn.commit()
            self.desconecta_db()
            self.limpa_tela()
            self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade= ?
        WHERE cod = ? """,(self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpa_tela()

    def busca_cliente(self):

        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children())
        if self.nome_entry.get() !="":
            self.nome_entry.insert(END, '%')
            nome = self.nome_entry.get()
            self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" %nome
            )
            buscanomeCli = self.cursor.fetchall()
            for i in buscanomeCli:
                self.listaCli.insert("",END, values=i)
            self.limpa_tela()
        elif self.cidade_entry.get() !="":
            self.cidade_entry.insert(END, '%')
            cidade = self.cidade_entry.get()
            self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE cidade LIKE '%s' ORDER BY cidade ASC""" %cidade
            )
            buscacidadeCli = self.cursor.fetchall()
            for i in buscacidadeCli:
                self.listaCli.insert("",END, values=i)
            self.limpa_tela()
        elif self.telefone_entry.get() !="":
            self.telefone_entry.insert(END, '%')
            telefone = self.telefone_entry.get()
            self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            WHERE telefone LIKE '%s' """ %telefone
            )
            buscatelefoneCli = self.cursor.fetchall()
            for i in buscatelefoneCli:
                self.listaCli.insert("",END, values=i)
            self.limpa_tela()
        else:
            self.select_lista()
        self.desconecta_db()

    def calendario(self):
        self.calendario1 = Calendar(self.aba2, fg="gray75",bg="blue", font=("Times","9","bold"), locale='pt_br')
        self.calendario1.place(relx=0.5,rely=0.1)
        self.calDataInicio = Button(self.aba2, text="Inserir Data", command=self.print_cal)
        self.calDataInicio.place(relx=0.85, rely=0.85, height=25, width=100)

    def print_cal(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END,dataIni)
        self.calDataInicio.destroy()

    #se uma classe vai usar outra as outras deve passada por parametro
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
        self.lb_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.aba1,validate="key", validatecommand=self.vcmd2)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #criacao da label e entrada do nome cliente
        self.lb_nome = Label(self.aba1, text="Nome",bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)
        
        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        #criacao da label e entrada do telefone
        self.lb_telefone = Label(self.aba1, text="Telefone",bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)
        
        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        #criacao da label e entrada da cidade
        self.lb_cidade = Label(self.aba1, text="Cidade",bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)
        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

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

