# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:47:11 2017

@author: kishor
    
    Description:
        This module contains dock widget related classes.
        Manages prediction tab as well.

"""

import csv

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QMessageBox, QPushButton, QHBoxLayout
import logging

from arcaneUI import Ui_AppMainWindow

from browser import ArcaneBrowser
import plotter
import predictor
import predictDialog

module_logger = logging.getLogger('mainApp.dockContents')


COMPANY_SELECTED = ""

class DockCompany(QListWidget, Ui_AppMainWindow):
    """Dock widget class."""
    
    def __init__(self, mainwinref, parent=None):
        module_logger.info("Inside 'DockCompany' constructor.")

        QListWidget.__init__(self, parent)
        self.mainwinref = mainwinref
        
        self.myflag = 0
        self.company_symbol = []

        #reading the company symbols
        with open('data/symbol.csv', 'r') as f:
            reader = csv.reader(f)
            symbol_list = list(reader)
        
        for items in symbol_list:
            for item in items:
                self.company_symbol.append(str(item))
                self.addItem(str(item))
        
        self.itemClicked.connect(self.clk)
        
        #self.itemSelectionChanged.connect(self.foo)
        
        self.mainwinref.verticalLayout.addWidget(self)
        
        module_logger.info("Done.")
    
    #slot
    def clk(self,item):
        
        for sym in self.company_symbol:
            if item.text() == sym:
                link = "http://localhost/stockDhurbaData/goal.php?id= %s.csv" %sym
                self.tabanas = ArcaneBrowser(self.mainwinref, link, self.mainwinref.verticalLayout_4, 1.25)
                
                global COMPANY_SELECTED
                COMPANY_SELECTED = sym
                print(COMPANY_SELECTED)
                
        
        while True:
            itemx = self.mainwinref.verticalLayout_4.takeAt(0)
            if not itemx:
                break
            self.mainwinref.verticalLayout_4.removeWidget(itemx.widget())

        


    def foo(self):
        print('hello')


          

class DockWelcome(QListWidget, Ui_AppMainWindow):
    """Dock widget class."""
    
    def __init__(self, mainwinref, parent=None):
        module_logger.info("Inside 'DockWelcome' constructor.")

        QListWidget.__init__(self, parent)
        self.mainwinref = mainwinref
        
        self.models_list = ['Linear Regression', 'SVR model']
        for item in self.models_list:
            self.addItem(str(item))
        
        self.itemClicked.connect(self.clkd)
        
        self.mainwinref.verticalLayout_2.addWidget(self)
        
        module_logger.info("Done.")
        


    #slot
    def clkd(self, item): 
        
        global COMPANY_SELECTED
       
        if item.text() == 'Linear Regression':
            
            value = 0
            
            mypre = predictor.Predictor()
            path = 'data/company_data/' + COMPANY_SELECTED + '.csv'
            mypre.getData(path)
            result1 = mypre.predictPriceLinearRegression(mypre.sno, mypre.prices, value)            
            mypre.plotLinearRegression(mypre.sno, mypre.prices)
            
            self.mainwinref.verticalLayout_5.addWidget(mypre)
            
            while True:
                itemx = self.mainwinref.verticalLayout_5.takeAt(0)
                if not itemx:
                    break
                self.mainwinref.verticalLayout_5.removeWidget(itemx.widget())

            
            #QMessageBox.information(self, "Predict", "hello")
            self.dia = predictDialog.PredictDialog(self)
            value = self.dia.showDialog()
            
            result1 = mypre.predictPriceLinearRegression(mypre.sno, mypre.prices, value)            

            QMessageBox.information(self, "Prediction Result" , "Linear regression predicted price: {0}".format(result1))
            
            self.mainwinref.verticalLayout_5.addWidget(mypre)

        if item.text() == 'SVR model':
            
            value = 0
            
            mypre1 = predictor.Predictor()
            path = 'data/company_data/' + COMPANY_SELECTED + '.csv'
            mypre1.getData(path)
            result2, result3 = mypre1.predictPriceSVR(mypre1.sno, mypre1.prices, value)

            self.mainwinref.verticalLayout_5.addWidget(mypre1)
            
            while True:
                itemx = self.mainwinref.verticalLayout_5.takeAt(0)
                if not itemx:
                    break
                self.mainwinref.verticalLayout_5.removeWidget(itemx.widget())

            
            #QMessageBox.information(self, "Predict", "hello")
            self.dia = predictDialog.PredictDialog(self)
            value = self.dia.showDialog()
            
            result2, result3 = mypre1.predictPriceSVR(mypre1.sno, mypre1.prices, value)

            QMessageBox.information(self, "Prediction Result" , "Linear SVR predicted price: {0}\nRBF SVR predicted price: {1}".format(result2, result3))

            self.mainwinref.verticalLayout_5.addWidget(mypre1)
        

        while True:
            itemx = self.mainwinref.verticalLayout_5.takeAt(0)
            if not itemx:
                break
            self.mainwinref.verticalLayout_5.removeWidget(itemx.widget())
        
    
        
    
    
    
        
