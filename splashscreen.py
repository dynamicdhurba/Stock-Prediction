# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:45:43 2017

@author: kishor

Description:
        Contains custom Splashscreen class.

"""
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap, QMovie
import logging

module_logger = logging.getLogger('mainApp.splashscreen')


class ArcaneSplashScreen(QSplashScreen):
    """Arcane splashscreen. Shows gif while starting the application."""
    
    def __init__(self, animation):
        module_logger.info("Inside 'ArcaneSplashScreen' constructor.")

        QSplashScreen.__init__(self, QPixmap())
        self.movie = QMovie(animation)
        
        self.movie.frameChanged.connect(self.onNextFrame)
        
        self.movie.start()
        
        module_logger.info("Done.")

    #slot
    def onNextFrame(self):
        pixmap = self.movie.currentPixmap() # returns current frame
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask()) #causes only frame to be visible ie transparent, depending upon the system















    