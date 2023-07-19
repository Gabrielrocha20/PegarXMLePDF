import json
import os
import sys
from datetime import datetime
from time import sleep
from zipfile import *

from PyQt5.QtWidgets import QApplication, QMainWindow

from gerarpdf import PegarPDF
from ui import Ui_CompactarNotas


class Interface(QMainWindow, Ui_CompactarNotas):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.thread = {}
        self.btnGerar.clicked.connect(self.gerar)

    def gerar(self):
        self.labelColetar.setText("")
        self.labelCompactar.setText("")
        self.labelFinalizar.setText("")
        self.labelColetar.setText("Coletando dados   e baixando pdf                       ✅")
        compactador = ZipNotas()
        notas = compactador.coletarNotas()
        check = False

        if len(notas) > 0:
            caminho_pdf, nome_pdf = compactador.gerarPdf(notas)
            
            self.labelCompactar.setText("Compactando dados                                    ✅")
            check = compactador.zipar(notas, caminho_pdf, nome_pdf)
            sleep(0.5)
        else:
            self.labelColetar.setText("Dados nao encontrados                                  ⛔")
            self.labelCompactar.setText("Compactando dados Vazios                             ⛔")
        
        return self.finalizar(check)

        

        
    def finalizar(self, check):
        if check:
            sleep(1)
            self.labelFinalizar.setText("Arquivo gerado                                       ✅")
        else:
            self.labelFinalizar.setText("Arquivo não foi gerado                               ⛔")
            


class ZipNotas:
    def __init__(self):
        self.date = datetime.now()
        self.data_dia = self.date.strftime('%d-%m-%Y')

        self.caminho_xml = None
        self.nomearquivo = None
        self.caminho_area_trabalho = None
        self.caminho_download = None

        self.get_config()

        self.pasta_nova = f"{self.caminho_area_trabalho}/{self.nomearquivo}_{self.date.year}_{self.date.month}"

    def get_config(self):
        pasta = fr"{os.getcwd()}\configCaminho.json"
        with open(pasta, encoding='utf-8') as meu_json:
            config = json.load(meu_json)
            self.caminho_xml = f"{config['caminho']}/{self.date.year}0{self.date.month}{config['autorizados']}"
            self.nomearquivo = config['nome']
            self.caminho_area_trabalho = config["caminhoFinal"]
            self.caminho_download = config["caminhoDownload"]
        
        return
    
    def coletarNotas(self):
        notas = []
        for diretorio, subpastas, arquivos in os.walk(self.caminho_xml):
            for arquivo in arquivos:
                segundos = os.path.getmtime(os.path.join(os.path.realpath(diretorio), arquivo))
                data_arquivo = datetime.fromtimestamp(segundos).strftime('%d-%m-%Y')
                if ("-procNFe.xml" in arquivo) and (data_arquivo == self.data_dia):
                    caminho_arquivo = os.path.join(diretorio, arquivo)
                    notas.append((caminho_arquivo, arquivo))
        return notas

    def zipar(self, notas, caminho_pdf, nome_pdf):
        with ZipFile(f"{self.pasta_nova}.rar", "w") as compactar:
            for nota in notas:
                compactar.write(nota[0], nota[1])
                
            compactar.write(caminho_pdf, nome_pdf)

        os.remove(caminho_pdf)
        return True

    
    def gerarPdf(self, notas):
        pdf = PegarPDF()
        pdf.baixarPDF(notas)

        for diretorio, subpastas, arquivos in os.walk(self.caminho_download):
                for arquivo in arquivos:
                    segundos = os.path.getmtime(os.path.join(os.path.realpath(diretorio), arquivo))
                    data_arquivo = datetime.fromtimestamp(segundos).strftime('%d-%m-%Y')

                    if ("FSist" in arquivo) and (data_arquivo == self.data_dia):
                        caminho_arquivo = os.path.join(diretorio, arquivo)
                        caminho_pdf = os.path.join(diretorio, 'NOTAS-PDFs.zip')

                        if not os.path.exists(caminho_pdf):
                            os.rename(caminho_arquivo, caminho_pdf)
                            return caminho_pdf, 'NOTAS-PDFs.zip'
        

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loja = Interface()
    loja.show()
    app.exec()