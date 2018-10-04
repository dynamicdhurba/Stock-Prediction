# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 21:23:13 2017

@author: kishor

    Description:
        Contains implementation of toolbar,statusbar like GUIs.
"""

from PyQt5.QtWidgets import QStatusBar, QMenuBar, QAction, QMessageBox, QPlainTextEdit
from PyQt5 import Qt
import logging



module_logger = logging.getLogger('mainApp.bars')


class ArcaneStatusBar(QStatusBar):
    """Status bar class. Inherits QStatusBar."""
        
    def __init__(self, mainwinref, parent=None): # 'mainwinref' is a MainApplication object 
        module_logger.info("Inside 'ArcaneStatusBar' constructor.")
        
        QStatusBar.__init__(self, parent)
        self.asbar = mainwinref.statusBar()
                
        module_logger.info("Done.")
        
        
    def showMsg(self, msg, duration, critical=0):
        '''shows red messages when critical else in normal color for certain duration.'''
        module_logger.info("Inside 'ArcaneStatusBar.showMsg()'.")
        
        
        if critical is not 0:
            self.asbar.setStyleSheet("QStatusBar{padding-left:10px;color:red;}")
        else:
            self.asbar.setStyleSheet("QStatusBar{padding-left:10px;color:white;}")
            
        self.asbar.showMessage(msg, duration)
        
        module_logger.info("Done.")


class ArcaneMenuBar(QMenuBar):
    
    def __init__(self, mainwinref, parent=None):
        module_logger.info("Inside 'ArcaneMenuBar' constructor.")
        
        QMenuBar.__init__(self, parent)
        self.mainwinref = mainwinref
        self.amenubar = self.mainwinref.menuBar()
        
        quitaction = QAction("&Quit", self)
        
        aboutaction = QAction("&About", self)
        aboutaction.triggered.connect(self.aboutArcane)
        
        docsaction = QAction("&Docs", self)
        
        viewaction = QAction("&Logs", self)
        #viewaction.triggered.connect(self.showLogs)

        #mainMenu = self.menuBar()
        filemenu = self.amenubar.addMenu('&File')
        helpmenu = self.amenubar.addMenu('&Help')
        viewmenu = self.amenubar.addMenu('&View')
        filemenu.addAction(quitaction)
        helpmenu.addAction(aboutaction)
        helpmenu.addAction(docsaction)
        viewmenu.addAction(viewaction)
        
        module_logger.info("Done.")
    
    #slot
    def showLogs(self):
        pass
        
        
    
    #slot
    def aboutArcane(self):
        title = "About Arcane"
        content = """Arcane is a software as you have already guessed.Computer software, or 
        simply software, is a part of a computer system that consists of
        data or computer instructions, in contrast to the physical hardware
        from which the system is built. In computer science and software engineering, 
        computer software is all information processed by computer systems, programs and 
        data. Computer software includes computer programs, libraries and related non-executable
        data, such as online documentation or digital media. Computer hardware and software 
        require each other and neither can be realistically used on its own."""
        
        QMessageBox.about(self.amenubar, title, content)
        
     
    
        
        
            

    
