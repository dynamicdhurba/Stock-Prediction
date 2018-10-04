# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arcane2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AppMainWindow(object):
    def setupUi(self, AppMainWindow):
        AppMainWindow.setObjectName("AppMainWindow")
        AppMainWindow.resize(1114, 815)
        AppMainWindow.setMinimumSize(QtCore.QSize(700, 500))
        AppMainWindow.setBaseSize(QtCore.QSize(0, 0))
        AppMainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(AppMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName("tabWidget_main")
        self.tab_technicalAnalysis = QtWidgets.QWidget()
        self.tab_technicalAnalysis.setObjectName("tab_technicalAnalysis")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_technicalAnalysis)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_main.addTab(self.tab_technicalAnalysis, "")
        self.tab_fundamentalAnalysis = QtWidgets.QWidget()
        self.tab_fundamentalAnalysis.setObjectName("tab_fundamentalAnalysis")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_fundamentalAnalysis)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget_main.addTab(self.tab_fundamentalAnalysis, "")
        self.tab_browser = QtWidgets.QWidget()
        self.tab_browser.setObjectName("tab_browser")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_browser)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget_main.addTab(self.tab_browser, "")
        self.verticalLayout_3.addWidget(self.tabWidget_main)
        AppMainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget_companyName = QtWidgets.QDockWidget(AppMainWindow)
        self.dockWidget_companyName.setMinimumSize(QtCore.QSize(200, 76))
        self.dockWidget_companyName.setFloating(False)
        self.dockWidget_companyName.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_companyName.setObjectName("dockWidget_companyName")
        self.dockWidgetContents_companyName = QtWidgets.QWidget()
        self.dockWidgetContents_companyName.setObjectName("dockWidgetContents_companyName")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_companyName)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dockWidget_companyName.setWidget(self.dockWidgetContents_companyName)
        AppMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_companyName)
        self.dockWidget_Welcome = QtWidgets.QDockWidget(AppMainWindow)
        self.dockWidget_Welcome.setObjectName("dockWidget_Welcome")
        self.dockWidgetContents_Welcome = QtWidgets.QWidget()
        self.dockWidgetContents_Welcome.setObjectName("dockWidgetContents_Welcome")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_Welcome)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dockWidget_Welcome.setWidget(self.dockWidgetContents_Welcome)
        AppMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Welcome)
        self.actionExit = QtWidgets.QAction(AppMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHello = QtWidgets.QAction(AppMainWindow)
        self.actionHello.setObjectName("actionHello")
        self.help_actionDocs = QtWidgets.QAction(AppMainWindow)
        self.help_actionDocs.setObjectName("help_actionDocs")
        self.file_actionExit = QtWidgets.QAction(AppMainWindow)
        self.file_actionExit.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.file_actionExit.setObjectName("file_actionExit")
        self.help_actionAbout_Us = QtWidgets.QAction(AppMainWindow)
        self.help_actionAbout_Us.setObjectName("help_actionAbout_Us")

        self.retranslateUi(AppMainWindow)
        self.tabWidget_main.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(AppMainWindow)

    def retranslateUi(self, AppMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AppMainWindow.setWindowTitle(_translate("AppMainWindow", "Arcane"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_technicalAnalysis), _translate("AppMainWindow", "Technical Analysis"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_fundamentalAnalysis), _translate("AppMainWindow", "Fundamental Analysis"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_browser), _translate("AppMainWindow", "Prediction"))
        self.dockWidget_companyName.setWindowTitle(_translate("AppMainWindow", "Company Name"))
        self.dockWidget_Welcome.setWindowTitle(_translate("AppMainWindow", "Models"))
        self.actionExit.setText(_translate("AppMainWindow", "Exit"))
        self.actionHello.setText(_translate("AppMainWindow", "hello"))
        self.help_actionDocs.setText(_translate("AppMainWindow", "Docs"))
        self.file_actionExit.setText(_translate("AppMainWindow", "Exit"))
        self.help_actionAbout_Us.setText(_translate("AppMainWindow", "About Us"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AppMainWindow()
    ui.setupUi(AppMainWindow)
    AppMainWindow.show()
    sys.exit(app.exec_())

