# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 23:14:16 2017

@author: kishor

    Description:
        Basic browser.

"""

from PyQt5.QtWebKitWidgets import QWebView # note: this module has been removed in some latest versions of PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget
import logging

from arcaneUI import Ui_AppMainWindow


module_logger = logging.getLogger('mainApp.browser')


class ArcaneBrowser(QWebView, Ui_AppMainWindow):
    """Arcane browser class."""
    
    def __init__(self, mainwinref, url, layout, zoomfactor, parent=None):
        module_logger.info("Inside 'ArcaneBrowser' constructor.")
        
        QWebView.__init__(self, parent)
        
        self.mainwinref = mainwinref

        
        #url = "https://google.com"
        
        self.view = QWebView()
        
        self.view.setFixedSize(1700, 1000)
        
        self.view.setZoomFactor(zoomfactor) #zoom
        
        self.view.setUrl(QUrl(url))
        
        layout.addWidget(self.view)

        module_logger.info("Done.")
    

    
    
