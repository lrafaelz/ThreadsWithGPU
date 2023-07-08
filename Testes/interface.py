# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(60, 20, 491, 51))
        self.label_title.setStyleSheet("font: 16pt \"Consolas\";\n"
"text-align: center;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 204, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_threads_io = QtWidgets.QLabel(self.centralwidget)
        self.label_threads_io.setGeometry(QtCore.QRect(80, 90, 361, 31))
        self.label_threads_io.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_threads_io.setObjectName("label_threads_io")
        self.label_threads_cpu = QtWidgets.QLabel(self.centralwidget)
        self.label_threads_cpu.setGeometry(QtCore.QRect(80, 140, 361, 31))
        self.label_threads_cpu.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_threads_cpu.setObjectName("label_threads_cpu")
        self.sbThreadsCPU = QtWidgets.QSpinBox(self.centralwidget)
        self.sbThreadsCPU.setGeometry(QtCore.QRect(380, 140, 61, 31))
        self.sbThreadsCPU.setStyleSheet("font: 14pt \"Consolas\";")
        self.sbThreadsCPU.setMinimum(1)
        self.sbThreadsCPU.setMaximum(100)
        self.sbThreadsCPU.setSingleStep(1)
        self.sbThreadsCPU.setObjectName("sbThreadsCPU")
        self.sbThreadsIO = QtWidgets.QSpinBox(self.centralwidget)
        self.sbThreadsIO.setGeometry(QtCore.QRect(380, 90, 61, 31))
        self.sbThreadsIO.setStyleSheet("font: 14pt \"Consolas\";")
        self.sbThreadsIO.setMinimum(1)
        self.sbThreadsIO.setMaximum(100)
        self.sbThreadsIO.setSingleStep(1)
        self.sbThreadsIO.setObjectName("sbThreadsIO")
        self.label_results = QtWidgets.QLabel(self.centralwidget)
        self.label_results.setGeometry(QtCore.QRect(60, 390, 491, 31))
        self.label_results.setStyleSheet("font: 16pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_results.setObjectName("label_results")
        self.btnEXE = QtWidgets.QPushButton(self.centralwidget)
        self.btnEXE.setGeometry(QtCore.QRect(240, 290, 131, 51))
        self.btnEXE.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 14pt \"Consolas\";\n"
"font-weight: bold;")
        self.btnEXE.setObjectName("btnEXE")
        self.label_graph_io = QtWidgets.QLabel(self.centralwidget)
        self.label_graph_io.setGeometry(QtCore.QRect(80, 440, 361, 31))
        self.label_graph_io.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_graph_io.setObjectName("label_graph_io")
        self.label_graph_cpu = QtWidgets.QLabel(self.centralwidget)
        self.label_graph_cpu.setGeometry(QtCore.QRect(80, 490, 361, 31))
        self.label_graph_cpu.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_graph_cpu.setObjectName("label_graph_cpu")
        self.btnGraphIO = QtWidgets.QPushButton(self.centralwidget)
        self.btnGraphIO.setGeometry(QtCore.QRect(450, 440, 101, 31))
        self.btnGraphIO.setStyleSheet("background-color: rgb(255, 166, 77);\n"
"font: 10pt \"Consolas\";\n"
"font-weight: bold;")
        self.btnGraphIO.setObjectName("btnGraphIO")
        self.btnGraphCPU = QtWidgets.QPushButton(self.centralwidget)
        self.btnGraphCPU.setGeometry(QtCore.QRect(450, 490, 101, 31))
        self.btnGraphCPU.setStyleSheet("background-color: rgb(255, 166, 77);\n"
"font: 10pt \"Consolas\";\n"
"font-weight: bold;")
        self.btnGraphCPU.setObjectName("btnGraphCPU")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 360, 501, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lvalorDePi = QtWidgets.QLabel(self.centralwidget)
        self.lvalorDePi.setGeometry(QtCore.QRect(80, 540, 401, 31))
        self.lvalorDePi.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 204, 100), stop:1 rgba(255, 255, 255, 255));")
        self.lvalorDePi.setObjectName("lvalorDePi")
        self.lPiCalculado = QtWidgets.QLabel(self.centralwidget)
        self.lPiCalculado.setGeometry(QtCore.QRect(80, 590, 401, 31))
        self.lPiCalculado.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 204, 100), stop:1 rgba(255, 255, 255, 255));")
        self.lPiCalculado.setObjectName("lPiCalculado")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(490, 540, 61, 81))
        self.label_error.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(230, 153, 255, 255));")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.label_path_file_in = QtWidgets.QLabel(self.centralwidget)
        self.label_path_file_in.setGeometry(QtCore.QRect(80, 190, 361, 31))
        self.label_path_file_in.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_path_file_in.setObjectName("label_path_file_in")
        self.label_path_file_out = QtWidgets.QLabel(self.centralwidget)
        self.label_path_file_out.setGeometry(QtCore.QRect(80, 240, 361, 31))
        self.label_path_file_out.setStyleSheet("font: 14pt \"Consolas\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_path_file_out.setObjectName("label_path_file_out")
        self.btnPathFileIn = QtWidgets.QPushButton(self.centralwidget)
        self.btnPathFileIn.setGeometry(QtCore.QRect(450, 190, 101, 31))
        self.btnPathFileIn.setStyleSheet("background-color: rgb(255, 166, 77);\n"
"font: 10pt \"Consolas\";\n"
"font-weight: bold;")
        self.btnPathFileIn.setObjectName("btnPathFileIn")
        self.btnPathFileOut = QtWidgets.QPushButton(self.centralwidget)
        self.btnPathFileOut.setGeometry(QtCore.QRect(450, 240, 101, 31))
        self.btnPathFileOut.setStyleSheet("background-color: rgb(255, 166, 77);\n"
"font: 10pt \"Consolas\";\n"
"font-weight: bold;")
        self.btnPathFileOut.setObjectName("btnPathFileOut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manipulação de Matrizes"))
        self.label_title.setText(_translate("MainWindow", "Manipulação de Matrizes"))
        self.label_threads_io.setText(_translate("MainWindow", " Número de threads de IO:"))
        self.label_threads_cpu.setText(_translate("MainWindow", " Número de threads de CPU:"))
        self.label_results.setText(_translate("MainWindow", " Resultados:"))
        self.btnEXE.setText(_translate("MainWindow", "EXECUTAR"))
        self.label_graph_io.setText(_translate("MainWindow", " Gráfico de operações de IO_BOUND:"))
        self.label_graph_cpu.setText(_translate("MainWindow", " Gráfico de operações de CPU_BOUND:"))
        self.btnGraphIO.setToolTip(_translate("MainWindow", "Gráfico de ganho"))
        self.btnGraphIO.setText(_translate("MainWindow", "VISUALIZAR"))
        self.btnGraphCPU.setToolTip(_translate("MainWindow", "Gráfico de eficiência por core"))
        self.btnGraphCPU.setText(_translate("MainWindow", "VISUALIZAR"))
        self.lvalorDePi.setText(_translate("MainWindow", " Valor de Pi: 3.14159265358979323846"))
        self.lPiCalculado.setText(_translate("MainWindow", " Pi calculado:"))
        self.label_error.setText(_translate("MainWindow", "Erro:\n"
"0%"))
        self.label_path_file_in.setText(_translate("MainWindow", " Diretório de arquivos de entrada:"))
        self.label_path_file_out.setText(_translate("MainWindow", " Diretório de arquivos de saída:"))
        self.btnPathFileIn.setToolTip(_translate("MainWindow", "Gráfico de ganho"))
        self.btnPathFileIn.setText(_translate("MainWindow", "ESCOLHER"))
        self.btnPathFileOut.setToolTip(_translate("MainWindow", "Gráfico de ganho"))
        self.btnPathFileOut.setText(_translate("MainWindow", "ESCOLHER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
