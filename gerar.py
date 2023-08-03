import json
import os
import sys
from datetime import datetime
from time import sleep
from zipfile import *

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from EnviarEmail import Enviar
from gerarpdf import PegarPDF
from MSGBOX import Ui_Dialog
from ui import Ui_CompactarNotas


class MsgBox(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
    
    def setError(self, text):
        self.labelMSG.setText(f"{text}")


class Interface(QMainWindow, Ui_CompactarNotas):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.date = datetime.now()
        self.data_dia = self.date.strftime('%d-%m-%Y')
        self.thread = {}
        self.btnGerar.clicked.connect(self.gerar)

        self.msgBox = MsgBox()

    def gerar(self):
        self.btnGerar.setEnabled(False)
        try:
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
            caminho_arquivo = compactador.pasta_nova + ".zip"
            return self.finalizar(check, caminho_arquivo)
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function Gerar\n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")


    def finalizar(self, check, caminho_arquivo):
        try:
            if check:
                pasta = fr"{os.getcwd()}\configCaminho.json"
                with open(pasta, encoding='utf-8') as meu_json:
                    config = json.load(meu_json)
                    email = config["Email"]
                    nome_arquivo = config["nome"]
                    assunto = config["assunto"]
                enviar = Enviar()
                check_envio = enviar.enviar_email(email, assunto,caminho_arquivo, nome_arquivo)
                if check_envio:
                    self.labelFinalizar.setText("Arquivo gerado  e enviado para o email               ✅")
                else:
                    self.labelFinalizar.setText("Arquivo gerado  mas não enviado                    ⛔✅")
            else:
                self.labelFinalizar.setText("Arquivo não foi gerado                                    ⛔")
            self.btnGerar.setEnabled(True)
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function Finalizar\n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")

            


class ZipNotas:
    def __init__(self):
        self.date = datetime.now()
        self.data_dia = self.date.strftime('%d-%m-%Y')

        self.caminho_xml = None
        self.nomearquivo = None
        self.caminho_area_trabalho = None
        self.caminho_download = None

        self.get_config()

        self.pasta_nova = f"{self.caminho_area_trabalho}/{self.nomearquivo}_{self.date.year}_{self.date.month}_{self.date.day}"

        self.msgBox = MsgBox()

    def get_config(self):
        try:
            pasta = fr"{os.getcwd()}\configCaminho.json"
            with open(pasta, encoding='utf-8') as meu_json:
                config = json.load(meu_json)
                self.caminho_xml = f"{config['caminho']}/{self.date.year}0{self.date.month}{config['autorizados']}"
                self.nomearquivo = config['nome']
                self.caminho_area_trabalho = config["caminhoFinal"]
                self.caminho_download = config["caminhoDownload"]
            
            return
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function Get Config \n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")

    
    def coletarNotas(self):
        try:
            notas = []
            for diretorio, subpastas, arquivos in os.walk(self.caminho_xml):
                for arquivo in arquivos:
                    segundos = os.path.getmtime(os.path.join(os.path.realpath(diretorio), arquivo))
                    data_arquivo = datetime.fromtimestamp(segundos).strftime('%d-%m-%Y')
                    if ("-procNFe.xml" in arquivo) and (data_arquivo == self.data_dia):
                        caminho_arquivo = os.path.join(diretorio, arquivo)
                        notas.append((caminho_arquivo, arquivo))
            return notas
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function  Coletar Notas\n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")


    def zipar(self, notas, caminho_pdf, nome_pdf):
        try:
            with ZipFile(f"{self.pasta_nova}.zip", "w") as compactar:
                for nota in notas:
                    compactar.write(nota[0], nota[1])
                    
                compactar.write(caminho_pdf, nome_pdf)

            os.remove(caminho_pdf)
            return True
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function Zipar\n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")


    
    def gerarPdf(self, notas):
        try:
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
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function Gerar PDF\n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")

        

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loja = Interface()
    loja.show()
    app.exec()