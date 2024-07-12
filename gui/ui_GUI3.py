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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(989, 764)
        MainWindow.setMinimumSize(QSize(950, 500))
        self.widgetMainWindow = QWidget(MainWindow)
        self.widgetMainWindow.setObjectName(u"widgetMainWindow")
        self.widgetMainWindow.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widgetMainWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.widgetMainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pbTC1 = QProgressBar(self.groupBox)
        self.pbTC1.setObjectName(u"pbTC1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbTC1.sizePolicy().hasHeightForWidth())
        self.pbTC1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(32)
        self.pbTC1.setFont(font)
        self.pbTC1.setMinimum(0)
        self.pbTC1.setMaximum(150)
        self.pbTC1.setValue(20)
        self.pbTC1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC1.setTextVisible(True)
        self.pbTC1.setOrientation(Qt.Orientation.Vertical)
        self.pbTC1.setInvertedAppearance(False)
        self.pbTC1.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.horizontalLayout_3.addWidget(self.pbTC1)

        self.pbTC2 = QProgressBar(self.groupBox)
        self.pbTC2.setObjectName(u"pbTC2")
        sizePolicy.setHeightForWidth(self.pbTC2.sizePolicy().hasHeightForWidth())
        self.pbTC2.setSizePolicy(sizePolicy)
        self.pbTC2.setFont(font)
        self.pbTC2.setMaximum(150)
        self.pbTC2.setValue(24)
        self.pbTC2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC2.setTextVisible(True)
        self.pbTC2.setOrientation(Qt.Orientation.Vertical)
        self.pbTC2.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC2)

        self.pbTC3 = QProgressBar(self.groupBox)
        self.pbTC3.setObjectName(u"pbTC3")
        sizePolicy.setHeightForWidth(self.pbTC3.sizePolicy().hasHeightForWidth())
        self.pbTC3.setSizePolicy(sizePolicy)
        self.pbTC3.setFont(font)
        self.pbTC3.setMaximum(150)
        self.pbTC3.setValue(24)
        self.pbTC3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC3.setTextVisible(True)
        self.pbTC3.setOrientation(Qt.Orientation.Vertical)
        self.pbTC3.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC3)

        self.pbTC4 = QProgressBar(self.groupBox)
        self.pbTC4.setObjectName(u"pbTC4")
        sizePolicy.setHeightForWidth(self.pbTC4.sizePolicy().hasHeightForWidth())
        self.pbTC4.setSizePolicy(sizePolicy)
        self.pbTC4.setFont(font)
        self.pbTC4.setMaximum(150)
        self.pbTC4.setValue(24)
        self.pbTC4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC4.setTextVisible(True)
        self.pbTC4.setOrientation(Qt.Orientation.Vertical)
        self.pbTC4.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC4)

        self.pbTC5 = QProgressBar(self.groupBox)
        self.pbTC5.setObjectName(u"pbTC5")
        sizePolicy.setHeightForWidth(self.pbTC5.sizePolicy().hasHeightForWidth())
        self.pbTC5.setSizePolicy(sizePolicy)
        self.pbTC5.setFont(font)
        self.pbTC5.setMaximum(150)
        self.pbTC5.setValue(24)
        self.pbTC5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC5.setTextVisible(True)
        self.pbTC5.setOrientation(Qt.Orientation.Vertical)
        self.pbTC5.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC5)

        self.pbTC6 = QProgressBar(self.groupBox)
        self.pbTC6.setObjectName(u"pbTC6")
        sizePolicy.setHeightForWidth(self.pbTC6.sizePolicy().hasHeightForWidth())
        self.pbTC6.setSizePolicy(sizePolicy)
        self.pbTC6.setFont(font)
        self.pbTC6.setMaximum(150)
        self.pbTC6.setValue(24)
        self.pbTC6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC6.setTextVisible(True)
        self.pbTC6.setOrientation(Qt.Orientation.Vertical)
        self.pbTC6.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC6)

        self.pbTC7 = QProgressBar(self.groupBox)
        self.pbTC7.setObjectName(u"pbTC7")
        sizePolicy.setHeightForWidth(self.pbTC7.sizePolicy().hasHeightForWidth())
        self.pbTC7.setSizePolicy(sizePolicy)
        self.pbTC7.setFont(font)
        self.pbTC7.setMaximum(150)
        self.pbTC7.setValue(24)
        self.pbTC7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC7.setTextVisible(True)
        self.pbTC7.setOrientation(Qt.Orientation.Vertical)
        self.pbTC7.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC7)

        self.pbTC8 = QProgressBar(self.groupBox)
        self.pbTC8.setObjectName(u"pbTC8")
        sizePolicy.setHeightForWidth(self.pbTC8.sizePolicy().hasHeightForWidth())
        self.pbTC8.setSizePolicy(sizePolicy)
        self.pbTC8.setFont(font)
        self.pbTC8.setMaximum(150)
        self.pbTC8.setValue(24)
        self.pbTC8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbTC8.setTextVisible(True)
        self.pbTC8.setOrientation(Qt.Orientation.Vertical)
        self.pbTC8.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.pbTC8)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_3 = QGroupBox(self.widgetMainWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pbHeaterPwm = QProgressBar(self.groupBox_3)
        self.pbHeaterPwm.setObjectName(u"pbHeaterPwm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pbHeaterPwm.sizePolicy().hasHeightForWidth())
        self.pbHeaterPwm.setSizePolicy(sizePolicy1)
        self.pbHeaterPwm.setFont(font)
        self.pbHeaterPwm.setValue(24)
        self.pbHeaterPwm.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbHeaterPwm.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_5.addWidget(self.pbHeaterPwm)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.widgetMainWindow)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edtTemperatureTarget = QLineEdit(self.groupBox_4)
        self.edtTemperatureTarget.setObjectName(u"edtTemperatureTarget")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edtTemperatureTarget)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.edtTemperatureFinal = QLineEdit(self.groupBox_4)
        self.edtTemperatureFinal.setObjectName(u"edtTemperatureFinal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edtTemperatureFinal)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.edtLoggingInterval = QLineEdit(self.groupBox_4)
        self.edtLoggingInterval.setObjectName(u"edtLoggingInterval")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edtLoggingInterval)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.edtPwmMax = QLineEdit(self.groupBox_4)
        self.edtPwmMax.setObjectName(u"edtPwmMax")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edtPwmMax)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.edtPFactor = QLineEdit(self.groupBox_4)
        self.edtPFactor.setObjectName(u"edtPFactor")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.edtPFactor)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnControllerActive = QPushButton(self.groupBox_4)
        self.btnControllerActive.setObjectName(u"btnControllerActive")
        self.btnControllerActive.setCheckable(True)
        self.btnControllerActive.setChecked(False)

        self.horizontalLayout.addWidget(self.btnControllerActive)

        self.btnLoggingActive = QPushButton(self.groupBox_4)
        self.btnLoggingActive.setObjectName(u"btnLoggingActive")
        self.btnLoggingActive.setCheckable(True)
        self.btnLoggingActive.setChecked(False)

        self.horizontalLayout.addWidget(self.btnLoggingActive)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.widgetMainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pbMicrometer1 = QProgressBar(self.groupBox_2)
        self.pbMicrometer1.setObjectName(u"pbMicrometer1")
        sizePolicy1.setHeightForWidth(self.pbMicrometer1.sizePolicy().hasHeightForWidth())
        self.pbMicrometer1.setSizePolicy(sizePolicy1)
        self.pbMicrometer1.setFont(font)
        self.pbMicrometer1.setMaximum(1000)
        self.pbMicrometer1.setValue(480)
        self.pbMicrometer1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbMicrometer1.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_4.addWidget(self.pbMicrometer1)

        self.pbMicrometer2 = QProgressBar(self.groupBox_2)
        self.pbMicrometer2.setObjectName(u"pbMicrometer2")
        sizePolicy1.setHeightForWidth(self.pbMicrometer2.sizePolicy().hasHeightForWidth())
        self.pbMicrometer2.setSizePolicy(sizePolicy1)
        self.pbMicrometer2.setFont(font)
        self.pbMicrometer2.setMaximum(1000)
        self.pbMicrometer2.setValue(480)
        self.pbMicrometer2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pbMicrometer2.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_4.addWidget(self.pbMicrometer2)


        self.horizontalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.widgetMainWindow)

        self.retranslateUi(MainWindow)

        self.btnControllerActive.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Heater control", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Temperatures", None))
        self.pbTC1.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC2.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC3.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC4.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC5.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC6.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC7.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbTC8.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.pbHeaterPwm.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
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
        self.btnControllerActive.setText(QCoreApplication.translate("MainWindow", u"Heating", None))
        self.btnLoggingActive.setText(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Micrometers", None))
        self.pbMicrometer1.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
        self.pbMicrometer2.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
    # retranslateUi

