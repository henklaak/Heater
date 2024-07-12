from PySide6.QtWidgets import QDialog

from .ui_Settings import Ui_Dialog


class Settings(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()  # De tweede .ui file bevat een QDialog, gemaakt in Qt designer. Deze
        # class is ge"importeerd als(met naam): Ui_Dialog2.
        self.ui.setupUi(self)  # setup van alle buttons, labels etc zoals gemaakt in designer.
        # self._MaxTemp = 0
        # self.ui.bttnUseNewSettings.clicked.connect(self.checksettings)  # connect een button met een method()
        # self.ui.bttnUpdate.clicked.connect(self.read_coldjunctions_tc_board)  # connect een button met een method()
        # self.ui.bttnUpdate.clicked.connect(self.read_sensor_type)  # connect een button met een method()
        # self.ui.bttnMain.clicked.connect(self.gotoMainscreen)
        # Todo: vul de initiele waardes met getallen uit de ini-file en save nieuwe waardes in die ini-file
        # Gebruik hiervoor QSettings (class met alle settings)

        self.ui.pushButton_OK.clicked.connect(self.gotoMainscreen)

        # self.ui.buttonBox.accepted.connect(self.accept())       # Todo button click' s werken niet.
        # self.ui.buttonBox.rejected.connect(self.reject())

    def get_max_temperature(self) -> float:
        return float(self.ui.inGUI_MaxTemp.text())
        # self._MaxTemp = float(self.ui.inGUI_MaxTemp.text())
        # return self._MaxTemp

    def get_log_interval(self) -> int:
        return int(self.ui.inGUI_LogInterval.text())

    def get_log_stop_temperature(self) -> int:
        return int(self.ui.inGUI_StopTemp.text())

    def get_max_duty_cycle(self) -> int:
        return int(self.ui.inGUI_heater_max_duty_cycle.text())

    def get_heater_P_actie(self) -> int:
        return int(self.ui.inGUI_heater_p_actie.text())

    def gotoMainscreen(self):
        self.close()  # Sluit het settings screen. Het main screen is nog open.

    # def checksettings(self):
    #     global max_temp
    #     global log_interval
    #     global stop_temp
    #     global heater_max_duty_cycle
    #     global heater_p_control
    #     max_temp = self.ui.inGUI_MaxTemp.value()         # invoerveld in ui (QDialog settings) van deze class (self)
    #     print("The maximum temperature set is: ", max_temp, " [C]")
    #     if max_temp < 0:
    #         print("Maximale temperatuur moet hoger zijn dan 0.")
    #     if max_temp > 130:
    #         print("Maximale temperatuur mag niet hoger zijn dan 130 C.")
    #
    #     log_interval = self.ui.inGUI_LogInterval.value()
    #     print("Logging interval is: ", log_interval, " [sec]")
    #     stop_temp = self.ui.inGUI_StopTemp.value()
    #     print("Stop temperature is: ", stop_temp, " [C]")
    #     heater_max_duty_cycle = self.ui.inGUI_heater_max_duty_cycle.value()
    #     print("Heater max duty cycle is: ", heater_max_duty_cycle, " [%]")
    #     heater_p_control = self.ui.inGUI_heater_p_actie.value() / 10.0
    #     print("Heater P-actie is: ", heater_p_control)

    # def read_coldjunctions_tc_board(self):
    #     # tc.   geen fucntie beschikbaar in de python lib (wel op de command line)
    #     self.ui.lcdNumber_cj_1.display(0.0)
    #     self.ui.lcdNumber_cj_2.display(0.0)
    #     self.ui.lcdNumber_cj_3.display(0.0)
    #     self.ui.lcdNumber_cj_4.display(0.0)
    #     self.ui.lcdNumber_cj_5.display(0.0)
    #     self.ui.lcdNumber_cj_6.display(0.0)
    #     self.ui.lcdNumber_cj_7.display(0.0)
    #     self.ui.lcdNumber_cj_8.display(0.0)
    #     return 0
    #
    # def read_sensor_type(self):
    #     self.ui.TC_type_1.setText(str(tc.get_sensor_type(1)))  # 3 = sensor type K
    #     self.ui.TC_type_2.setText(str(tc.get_sensor_type(2)))
    #     self.ui.TC_type_3.setText(str(tc.get_sensor_type(3)))
    #     self.ui.TC_type_4.setText(str(tc.get_sensor_type(4)))
    #     self.ui.TC_type_5.setText(str(tc.get_sensor_type(5)))
    #     self.ui.TC_type_6.setText(str(tc.get_sensor_type(6)))
    #     self.ui.TC_type_7.setText(str(tc.get_sensor_type(7)))
    #     self.ui.TC_type_8.setText(str(tc.get_sensor_type(8)))
