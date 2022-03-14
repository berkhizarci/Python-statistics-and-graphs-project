# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit ,QMainWindow
import matplotlib.pyplot as plt
import statistics
from scipy import stats
import numpy as np
import math
import pandas as pd 

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 403)
        Dialog.setFixedSize(630, 403)
        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(80, 70, 71, 41))
        self.Add.setObjectName("Add")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 40, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 80, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 111, 21))
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.Remove_Selected = QtWidgets.QPushButton(Dialog)
        self.Remove_Selected.setGeometry(QtCore.QRect(20, 150, 71, 41))
        self.Remove_Selected.setObjectName("Remove_Selected")
        self.Plot = QtWidgets.QPushButton(Dialog)
        self.Plot.setGeometry(QtCore.QRect(265, 140, 91, 31))
        self.Plot.setObjectName("Plot")
        self.Histogram = QtWidgets.QPushButton(Dialog)
        self.Histogram.setGeometry(QtCore.QRect(265, 190, 91, 31))
        self.Histogram.setObjectName("Histogram")
        self.Maximum = QtWidgets.QPushButton(Dialog)
        self.Maximum.setGeometry(QtCore.QRect(370, 40, 91, 31))
        self.Maximum.setObjectName("Maximum")
        self.Minimum = QtWidgets.QPushButton(Dialog)
        self.Minimum.setGeometry(QtCore.QRect(370, 90, 91, 31))
        self.Minimum.setObjectName("Minimum")
        self.Standard_Deviation = QtWidgets.QPushButton(Dialog)
        self.Standard_Deviation.setGeometry(QtCore.QRect(370, 140, 91, 31))
        self.Standard_Deviation.setObjectName("Standard_Deviation")
        self.Skewness = QtWidgets.QPushButton(Dialog)
        self.Skewness.setGeometry(QtCore.QRect(370, 190, 91, 31))
        self.Skewness.setObjectName("Skewness")
        self.Kurtosis = QtWidgets.QPushButton(Dialog)
        self.Kurtosis.setGeometry(QtCore.QRect(370, 240, 91, 31))
        self.Kurtosis.setObjectName("Kurtosis")
        self.Mean = QtWidgets.QPushButton(Dialog)
        self.Mean.setGeometry(QtCore.QRect(370, 290, 91, 31))
        self.Mean.setObjectName("Mean")
        self.Median = QtWidgets.QPushButton(Dialog)
        self.Median.setGeometry(QtCore.QRect(370, 340, 91, 31))
        self.Median.setObjectName("Median")
        self.Remove_All = QtWidgets.QPushButton(Dialog)
        self.Remove_All.setGeometry(QtCore.QRect(20, 200, 71, 41))
        self.Remove_All.setObjectName("Remove_All")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(100, 130, 150, 241))
        self.listWidget.setObjectName("listWidget")
        self.maximum_output = QtWidgets.QLineEdit(Dialog)
        self.maximum_output.setGeometry(QtCore.QRect(480, 39, 113, 31))
        self.maximum_output.setReadOnly(True)
        self.maximum_output.setObjectName("maximum_output")
        self.maximum_output.setAlignment(QtCore.Qt.AlignLeft)
        self.minimum_output = QtWidgets.QLineEdit(Dialog)
        self.minimum_output.setGeometry(QtCore.QRect(480, 89, 113, 31))
        self.minimum_output.setReadOnly(True)
        self.minimum_output.setObjectName("minimum_output")
        self.minimum_output.setAlignment(QtCore.Qt.AlignLeft)
        self.standart_deviation_output = QtWidgets.QLineEdit(Dialog)
        self.standart_deviation_output.setGeometry(QtCore.QRect(480, 139, 113, 31))
        self.standart_deviation_output.setReadOnly(True)
        self.standart_deviation_output.setObjectName("standart_deviation_output")
        self.standart_deviation_output.setAlignment(QtCore.Qt.AlignLeft)
        self.skewness_output = QtWidgets.QLineEdit(Dialog)
        self.skewness_output.setGeometry(QtCore.QRect(480, 189, 113, 31))
        self.skewness_output.setReadOnly(True)
        self.skewness_output.setObjectName("skewness_output")
        self.skewness_output.setAlignment(QtCore.Qt.AlignLeft)
        self.kurtosis_output = QtWidgets.QLineEdit(Dialog)
        self.kurtosis_output.setGeometry(QtCore.QRect(480, 239, 113, 31))
        self.kurtosis_output.setReadOnly(True)
        self.kurtosis_output.setObjectName("kurtosis_output")
        self.kurtosis_output.setAlignment(QtCore.Qt.AlignLeft)
        self.mean_output = QtWidgets.QLineEdit(Dialog)
        self.mean_output.setGeometry(QtCore.QRect(480, 289, 113, 31))
        self.mean_output.setReadOnly(True)
        self.mean_output.setObjectName("mean_output")
        self.mean_output.setAlignment(QtCore.Qt.AlignLeft)
        self.median_output = QtWidgets.QLineEdit(Dialog)
        self.median_output.setGeometry(QtCore.QRect(480, 339, 113, 31))
        self.median_output.setReadOnly(True)
        self.median_output.setObjectName("median_output")
        self.median_output.setAlignment(QtCore.Qt.AlignLeft)
        self.file_import = QtWidgets.QPushButton(Dialog)
        self.file_import.setGeometry(QtCore.QRect(230, 70, 75, 41))
        self.file_import.setObjectName("file_import")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        y = []
    
        def Add_is_clicked():
            values = self.lineEdit.text()
            try:
                a=values
                float(a)
                self.listWidget.addItem(values+'\n')
                y.append(values)
            except ValueError:
                pass

        def Remove_Selected_is_clicked():
            i = self.listWidget.currentRow()
            if i >= 0:
                y.pop(i) 
                for item in self.listWidget.selectedItems():
                    self.listWidget.takeItem(self.listWidget.row(item))
            else: 
                pass
  
        def Remove_All_is_clicked():
            self.listWidget.clear()
            y.clear()

        def Plot_is_clicked():
            if len(y) < 1:
                pass
            else:
                y1 = [float(i) for i in y]
                plt.plot(list(range(0, len(y1))), (y1))
                plt.show()
            
        def Histogram_is_clicked():
            if len(y) < 1:
                pass
            else:
                x=np.asfarray(y,float)
                max_value=np.max(x)
                min_value=np.min(x)
                number_of_bins = round(math.sqrt(len(x)))
                bin_width = abs((max_value-min_value)/number_of_bins)
                plt.hist(x, bins=number_of_bins, width = bin_width, color='#0504aa',alpha=0.7)
                plt.axvline(0)
                plt.grid(axis='y', alpha=0.75)
                plt.xticks(fontsize=15)
                plt.yticks(fontsize=15)
                plt.xlabel('Item',fontsize=15)
                plt.ylabel('Frequency',fontsize=15)
                plt.title('Normal Distribution Histogram',fontsize=15)
                plt.show()

        def Standard_Deviation_is_clicked():
            if len(y) < 2:
                pass
            else:
                x=np.asfarray(y,float)
                standard_deviation = format(statistics.stdev(x), ".5f")
                self.standart_deviation_output.setText(str(standard_deviation))
                    
        def Skewness_is_clicked():
            if len(y) < 2:
                pass
            else:
                x=np.asfarray(y,float)
                standard_deviation = (statistics.stdev(x))
                number_of_data = len(x)
                arithmetic_mean = sum(x) / number_of_data
                if number_of_data % 2 == 1:
                    median = (sorted(x)[number_of_data // 2])
                else:
                    i = number_of_data // 2
                    median = ((sorted(x)[i - 1] + sorted(x)[i]) / 2)
                skewness = format((3 * (arithmetic_mean - median) / standard_deviation), ".5f")
                self.skewness_output.setText(str(skewness))

        def Kurtosis_is_clicked():
            if len(y) < 2:
                pass
            else:
                x=np.asfarray(y,float)
                standard_deviation = (statistics.stdev(x))
                m4 = stats.moment(x, moment=4)
                kurtosis = format((m4 / standard_deviation ** 4), ".5f")
                self.kurtosis_output.setText(str(kurtosis))
                
        def Mean_is_clicked():
            x=np.asfarray(y,float)
            mean = format((statistics.mean(x)), ".5f")
            self.mean_output.setText(str(mean))

        def Median_is_clicked():
            x=np.asfarray(y,float)
            median = format((statistics.median(x)), ".5f")
            self.median_output.setText(str(median))

        def Maximum_is_clicked():
            x=np.asfarray(y,float)
            maximum = format((max(x)), ".5f")
            self.maximum_output.setText(str(maximum))

        def Minimum_is_clicked():
            x=np.asfarray(y,float)
            minimum = format((min(x)), ".5f")
            self.minimum_output.setText(str(minimum))
            
        def loadFileContent():
            options = QtWidgets.QFileDialog.Options()
            fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', filter='Text File (*.txt);;Excel File (*.xlsx)',options=options)
            path = fileName[0]
            if path != '':
                if path.lower().endswith('.txt'):
                    array2D = []
                    column = int(get_column_name())
                    sign = str(get_sign_name())
                    with open(path, 'r') as f:
                        for line in f.readlines():
                            array2D.append(line.split())
                    array2D = list(filter(None,array2D))
                    if sign.lower() == "positive":
                        for i in range(len(array2D)):
                            if float(array2D[i][column-1])>=0:
                               self.listWidget.addItem(array2D[i][column-1]+'\n')
                               y.append(array2D[i][column-1])
                            else:
                                continue
                    elif sign.lower() == "negative":
                        for i in range(len(array2D)):
                            if float(array2D[i][column-1])<=0:
                                self.listWidget.addItem(array2D[i][column-1]+'\n')
                                y.append(array2D[i][column-1])
                            else:
                                continue
                    elif sign.lower() == "either":
                        for i in range(len(array2D)):
                            self.listWidget.addItem(array2D[i][column-1]+'\n')
                            y.append(array2D[i][column-1])

                elif path.lower().endswith('.xlsx'):
                    excel_data=pd.read_excel(path,sheet_name=get_sheet_name())
                    column_list = excel_data[get_column_name()].tolist()
                    for i in column_list:
                        if i==i:
                            self.listWidget.addItem(str(i)+'\n')
                            y.append(str(i))
                        else:
                            continue
            else:
                pass      
             
        def get_sheet_name():
            text, okPressed = QInputDialog.getText(None, "Get text","Sheet name:", QLineEdit.Normal, "")
            return text

        def get_column_name():
            text, okPressed = QInputDialog.getText(None, "Get text","Column number or name:", QLineEdit.Normal, "")
            return text

        def get_sign_name():
            text, okPressed = QInputDialog.getText(None, "Get text","positive, negative or either:", QLineEdit.Normal, "")
            return text
           
            
        
        self.Add.clicked.connect(Add_is_clicked)
        self.Remove_Selected.clicked.connect(Remove_Selected_is_clicked)
        self.Remove_All.clicked.connect(Remove_All_is_clicked)
        self.Histogram.clicked.connect(Histogram_is_clicked)
        self.Maximum.clicked.connect(Maximum_is_clicked)
        self.Minimum.clicked.connect(Minimum_is_clicked)
        self.Standard_Deviation.clicked.connect(Standard_Deviation_is_clicked)
        self.Kurtosis.clicked.connect(Kurtosis_is_clicked)
        self.Skewness.clicked.connect(Skewness_is_clicked)
        self.Mean.clicked.connect(Mean_is_clicked)
        self.Median.clicked.connect(Median_is_clicked)
        self.Plot.clicked.connect(Plot_is_clicked)
        self.file_import.clicked.connect(loadFileContent)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Statistical Calculator"))
        self.Add.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "Values :"))
        self.label_2.setText(_translate("Dialog", "Show :"))
        self.label_3.setText(_translate("Dialog", "Entered Values:"))
        self.Remove_Selected.setText(_translate("Dialog", "Remove \n"
                                                          "Selected"))
        self.Plot.setText(_translate("Dialog", "Plot"))
        self.Maximum.setText(_translate("Dialog", "Maximum"))
        self.Minimum.setText(_translate("Dialog", "Minimum"))
        self.Standard_Deviation.setText(_translate("Dialog", "Standard \n"
                                                             "Deviation"))
        self.Histogram.setText(_translate("Dialog", "Histogram"))
        self.Kurtosis.setText(_translate("Dialog", "Kurtosis"))
        self.Skewness.setText(_translate("Dialog", "Skewness"))
        self.Mean.setText(_translate("Dialog", "Mean"))
        self.Median.setText(_translate("Dialog", "Median"))
        self.Remove_All.setText(_translate("Dialog", "Remove All"))
        self.file_import.setText(_translate("Dialog", "Import"))
        self.label_4.setText(_translate("Dialog", "Or"))



def main():
    numerical_calculations=QApplication(sys.argv)
    window=QMainWindow()
    ui=Ui_Dialog()
    ui.setupUi(window)
    window.show()
    sys.exit(numerical_calculations.exec_())

main()

