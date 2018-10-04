# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:30:00 2017

@author: kishor

Description :
    uses matplotlib to plot various data.

"""

import matplotlib
matplotlib.use('Qt5Agg')
#matplotlib.style.use('ggplot')


from PyQt5 import QtWidgets

import numpy as np
import pandas as pd

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import logging


module_logger = logging.getLogger('mainApp.plotter')



class ArcaneMplCanvas(FigureCanvas):
    """Canvas to plot 'Figure' objects"""
    
    def __init__(self, parent=None, width=17, height=9, dpi=100):
        module_logger.info("Inside 'ArcaneMplCanvas' constructor.")
        
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111, facecolor='#000000')

        FigureCanvas.__init__(self,fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding
                                   )
        FigureCanvas.updateGeometry(self)
        
        module_logger.info("Done.")

    
class ArcanePlotterMplCanvas(ArcaneMplCanvas):
    '''Class where we plot all the graphs'''
    
    def plotsine(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*(np.pi)*t)
        self.axes.plot(t, s)
    
    def plotcosine(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.cos(2*(np.pi)*t)
        self.axes.plot(t, s)   
        


        
    
    
    
    
    



