import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

#Algoritma
import vcstandard,vcext,playfair

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        loadUi('kripto.ui', self)

    #Vigenere Cipher Standard
        self.vcstandard_read_encode()
        self.vcstandard_read_decode()
        self.encode_vc.clicked.connect(lambda: self.standar_vc.setCurrentWidget(self.encode_page_vc))
        self.encode_vc.clicked.connect(self.vcstandard_read_encode)
        self.enter_encode_vc.clicked.connect(self.vcstandard_encode)
        self.decode_vc.clicked.connect(lambda: self.standar_vc.setCurrentWidget(self.decode_page_vc))
        self.decode_vc.clicked.connect(self.vcstandard_read_decode)
        self.enter_decode_vc.clicked.connect(self.vcstandard_decode)

    #Vigenere Cipher Extended
        self.vcext_read_encode()
        self.vcext_read_decode()
        self.encode_vcx.clicked.connect(lambda: self.standar_vcx.setCurrentWidget(self.encode_page_vcx))
        self.encode_vcx.clicked.connect(self.vcext_read_encode)
        self.enter_encode_vcx.clicked.connect(self.vcext_encode)
        self.decode_vcx.clicked.connect(lambda: self.standar_vcx.setCurrentWidget(self.decode_page_vcx))
        self.decode_vcx.clicked.connect(self.vcext_read_decode)
        self.enter_decode_vcx.clicked.connect(self.vcext_decode)

    #Playfair
        self.pf_read_encode()
        self.pf_read_decode()
        self.encode_pf.clicked.connect(lambda: self.standar_pf.setCurrentWidget(self.encode_page_pf))
        self.encode_pf.clicked.connect(self.pf_read_encode)
        self.enter_encode_pf.clicked.connect(self.pf_encode)
        self.decode_pf.clicked.connect(lambda: self.standar_pf.setCurrentWidget(self.decode_page_pf))
        self.decode_pf.clicked.connect(self.pf_read_decode)
        self.enter_decode_pf.clicked.connect(self.pf_decode)

        self.show()

    def vcstandard_read_encode(self):
        readplain = open('plaintext.txt')
        plaintext = readplain.read()
        self.plain_vc.setPlainText(str(plaintext))
    def vcstandard_encode(self):
        filecipher = open('ciphertext.txt','w')
        file = str(self.plain_vc.toPlainText())
        key = str(self.key_vc.toPlainText())
        cipher = vcstandard.encode_text(file,key)
        self.cipher_vc.setPlainText(str(cipher))
        filecipher.write(cipher)
        filecipher.close()
    def vcstandard_read_decode(self):
        readcipher = open('ciphertext.txt')
        ciphertext = readcipher.read()
        self.cipher_vc_2.setPlainText(str(ciphertext))
    def vcstandard_decode(self):
        fileplain = open('plaintext.txt','w')
        file = str(self.cipher_vc_2.toPlainText())
        key = str(self.key_vc_2.toPlainText())
        plain = vcstandard.decode_text(file,key)
        self.plain_vc_2.setPlainText(str(plain))
        fileplain.write(plain)
        fileplain.close()
    def vcext_read_encode(self):
        readplain = open('extplain.txt')
        plaintext = readplain.read()
        self.plain_vcx.setPlainText(str(plaintext))
    def vcext_encode(self):
        filecipher = open('extcipher.txt','w')
        file = str(self.plain_vcx.toPlainText())
        key = str(self.key_vcx.toPlainText())
        cipher = vcext.encode_text(file,key)
        self.cipher_vcx.setPlainText(str(cipher))
        filecipher.write(repr(cipher))
        filecipher.close()
    def vcext_read_decode(self):
        readcipher = open('extcipher.txt')
        ciphertext = readcipher.read()
        self.cipher_vcx_2.setPlainText(str(ciphertext))
    def vcext_decode(self):
        fileplain = open('extplain.txt','w')
        file = str(self.cipher_vcx_2.toPlainText())
        key = str(self.key_vcx_2.toPlainText())
        plain = vcext.decode_text(file,key)
        self.plain_vcx_2.setPlainText(str(plain))
        fileplain.write(plain)
        fileplain.close()
    def pf_read_encode(self):
        readplain = open('plaintext.txt')
        plaintext = readplain.read()
        self.plain_pf.setPlainText(str(plaintext))
    def pf_encode(self):
        filecipher = open('ciphertext.txt','w')
        file = str(self.plain_pf.toPlainText())
        key = str(self.key_pf.toPlainText())
        key = playfair.create_key(key)
        cipher = playfair.encode_text(file,key)
        self.cipher_pf.setPlainText(str(cipher))
        filecipher.write(cipher)
        filecipher.close()
    def pf_read_decode(self):
        readcipher = open('ciphertext.txt')
        ciphertext = readcipher.read()
        self.cipher_pf_2.setPlainText(str(ciphertext))
    def pf_decode(self):
        fileplain = open('plaintext.txt','w')
        file = str(self.cipher_pf_2.toPlainText())
        key = str(self.key_pf_2.toPlainText())
        key = playfair.create_key(key)
        plain = playfair.decode_text(file,key)
        self.plain_pf_2.setPlainText(str(plain))
        fileplain.write(plain)
        fileplain.close()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()