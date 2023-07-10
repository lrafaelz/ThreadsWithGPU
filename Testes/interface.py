# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

import numpy as np
import multiprocessing as mp
import time
import os
import fnmatch
import matplotlib.pyplot as plt

executado = False
folder_path_file_in = ''
folder_path_file_out = ''
nthreads_io = 0
nthreads_cpu = 0
nthreads_local = mp.cpu_count()
tempos_io = []
tempos_cpu = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(60, 20, 491, 51))
        self.label_title.setStyleSheet("font: 16pt \"Consolas\"; text-align: center; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 204, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_threads_io = QtWidgets.QLabel(self.centralwidget)
        self.label_threads_io.setGeometry(QtCore.QRect(80, 90, 361, 31))
        self.label_threads_io.setStyleSheet("font: 14pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_threads_io.setObjectName("label_threads_io")
        self.label_threads_cpu = QtWidgets.QLabel(self.centralwidget)
        self.label_threads_cpu.setGeometry(QtCore.QRect(80, 140, 361, 31))
        self.label_threads_cpu.setStyleSheet("font: 14pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_threads_cpu.setObjectName("label_threads_cpu")
        self.sbThreadsCPU = QtWidgets.QSpinBox(self.centralwidget)
        self.sbThreadsCPU.setGeometry(QtCore.QRect(380, 140, 61, 31))
        self.sbThreadsCPU.setStyleSheet("font: 14pt \"Consolas\";")
        self.sbThreadsCPU.setMinimum(nthreads_local)
        self.sbThreadsCPU.setMaximum(100)
        self.sbThreadsCPU.setSingleStep(1)
        self.sbThreadsCPU.setObjectName("sbThreadsCPU")
        self.sbThreadsIO = QtWidgets.QSpinBox(self.centralwidget)
        self.sbThreadsIO.setGeometry(QtCore.QRect(380, 90, 61, 31))
        self.sbThreadsIO.setStyleSheet("font: 14pt \"Consolas\";")
        self.sbThreadsIO.setMinimum(nthreads_local)
        self.sbThreadsIO.setMaximum(100)
        self.sbThreadsIO.setSingleStep(1)
        self.sbThreadsIO.setObjectName("sbThreadsIO")
        self.label_results = QtWidgets.QLabel(self.centralwidget)
        self.label_results.setGeometry(QtCore.QRect(60, 390, 491, 31))
        self.label_results.setStyleSheet("font: 16pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_results.setObjectName("label_results")
        self.btnEXE = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it(""))
        self.btnEXE.setGeometry(QtCore.QRect(240, 290, 131, 51))
        self.btnEXE.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(255, 255, 255, 255)); font: 14pt \"Consolas\"; font-weight: bold;")
        self.btnEXE.setObjectName("btnEXE")
        self.label_graph_io = QtWidgets.QLabel(self.centralwidget)
        self.label_graph_io.setGeometry(QtCore.QRect(80, 440, 361, 31))
        self.label_graph_io.setStyleSheet("font: 14pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_graph_io.setObjectName("label_graph_io")
        self.label_graph_cpu = QtWidgets.QLabel(self.centralwidget)
        self.label_graph_cpu.setGeometry(QtCore.QRect(80, 490, 361, 31))
        self.label_graph_cpu.setStyleSheet("font: 14pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_graph_cpu.setObjectName("label_graph_cpu")
        self.btnGraphIO = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_graph_io())
        self.btnGraphIO.setGeometry(QtCore.QRect(450, 440, 101, 31))
        self.btnGraphIO.setStyleSheet("background-color: rgb(255, 166, 77); font: 10pt \"Consolas\"; font-weight: bold;")
        self.btnGraphIO.setObjectName("btnGraphIO")
        self.btnGraphCPU = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_graph_cpu())
        self.btnGraphCPU.setGeometry(QtCore.QRect(450, 490, 101, 31))
        self.btnGraphCPU.setStyleSheet("background-color: rgb(255, 166, 77); font: 10pt \"Consolas\"; font-weight: bold;")
        self.btnGraphCPU.setObjectName("btnGraphCPU")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 360, 501, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_path_file_in = QtWidgets.QLabel(self.centralwidget)
        self.label_path_file_in.setGeometry(QtCore.QRect(80, 190, 361, 31))
        self.label_path_file_in.setStyleSheet("font: 14pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_path_file_in.setWordWrap(True)
        self.label_path_file_in.setObjectName("label_path_file_in")
        self.label_path_file_out = QtWidgets.QLabel(self.centralwidget)
        self.label_path_file_out.setGeometry(QtCore.QRect(80, 240, 361, 31))
        self.label_path_file_out.setStyleSheet("font: 14pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_path_file_out.setWordWrap(True)
        self.label_path_file_out.setObjectName("label_path_file_out")
        self.btnPathFileIn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.path_file_in())
        self.btnPathFileIn.setGeometry(QtCore.QRect(450, 190, 101, 31))
        self.btnPathFileIn.setStyleSheet("background-color: rgb(255, 166, 77); font: 10pt \"Consolas\"; font-weight: bold;")
        self.btnPathFileIn.setObjectName("btnPathFileIn")
        self.btnPathFileOut = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.path_file_out())
        self.btnPathFileOut.setGeometry(QtCore.QRect(450, 240, 101, 31))
        self.btnPathFileOut.setStyleSheet("background-color: rgb(255, 166, 77); font: 10pt \"Consolas\"; font-weight: bold;")
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
        self.btnGraphIO.setToolTip(_translate("MainWindow", "Gráfico de operações de IO"))
        self.btnGraphIO.setText(_translate("MainWindow", "VISUALIZAR"))
        self.btnGraphCPU.setToolTip(_translate("MainWindow", "Gráfico de operações de CPU"))
        self.btnGraphCPU.setText(_translate("MainWindow", "VISUALIZAR"))
        self.label_path_file_in.setText(_translate("MainWindow", " Diretório de arquivos de entrada:"))
        self.label_path_file_out.setText(_translate("MainWindow", " Diretório de arquivos de saída:"))
        self.btnPathFileIn.setToolTip(_translate("MainWindow", "Escolher Diretório IN"))
        self.btnPathFileIn.setText(_translate("MainWindow", "ESCOLHER"))
        self.btnPathFileOut.setToolTip(_translate("MainWindow", "Escolher Diretório OUT"))
        self.btnPathFileOut.setText(_translate("MainWindow", "ESCOLHER"))

    def press_it(self, pressed):
        print('click exe')
        ini_tempo_exe = time.time()
        global executado
        global folder_path_file_in
        global folder_path_file_out
        global nthreads_io
        global nthreads_cpu
        nthreads_io = int(self.sbThreadsIO.text())
        nthreads_cpu = int(self.sbThreadsCPU.text())

        if (folder_path_file_in and folder_path_file_out):
            readMulticore()
            executado = True
        else:
            self.msg_warning_path();
        
        end_tempo_exe = time.time()
        print('Tempo total de execução de software: ',  end_tempo_exe - ini_tempo_exe)
    
    def path_file_in(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")
        global folder_path_file_in
        folder_path_file_in = folder_path
        self.label_path_file_in.setStyleSheet("font: 10pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_path_file_in.setText(folder_path)
    
    def path_file_out(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")
        global folder_path_file_out
        folder_path_file_out = folder_path
        self.label_path_file_out.setStyleSheet("font: 10pt \"Consolas\"; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 204, 255, 100), stop:1 rgba(255, 255, 255, 255));")
        self.label_path_file_out.setText(folder_path)
    
    def msg_warning_path(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Atenção")
        msg.setText("Escolha os diretórios antes de executar!")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()
    
    def msg_warning_exe(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Atenção")
        msg.setText("O programa deve ser executado primeiro!")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()
    
    def show_graph_io(self):
        if (not executado):
            self.msg_warning_exe()
        else:
            # self.label_graph_io.setText("label_threads_io")
            global tempos_io
            qtd_arquivos = qtdArquivos(folder_path_file_in)
            x_plot = range(1, qtd_arquivos+1)
            plt.plot(x_plot, tempos_io, label='Arquivos')
            plt.title('Gráfico de tempo de leitura de cada arquivo')
            plt.xlabel('arquivos')
            plt.ylabel('tempo (s)')
            plt.legend()
            plt.show()
    
    def show_graph_cpu(self):
        if (not executado):
            self.msg_warning_exe()
        else:
            # self.label_graph_cpu.setText("label_threads_cpu")
            global tempos_cpu
            qtd_arquivos = qtdArquivos(folder_path_file_in)
            x_plot = range(1, qtd_arquivos+1)
            plt.plot(x_plot, tempos_cpu, label='Arquivos')
            plt.title('Gráfico de tempo de operações de cada arquivo')
            plt.xlabel('arquivos')
            plt.ylabel('tempo (s)')
            plt.legend()
            plt.show()

def qtdArquivos(folder_path_file_in):
    return len(fnmatch.filter(os.listdir(folder_path_file_in), '*.txt'))

def ler_arquivo_txt(arquivo_txt):
    ini_time = time.time()
    matriz = np.loadtxt(arquivo_txt, dtype=float)
    end_time = time.time()
    tempo_r = end_time - ini_time
    return matriz, tempo_r

def arquivos_txt():
    global folder_path_file_in
    qtd_arquivos = qtdArquivos(folder_path_file_in)
    arquivos_txt = []
    for i in range(1, qtd_arquivos+1):
        arquivos_txt.append(folder_path_file_in + '/' + str(i) + '.txt')
    return arquivos_txt

def arquivos_out_txt():
    global folder_path_file_in
    global folder_path_file_out
    qtd_arquivos = qtdArquivos(folder_path_file_in)
    arquivos_txt = []
    for i in range(1, qtd_arquivos+1):
        arquivos_txt.append(folder_path_file_out + '/' + str(i) + '_out.txt')
    return arquivos_txt

def calculo_matrizes(matrizes):
    ini_time = time.time()
    ordlin = np.sort(matrizes, axis=1)
    ordcol = np.sort(matrizes, axis=0)
    somal = np.sum(matrizes, axis=1)
    somac = np.sum(matrizes, axis=0)
    total = np.sum(matrizes)
    maxl = np.max(matrizes, axis=1)
    maxc = np.max(matrizes, axis=0)
    minl = np.min(matrizes, axis=1)
    minc = np.min(matrizes, axis=0)
    end_time = time.time()
    tempo_c = end_time - ini_time

    somal = np.reshape(somal, (1, 1000))
    somac = np.reshape(somac, (1, 1000))
    total = np.reshape(total, (1, 1))
    maxl = np.reshape(maxl, (1, 1000))
    maxc = np.reshape(maxc, (1, 1000))
    minl = np.reshape(minl, (1, 1000))
    minc = np.reshape(minc, (1, 1000))
    
    return ordlin, ordcol, somal, somac, total, maxl, maxc, minl, minc, tempo_c

def writeMulticore(i, ordlin, ordcol, somal, somac, 
            total, maxl, maxc, minl, minc):
    global folder_path_file_out
    arquivos_out = folder_path_file_out + '/' + str(i) + '_out.txt'

    with open(arquivos_out, 'w') as file:
        np.savetxt(file, ordlin[i], fmt='%1.7e')
        np.savetxt(file, ordcol[i], fmt='%1.7e')
        np.savetxt(file, somal[i], fmt='%1.7e')
        np.savetxt(file, somac[i], fmt='%1.7e')
        np.savetxt(file, total[i], fmt='%1.7e')
        np.savetxt(file, maxl[i], fmt='%1.7e')
        np.savetxt(file, maxc[i], fmt='%1.7e')
        np.savetxt(file, minl[i], fmt='%1.7e')
        np.savetxt(file, minc[i], fmt='%1.7e')

def readMulticore():
    global tempos_io
    global tempos_cpu
    global nthreads_io
    global nthreads_cpu
    global folder_path_file_in
    qtd_arquivos = qtdArquivos(folder_path_file_in)
    matrizes = ordlin = ordcol = somal = somac = total = maxl = maxc = minl = minc = []
    arquivos = arquivos_txt()
    arquivos_out = arquivos_out_txt()

    # begin leitura de arquivos
    ini_tempo = time.time()
    pool_r = mp.Pool(nthreads_io)
    resultados_r = pool_r.map(ler_arquivo_txt, arquivos)
    pool_r.close()
    pool_r.join()
    end_tempo = time.time()
    print('Tempo total de leitura de arquivos: ',  end_tempo - ini_tempo)

    for resultado in resultados_r: # resultado[0] == matrizes, resultado[1] == tempo_leitura
        tempos_io.append(resultado[1])
        matrizes.append(resultado[0])
    
    # begin calculos de matrizes
    ini_tempo = time.time()
    pool_c = mp.Pool(nthreads_cpu)
    resultados_c = pool_c.map(calculo_matrizes, matrizes)
    pool_c.close()
    pool_c.join()
    end_tempo = time.time()
    print('Tempo total de cálculos de matrizes: ',  end_tempo - ini_tempo)

    # 0 ordlin, 1 ordcol, 2 somal, 3 somac, 4 total, 5 maxl, 6 maxc, 7 minl, 8 minc, 9 tempo_c
    for resultado in resultados_c:
        ordlin.append(resultado[0])
        ordcol.append(resultado[1])
        somal.append(resultado[2][0])
        somac.append(resultado[3][0])
        total.append(resultado[4][0][0])
        maxl.append(resultado[5][0])
        maxc.append(resultado[6][0])
        minl.append(resultado[7][0])
        minc.append(resultado[8][0])
        tempos_cpu.append(resultado[9])

    # begin escrita de arquivos
    ini_tempo = time.time()
    pool_w = mp.Pool(nthreads_io)
    jobs = []
    for i in range(qtd_arquivos):
        job = pool_w.apply_async(writeMulticore, (i, 
            ordlin, ordcol, somal, somac, 
            total, maxl, maxc, minl, minc))
        jobs.append(job)

    for job in jobs:
        job.get()
    
    pool_w.close()
    pool_w.join()
    
    end_tempo = time.time()
    print('Tempo total de escrita de arquivos: ',  end_tempo - ini_tempo)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
