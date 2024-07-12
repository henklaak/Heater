# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

from .xygraph import XYGraph

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1122, 742)
        MainWindow.setMinimumSize(QSize(950, 500))
        self.widgetMainWindow = QWidget(MainWindow)
        self.widgetMainWindow.setObjectName(u"widgetMainWindow")
        self.widgetMainWindow.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widgetMainWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layTopRow = QHBoxLayout()
        self.layTopRow.setObjectName(u"layTopRow")
        self.grpTemperatures = QGroupBox(self.widgetMainWindow)
        self.grpTemperatures.setObjectName(u"grpTemperatures")
        self.formLayout_2 = QFormLayout(self.grpTemperatures)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(self.grpTemperatures)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.pbTC8 = QProgressBar(self.grpTemperatures)
        self.pbTC8.setObjectName(u"pbTC8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbTC8.sizePolicy().hasHeightForWidth())
        self.pbTC8.setSizePolicy(sizePolicy)
        self.pbTC8.setMinimum(20)
        self.pbTC8.setMaximum(100)
        self.pbTC8.setValue(25)
        self.pbTC8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC8.setTextVisible(True)
        self.pbTC8.setInvertedAppearance(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pbTC8)

        self.label_8 = QLabel(self.grpTemperatures)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.pbTC7 = QProgressBar(self.grpTemperatures)
        self.pbTC7.setObjectName(u"pbTC7")
        sizePolicy.setHeightForWidth(self.pbTC7.sizePolicy().hasHeightForWidth())
        self.pbTC7.setSizePolicy(sizePolicy)
        self.pbTC7.setMinimum(20)
        self.pbTC7.setMaximum(100)
        self.pbTC7.setValue(25)
        self.pbTC7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC7.setTextVisible(True)
        self.pbTC7.setInvertedAppearance(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pbTC7)

        self.label_9 = QLabel(self.grpTemperatures)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.pbTC6 = QProgressBar(self.grpTemperatures)
        self.pbTC6.setObjectName(u"pbTC6")
        sizePolicy.setHeightForWidth(self.pbTC6.sizePolicy().hasHeightForWidth())
        self.pbTC6.setSizePolicy(sizePolicy)
        self.pbTC6.setMinimum(20)
        self.pbTC6.setMaximum(100)
        self.pbTC6.setValue(25)
        self.pbTC6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC6.setTextVisible(True)
        self.pbTC6.setInvertedAppearance(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pbTC6)

        self.label_10 = QLabel(self.grpTemperatures)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.pbTC5 = QProgressBar(self.grpTemperatures)
        self.pbTC5.setObjectName(u"pbTC5")
        sizePolicy.setHeightForWidth(self.pbTC5.sizePolicy().hasHeightForWidth())
        self.pbTC5.setSizePolicy(sizePolicy)
        self.pbTC5.setMinimum(20)
        self.pbTC5.setMaximum(100)
        self.pbTC5.setValue(25)
        self.pbTC5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC5.setTextVisible(True)
        self.pbTC5.setInvertedAppearance(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pbTC5)

        self.label_11 = QLabel(self.grpTemperatures)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.pbTC4 = QProgressBar(self.grpTemperatures)
        self.pbTC4.setObjectName(u"pbTC4")
        sizePolicy.setHeightForWidth(self.pbTC4.sizePolicy().hasHeightForWidth())
        self.pbTC4.setSizePolicy(sizePolicy)
        self.pbTC4.setMinimum(20)
        self.pbTC4.setMaximum(100)
        self.pbTC4.setValue(25)
        self.pbTC4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC4.setTextVisible(True)
        self.pbTC4.setInvertedAppearance(False)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pbTC4)

        self.label_12 = QLabel(self.grpTemperatures)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.pbTC3 = QProgressBar(self.grpTemperatures)
        self.pbTC3.setObjectName(u"pbTC3")
        sizePolicy.setHeightForWidth(self.pbTC3.sizePolicy().hasHeightForWidth())
        self.pbTC3.setSizePolicy(sizePolicy)
        self.pbTC3.setMinimum(20)
        self.pbTC3.setMaximum(100)
        self.pbTC3.setValue(25)
        self.pbTC3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC3.setTextVisible(True)
        self.pbTC3.setInvertedAppearance(False)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.pbTC3)

        self.label_13 = QLabel(self.grpTemperatures)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_13)

        self.pbTC2 = QProgressBar(self.grpTemperatures)
        self.pbTC2.setObjectName(u"pbTC2")
        sizePolicy.setHeightForWidth(self.pbTC2.sizePolicy().hasHeightForWidth())
        self.pbTC2.setSizePolicy(sizePolicy)
        self.pbTC2.setMinimum(20)
        self.pbTC2.setMaximum(100)
        self.pbTC2.setValue(25)
        self.pbTC2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC2.setTextVisible(True)
        self.pbTC2.setInvertedAppearance(False)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.pbTC2)

        self.label_14 = QLabel(self.grpTemperatures)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.pbTC1 = QProgressBar(self.grpTemperatures)
        self.pbTC1.setObjectName(u"pbTC1")
        sizePolicy.setHeightForWidth(self.pbTC1.sizePolicy().hasHeightForWidth())
        self.pbTC1.setSizePolicy(sizePolicy)
        self.pbTC1.setMinimum(20)
        self.pbTC1.setMaximum(100)
        self.pbTC1.setValue(25)
        self.pbTC1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC1.setTextVisible(True)
        self.pbTC1.setInvertedAppearance(False)
        self.pbTC1.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.pbTC1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(8, QFormLayout.LabelRole, self.verticalSpacer)


        self.layTopRow.addWidget(self.grpTemperatures)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.grpHeating = QGroupBox(self.widgetMainWindow)
        self.grpHeating.setObjectName(u"grpHeating")
        self.formLayout_3 = QFormLayout(self.grpHeating)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(1, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.pbHeaterPwm = QProgressBar(self.grpHeating)
        self.pbHeaterPwm.setObjectName(u"pbHeaterPwm")
        self.pbHeaterPwm.setValue(24)
        self.pbHeaterPwm.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pbHeaterPwm)

        self.label_17 = QLabel(self.grpHeating)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_17)


        self.verticalLayout_2.addWidget(self.grpHeating)

        self.grpMicrometers = QGroupBox(self.widgetMainWindow)
        self.grpMicrometers.setObjectName(u"grpMicrometers")
        self.formLayout_4 = QFormLayout(self.grpMicrometers)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_15 = QLabel(self.grpMicrometers)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.pbMicrometer2 = QProgressBar(self.grpMicrometers)
        self.pbMicrometer2.setObjectName(u"pbMicrometer2")
        self.pbMicrometer2.setMaximum(1000)
        self.pbMicrometer2.setValue(480)
        self.pbMicrometer2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.pbMicrometer2)

        self.label_16 = QLabel(self.grpMicrometers)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.pbMicrometer1 = QProgressBar(self.grpMicrometers)
        self.pbMicrometer1.setObjectName(u"pbMicrometer1")
        self.pbMicrometer1.setMaximum(1000)
        self.pbMicrometer1.setValue(480)
        self.pbMicrometer1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.pbMicrometer1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_3)


        self.verticalLayout_2.addWidget(self.grpMicrometers)


        self.layTopRow.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.layTopRow)

        self.layBotRow = QHBoxLayout()
        self.layBotRow.setObjectName(u"layBotRow")
        self.groupBox = QGroupBox(self.widgetMainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gvXYGraph = XYGraph(self.groupBox)
        self.gvXYGraph.setObjectName(u"gvXYGraph")

        self.horizontalLayout_3.addWidget(self.gvXYGraph)


        self.layBotRow.addWidget(self.groupBox)

        self.grpControls = QGroupBox(self.widgetMainWindow)
        self.grpControls.setObjectName(u"grpControls")
        self.verticalLayout = QVBoxLayout(self.grpControls)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.grpControls)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edtTemperatureTarget = QLineEdit(self.grpControls)
        self.edtTemperatureTarget.setObjectName(u"edtTemperatureTarget")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edtTemperatureTarget)

        self.label_2 = QLabel(self.grpControls)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.edtTemperatureFinal = QLineEdit(self.grpControls)
        self.edtTemperatureFinal.setObjectName(u"edtTemperatureFinal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edtTemperatureFinal)

        self.label_3 = QLabel(self.grpControls)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.edtLoggingInterval = QLineEdit(self.grpControls)
        self.edtLoggingInterval.setObjectName(u"edtLoggingInterval")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edtLoggingInterval)

        self.label_4 = QLabel(self.grpControls)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.edtPwmMax = QLineEdit(self.grpControls)
        self.edtPwmMax.setObjectName(u"edtPwmMax")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edtPwmMax)

        self.label_5 = QLabel(self.grpControls)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.edtPFactor = QLineEdit(self.grpControls)
        self.edtPFactor.setObjectName(u"edtPFactor")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.edtPFactor)

        self.label_6 = QLabel(self.grpControls)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.edtLoggingFolder = QLineEdit(self.grpControls)
        self.edtLoggingFolder.setObjectName(u"edtLoggingFolder")

        self.horizontalLayout_2.addWidget(self.edtLoggingFolder)

        self.tbSelectFolder = QToolButton(self.grpControls)
        self.tbSelectFolder.setObjectName(u"tbSelectFolder")

        self.horizontalLayout_2.addWidget(self.tbSelectFolder)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnControllerActive = QPushButton(self.grpControls)
        self.btnControllerActive.setObjectName(u"btnControllerActive")
        self.btnControllerActive.setCheckable(True)
        self.btnControllerActive.setChecked(False)

        self.verticalLayout_4.addWidget(self.btnControllerActive)

        self.btnLoggingActive = QPushButton(self.grpControls)
        self.btnLoggingActive.setObjectName(u"btnLoggingActive")
        self.btnLoggingActive.setCheckable(True)
        self.btnLoggingActive.setChecked(False)

        self.verticalLayout_4.addWidget(self.btnLoggingActive)

        self.btnClearChart = QPushButton(self.grpControls)
        self.btnClearChart.setObjectName(u"btnClearChart")

        self.verticalLayout_4.addWidget(self.btnClearChart)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.layBotRow.addWidget(self.grpControls)

        self.layBotRow.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.layBotRow)

        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.widgetMainWindow)
        QWidget.setTabOrder(self.btnLoggingActive, self.edtTemperatureTarget)
        QWidget.setTabOrder(self.edtTemperatureTarget, self.edtTemperatureFinal)
        QWidget.setTabOrder(self.edtTemperatureFinal, self.edtLoggingInterval)
        QWidget.setTabOrder(self.edtLoggingInterval, self.edtPwmMax)
        QWidget.setTabOrder(self.edtPwmMax, self.edtPFactor)
        QWidget.setTabOrder(self.edtPFactor, self.edtLoggingFolder)
        QWidget.setTabOrder(self.edtLoggingFolder, self.tbSelectFolder)

        self.retranslateUi(MainWindow)

        self.btnControllerActive.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Heater control", None))
        self.grpTemperatures.setTitle(QCoreApplication.translate("MainWindow", u"Temperatures", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TC1", None))
        self.pbTC8.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TC2", None))
        self.pbTC7.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TC3", None))
        self.pbTC6.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TC4", None))
        self.pbTC5.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TC5", None))
        self.pbTC4.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TC6", None))
        self.pbTC3.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TC7", None))
        self.pbTC2.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TC8", None))
        self.pbTC1.setFormat(QCoreApplication.translate("MainWindow", u"%v \u2103", None))
        self.grpHeating.setTitle(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.pbHeaterPwm.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.grpMicrometers.setTitle(QCoreApplication.translate("MainWindow", u"Micrometers", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MM1", None))
        self.pbMicrometer2.setFormat(QCoreApplication.translate("MainWindow", u"%v \u00b5m", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"MM2", None))
        self.pbMicrometer1.setFormat(QCoreApplication.translate("MainWindow", u"%v \u00b5m", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.grpControls.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Target temperature:", None))
        self.edtTemperatureTarget.setText(QCoreApplication.translate("MainWindow", u"(not available)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Final temperature:", None))
        self.edtTemperatureFinal.setText(QCoreApplication.translate("MainWindow", u"(not available)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logging interval:", None))
        self.edtLoggingInterval.setText(QCoreApplication.translate("MainWindow", u"(not available)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Maximum heater power:", None))
        self.edtPwmMax.setText(QCoreApplication.translate("MainWindow", u"(not available)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Controller P-factor:", None))
        self.edtPFactor.setText(QCoreApplication.translate("MainWindow", u"(not available)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Logging folder:", None))
        self.edtLoggingFolder.setText(QCoreApplication.translate("MainWindow", u"(not available)", None))
        self.tbSelectFolder.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnControllerActive.setText(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.btnLoggingActive.setText(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.btnClearChart.setText(QCoreApplication.translate("MainWindow", u"Clear chart", None))
    # retranslateUi

