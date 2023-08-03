import email.message
import os
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5.QtWidgets import QDialog

from MSGBOX import Ui_Dialog


class MsgBox(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
    
    def setError(self, text):
        self.labelMSG.setText(f"{text}")


class Enviar:
    def __init__(self):
        self.date = datetime.now()
        self.data_dia = self.date.strftime('%d-%m-%Y')
        self.msgBox = MsgBox()
    
    def enviar_email(self, novoEmail,assunto,caminho_arquivo, filename):
        try:
            corpo_email = """
                <p>Segue Anexo</p>
            """
            msg = MIMEMultipart()
            msg["Subject"] = assunto
            msg["From"] = "email"
            msg["To"] = novoEmail
            senha = "senha"

            msg.attach(MIMEText(corpo_email, "html"))

            attchment = open(caminho_arquivo, 'rb')

            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attchment.read())
            encoders.encode_base64(att)
            print(filename)
            att.add_header("Content-Disposition", f'attachment; filename= {filename}.zip')
            attchment.close()
            msg.attach(att)
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()

            s.login(msg["From"], senha)
            s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode('utf-8'))
        except Exception as e:
            self.msgBox.setError(e)
            self.msgBox.show()
            pasta = fr"{os.getcwd()}\log.txt"
            with open(pasta, 'w') as log:
                log.write("=" * 60 + "\n")
                log.write("function Enviar Email\n")
                log.write(self.data_dia +"\n")
                log.write("\n")
                log.write(f"{e}\n")




if __name__ == "__main__":
    enviar = Enviar()
    enviar.enviar_email("gabrielrocha12.gs@gmail.com", "C:/Users/User/Desktop/Pegarxml/gerar.py", "Gerar.py")