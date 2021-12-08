import sys

import serial as s

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P4_LecturaEscrituraSerial.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None

        self.btn_conexion.clicked.connect(self.conexion)

        self.SegundoPlano = QtCore.QTimer()

        self.SegundoPlano.timeout.connect(self.accion)

    def accion(self):
        valor = self.arduino.readline().decode()
        valor = valor.replace("\n","")
        valor = valor.replace("\r", "")
        #print(valor)
        self.datosSensor.addItem(valor)
        self.datosSensor.setCurrentRow(self.datosSensor.count()-1)

        #proceso de control
        valor = int(valor)
        #[0 1023] -> [0 255]
        valor = valor/4
        valor = str(valor)
        self.arduino.write(valor.encode())
        self.txt_respuesta.setText(valor)

    def conexion(self):
        v= self.btn_conexion.text()
        if v == "CONECTAR": #DESCONECTADO A CONECTADO
            self.btn_conexion.setText("DESCONECTAR")

            if self.arduino == None:

                com = "COM" + self.txt_com.text()

                self.arduino = s.Serial(com,baudrate=9600,timeout=1000)

                self.txt_estado.setText("INICIALIZADA")

                self.SegundoPlano.start(100)

            elif not self.arduino.isOpen():
                self.arduino.open()
                self.txt_estado.setText("REESTABLECIDA")

                self.SegundoPlano.start(100)


        else:#CONECTADO A DESCONECTADO
            self.btn_conexion.setText("CONECTAR")
            self.arduino.close()
            self.txt_estado.setText("CERRADA")

            self.SegundoPlano.start(10)

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())