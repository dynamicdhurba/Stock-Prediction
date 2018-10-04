# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:13:08 2017

@author: kishor
"""

from PyQt5.QtWidgets import QMessageBox

import datetime
import csv
import numpy as np
from sklearn import linear_model
from sklearn.svm import SVR
#import matplotlib.pyplot as self.axes

import plotter

class Predictor(plotter.ArcaneMplCanvas):
    
    def __init__(self):
        
        plotter.ArcaneMplCanvas.__init__(self)
        self.dates = []
        self.prices = []
        self.sno = []
        
        pass
    
    def parseDate(self,datelist):
        anotherlist = []
        for item in datelist:
            datee = datetime.datetime.strptime(item, "%Y/%m/%d")
            anotherlist.append(datee.day)
    
        return anotherlist

    
    def getData(self, filename):
        datess = []
        with open(filename, 'r') as csvfile:
             csvFileReader = csv.reader(csvfile)
             next(csvFileReader)
             for row in csvFileReader:
                 datess.append(row[2])
                 try:
                     self.prices.append(float(row[6]))#open price
                 except ValueError as e:
                     #print('No integer data in the file.')
                     QMessageBox.information(self, "Error!", "No integer value in csv file.")
                     break
                 self.sno.append(int(row[1]))
        
        self.dates = self.parseDate(datess)
        return
    

    def predictPriceLinearRegression(self, sno, prices, x):
        """Uses Linear Regression model for prediction"""
        linear_mod = linear_model.LinearRegression()
        self.prices = prices
        
        self.sno = np.reshape(self.sno, (len(self.sno), 1))
        self.prices = np.reshape(self.prices, (len(self.prices), 1))
        
        linear_mod.fit(self.sno, self.prices)
        
        predicted_price = linear_mod.predict(x)
        
        return predicted_price[0][0]       
    
    
    def plotLinearRegression(self,sno,prices):
    	 linear_mod = linear_model.LinearRegression()
    	 sno = np.reshape(sno,(len(sno),1)) # converting to matrix of n X 1
    	 
    	 linear_mod.fit(sno,prices) #fitting the data points in the model
    	 self.axes.scatter(sno,prices,color='white') #plotting the initial datapoints 
    	 self.axes.plot(sno,linear_mod.predict(sno),color='blue',linewidth=3) #plotting the line made by linear regression
    	 #self.axes.show()
    	 return  
     
        
    def predictPriceSVR(self,sno, price, valnext):
        """Uses Support Vector Regression model for prediction"""

        #reshape the sno array into the numpy array of nX1
        sno=np.reshape(sno,(len(sno),1))
        
        
        svr_lin=SVR(kernel='linear',C=1e3)
        #svr_poly=SVR(kernel='poly',C=1e3,degree=2)
        svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1)
        
        svr_lin.fit(sno,price)
        #svr_poly.fit(sno,price)
        svr_rbf.fit(sno,price)
        
        
        #PLOT THE DATA ON THE GRAPH
        
        self.axes.scatter(sno,price,color='white',label='data')
        self.axes.plot(sno,svr_lin.predict(sno),color='blue',label='Linear SVR')
        #matself.axes.plot(sno,svr_poly.predict(sno),color='red',label='Polynomial SVR')
        self.axes.plot(sno,svr_rbf.predict(sno),color='red',label='RBF SVR')
        #self.axes.xlabel('snos')
        #self.axes.ylabel('Price')
        #self.axes.title('Support Vector Regression')
        #self.axes.legend()
        #self.axes.show()
        
        #print(svr_lin.predict(101)[0])
        #print(svr_poly.predict(10)[0])
        #print(svr_rbf.predict(101)[0])
        return svr_lin.predict(valnext)[0], svr_rbf.predict(valnext)[0]
     
''' 
def main():
    
    mypredictor = Predictor()
    mypredictor.getData('data/company_data/ADBL.csv')
    
    print (mypredictor.dates)
    print (mypredictor.prices)
    print ("\n")
    
    predicted_price, coefficient, constant = mypredictor.predictPriceLinearRegression(mypredictor.sno,mypredictor.prices,100)


    print ("The stock open price for the given date is: $",str(predicted_price))
    print ("The regression coefficient is ",str(coefficient),", and the constant is ", str(constant))
    print ("the relationship equation between dates and prices is: price = ",str(coefficient),"* date + ",str(constant))
    
    #mypredictor.show_plot(mypredictor.dates, mypredictor.prices)
    mypredictor.plotLinearRegression(mypredictor.sno, mypredictor.prices)
    #mypredictor.plotSVR(mypredictor.sno, mypredictor.prices)
    mypredictor.predictPriceSVR(mypredictor.sno, mypredictor.prices)  


if __name__ == '__main__':
    main()
'''





    
        
    