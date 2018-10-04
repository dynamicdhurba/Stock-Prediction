# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 08:35:49 2017

@author: kishor
"""

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox, QInputDialog

class PredictDialog(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__()
        
        self.initUI()
        
        #self.valnext = valnext
        
        self.initUI()
    
    def initUI(self):
        '''self.btn = QPushButton('Predict', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()'''
        pass
        
        
    def showDialog(self):
        
        mydialog = QInputDialog()
        mydialog.setStyleSheet('background-color: red;')

        num, ok = mydialog.getInt(self, 'Prediction Box', 
            'Enter the prediction point:')
        
        if not ok:
            #QMessageBox.information(self, "Predict" , "Error! Please dont leave the input field empty.")
            return
        return num

        
        