##uso de modulo pyserial
import serial as s
###################################

import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "ControlArduino.ui"  # Nombre del archivo

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


        self.btn_control.clicked.connect(self.control)

    def control(self):
        v = self.btn_control.text()
        if v == "PRENDER":
            self.btn_control.setText("APAGAR")
            self.arduino.write("1".encode())
        else:
            self.btn_control.setText("PRENDER")
            self.arduino.write("0".encode())

    def accion(self):
        #PENDIENTE aplicar: realizar lecturas SOLO cuando exista información que leer
		#instrucción necesaria: if o while ... self.arduino.inWaiting():

        while self.arduino.inWaiting():
            valor = self.arduino.readline().decode()

            valor = valor.replace("\n","")
            valor = valor.replace("\r", "")

            self.datosSensor.addItem(valor)

            self.datosSensor.setCurrentRow(self.datosSensor.count()-1)

        ########################################################

    def conexion(self):
        v = self.btn_conexion.text()
        if v == "CONECTAR": #pasa de desconectado a conectado
            self.btn_conexion.setText("DESCONECTAR")

            if self.arduino == None: #SI NO SE HABIA CONECTADO ANTES
                com = "COM" + self.txt_com.text()
                self.arduino = s.Serial(com, baudrate=9600, timeout=1000) ##realiza la conexion
                # y la iniciliza

                self.txt_estado.setText("INICIALIZADO")

                self.SegundoPlano.start(100)

            elif not self.arduino.isOpen():
                self.arduino.open()
                self.txt_estado.setText("REESTABLECIDO")

                self.SegundoPlano.start(100)

        else: #pasa de conectado a desconectado
            self.btn_conexion.setText("CONECTAR")

            self.arduino.close()
            self.txt_estado.setText("CERRADO")

            self.SegundoPlano.stop()

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

    #Tarea X Operaciones con Strings (Cadenas de Caracteres) en Python
    #Tarea X+1 Operaciones con Strings (Cadenas de Caracteres) en Arduino

    #Tarea (Programa) X+2 Modificar la interfaz gráfica de usuario a conveniencia del equipo

    #valor1 + valor 2 + valor 3
