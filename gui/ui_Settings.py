# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(670, 314)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_heater_duty_cycle = QLabel(Dialog)
        self.label_heater_duty_cycle.setObjectName(u"label_heater_duty_cycle")
        self.label_heater_duty_cycle.setStyleSheet(u"")
        self.label_heater_duty_cycle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_heater_duty_cycle, 3, 0, 1, 1)

        self.inGUI_MaxTemp = QSpinBox(Dialog)
        self.inGUI_MaxTemp.setObjectName(u"inGUI_MaxTemp")
        self.inGUI_MaxTemp.setMaximum(130)
        self.inGUI_MaxTemp.setValue(130)

        self.gridLayout.addWidget(self.inGUI_MaxTemp, 0, 1, 1, 1)

        self.label_heater_p_actie = QLabel(Dialog)
        self.label_heater_p_actie.setObjectName(u"label_heater_p_actie")
        self.label_heater_p_actie.setStyleSheet(u"")
        self.label_heater_p_actie.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_heater_p_actie, 4, 0, 1, 1)

        self.label_MaxTemperatuur = QLabel(Dialog)
        self.label_MaxTemperatuur.setObjectName(u"label_MaxTemperatuur")
        self.label_MaxTemperatuur.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_MaxTemperatuur, 0, 0, 1, 1)

        self.label_StopTemperatuur = QLabel(Dialog)
        self.label_StopTemperatuur.setObjectName(u"label_StopTemperatuur")
        self.label_StopTemperatuur.setStyleSheet(u"")
        self.label_StopTemperatuur.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_StopTemperatuur, 2, 0, 1, 1)

        self.label_StopTemperatuur2 = QLabel(Dialog)
        self.label_StopTemperatuur2.setObjectName(u"label_StopTemperatuur2")
        self.label_StopTemperatuur2.setStyleSheet(u"")
        self.label_StopTemperatuur2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_StopTemperatuur2, 2, 2, 1, 1)

        self.label_heater_p_actie_2 = QLabel(Dialog)
        self.label_heater_p_actie_2.setObjectName(u"label_heater_p_actie_2")
        self.label_heater_p_actie_2.setStyleSheet(u"")
        self.label_heater_p_actie_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_heater_p_actie_2, 4, 2, 1, 1)

        self.label_CT4 = QLabel(Dialog)
        self.label_CT4.setObjectName(u"label_CT4")
        self.label_CT4.setStyleSheet(u"")
        self.label_CT4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_CT4, 1, 0, 1, 1)

        self.inGUI_StopTemp = QSpinBox(Dialog)
        self.inGUI_StopTemp.setObjectName(u"inGUI_StopTemp")
        self.inGUI_StopTemp.setMaximum(130)
        self.inGUI_StopTemp.setValue(30)

        self.gridLayout.addWidget(self.inGUI_StopTemp, 2, 1, 1, 1)

        self.inGUI_LogInterval = QSpinBox(Dialog)
        self.inGUI_LogInterval.setObjectName(u"inGUI_LogInterval")
        self.inGUI_LogInterval.setMinimum(2)
        self.inGUI_LogInterval.setMaximum(900)
        self.inGUI_LogInterval.setValue(2)

        self.gridLayout.addWidget(self.inGUI_LogInterval, 1, 1, 1, 1)

        self.label_Temperaturen_3 = QLabel(Dialog)
        self.label_Temperaturen_3.setObjectName(u"label_Temperaturen_3")
        self.label_Temperaturen_3.setStyleSheet(u"")
        self.label_Temperaturen_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_Temperaturen_3, 1, 2, 1, 1)

        self.inGUI_heater_max_duty_cycle = QSpinBox(Dialog)
        self.inGUI_heater_max_duty_cycle.setObjectName(u"inGUI_heater_max_duty_cycle")
        self.inGUI_heater_max_duty_cycle.setMinimum(1)
        self.inGUI_heater_max_duty_cycle.setMaximum(25)
        self.inGUI_heater_max_duty_cycle.setValue(25)

        self.gridLayout.addWidget(self.inGUI_heater_max_duty_cycle, 3, 1, 1, 1)

        self.inGUI_heater_p_actie = QSpinBox(Dialog)
        self.inGUI_heater_p_actie.setObjectName(u"inGUI_heater_p_actie")
        self.inGUI_heater_p_actie.setMinimum(1)
        self.inGUI_heater_p_actie.setMaximum(10)
        self.inGUI_heater_p_actie.setValue(3)

        self.gridLayout.addWidget(self.inGUI_heater_p_actie, 4, 1, 1, 1)

        self.label_heater_duty_cycle_2 = QLabel(Dialog)
        self.label_heater_duty_cycle_2.setObjectName(u"label_heater_duty_cycle_2")
        self.label_heater_duty_cycle_2.setStyleSheet(u"")
        self.label_heater_duty_cycle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_heater_duty_cycle_2, 3, 2, 1, 1)

        self.label_Temperaturen_2 = QLabel(Dialog)
        self.label_Temperaturen_2.setObjectName(u"label_Temperaturen_2")
        self.label_Temperaturen_2.setStyleSheet(u"")
        self.label_Temperaturen_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_Temperaturen_2, 0, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)

        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton_OK = QPushButton(Dialog)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.verticalLayout.addWidget(self.pushButton_OK)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_heater_duty_cycle.setText(QCoreApplication.translate("Dialog", u"Heater max duty cycle", None))
        self.inGUI_MaxTemp.setPrefix("")
        self.label_heater_p_actie.setText(QCoreApplication.translate("Dialog", u"Heater P-actie", None))
        self.label_MaxTemperatuur.setText(QCoreApplication.translate("Dialog", u"Max. Temperatuur", None))
        self.label_StopTemperatuur.setText(QCoreApplication.translate("Dialog", u"Stop Temperatuur", None))
        self.label_StopTemperatuur2.setText(QCoreApplication.translate("Dialog", u"[\u2103]", None))
        self.label_heater_p_actie_2.setText(QCoreApplication.translate("Dialog", u"[ - ]", None))
        self.label_CT4.setText(QCoreApplication.translate("Dialog", u"Log interval", None))
        self.label_Temperaturen_3.setText(QCoreApplication.translate("Dialog", u"[s]", None))
#if QT_CONFIG(tooltip)
        self.inGUI_heater_max_duty_cycle.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_heater_duty_cycle_2.setText(QCoreApplication.translate("Dialog", u"[%]", None))
        self.label_Temperaturen_2.setText(QCoreApplication.translate("Dialog", u"[\u2103]", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"(max. 130 \u2103)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"(2...900 s)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"(stop loggen als gem. temp lager is dan deze waarde)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"(1...25 %)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"(1...10 => x/10 => p = 0.1...1.0)", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

