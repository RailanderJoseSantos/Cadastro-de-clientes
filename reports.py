from modulos import *
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