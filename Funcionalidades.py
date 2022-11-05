from modulos import *
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