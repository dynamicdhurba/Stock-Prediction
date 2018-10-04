# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:13:17 2017

@author: kishor
"""

LOG_FILENAME = "logs/logfile.log"

import sys
import logging
import time
from multiprocessing import Pool

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QEventLoop
from PyQt5.QtGui import QIcon

import arcaneUI
import dataGrabber
import plotter
import bars
import splashscreen
import browser
import dockContents



class MainApplication(QMainWindow, arcaneUI.Ui_AppMainWindow):
    '''Main class.It should be used to run the whole application.(uses all other modules if required)'''
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.setWindowIcon(QIcon("image/diamondgif.gif"))
        
        self.initUI()  
        
        
        self.initDataGrabber()
        
        
        with open("styles/mystyle.qss", "r") as f:
            self.setStyleSheet(f.read())

    
    def initUI(self):
        '''method which invokes all other UI modules' classes and uses them'''
        self.setupUi(self)
        
        self.showMaximized()
        
        self.initPlotter()
        
        self.initStatusBar()
        
        #self.initMenuBar()
        
        #self.initBrowser()
        
        self.initDockCompany()
        
        self.initDockWelcome()
        
        self.initTabAnalysis()
        
        self.initBrowserFundamentalAnalysis()
    
    def initBrowserFundamentalAnalysis(self):
        browser.ArcaneBrowser(self, "http://localhost/stockDhurbaData/homecopy.php", self.verticalLayout_6, 1,self)

    
    def initStatusBar(self):
        self.mysbar = bars.ArcaneStatusBar(self, self)
    
    def initMenuBar(self):
        bars.ArcaneMenuBar(self, self)
        
    #def initBrowser(self):
        #browser.ArcaneBrowser(self, "http://merolagani.com/LatestMarket.aspx", self.verticalLayout_5, self)

    def initDockCompany(self):
        dockContents.DockCompany(self, self)
    
    def initDockWelcome(self):
        dockContents.DockWelcome(self, self)
    
    def initTabAnalysis(self):
        #tabana = tabAnalysis.TabTechnicalAnalysis(self, "file:///C:/Users/kishor/Desktop/ArcaneProject/Arcane/webPlots/Stock/goal.html")
        #tabana.loadBrowserContent()
        #tabana.loadDataset("data/facebookCsv.csv")
        pass
        
    def initDataGrabber(self):
        with open('data/flags.txt', 'r') as f:
            if int(f.read()) is 1:
                print("Data already grabbed!")
            else:
                dataGrabber.grabAllData()
        pass


    def initPlotter(self):
        
        '''self.main_widgetplotter = self.tab_browser
        
        sc = plotter.ArcanePlotterMplCanvas(self.main_widgetplotter, width=5, height=4, dpi=100)
        
        #sc.plotsine()
        sc.plotsine()
        self.verticalLayout_5.addWidget(sc)
        pass'''
        
        
        

        
    pass  


# Put the initialization code here
def longInitialization(arg):
    time.sleep(arg)
    return 0



def main():
    
    #initializing the GUI
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash = splashscreen.ArcaneSplashScreen('image/diamondgif.gif')
    splash.show()
    splash.showMessage("Arcane")

    #app.processEvents()
    # this event loop is needed for dispatching of Qt events
    initLoop = QEventLoop()
    pool = Pool(processes=1)
    pool.apply_async(longInitialization, [1], callback=lambda exitCode: initLoop.exit(exitCode))
    initLoop.exec_()

    # create logger
    logger = logging.getLogger('mainApp')
    logger.setLevel(logging.DEBUG)
    # create file handler
    fhandler = logging.FileHandler(LOG_FILENAME)
    fhandler.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to fhandler
    fhandler.setFormatter(formatter)
    # add fhandler to logger
    logger.addHandler(fhandler)

    ###############################
    logger.info('Program started.')


    mainObj = MainApplication()
    mainObj.show()


    splash.finish(mainObj)  #Makes the splash screen wait until the widget mainObj is displayed before calling close() on itself.
    
    sys.exit(app.exec_())
    
    pass

if __name__ == '__main__':
    main()

