from PySide6.QtCore import Slot, QSettings
from PySide6.QtWidgets import QMainWindow

from backend import Backend
from .ui_GUI3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._settings = QSettings("settings.ini", QSettings.Format.IniFormat)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnControllerActive.clicked.connect(self._on_controller_active)
        self.ui.btnLoggingActive.clicked.connect(self._on_logging_active)

        self.ui.edtTemperatureTarget.editingFinished.connect(self._on_user_temperature_target_changed)
        self.ui.edtTemperatureFinal.editingFinished.connect(self._on_user_temperature_final_changed)
        self.ui.edtLoggingInterval.editingFinished.connect(self._on_user_logging_interval_changed)
        self.ui.edtPwmMax.editingFinished.connect(self._on_user_pwm_max_changed)
        self.ui.edtPFactor.editingFinished.connect(self._on_user_pwm_p_factor_changed)

    def set_backend(self, backend: Backend):
        self._backend = backend

        self._backend.heater_pwm_changed.connect(self._on_heater_pwm_changed)
        self._on_heater_pwm_changed()

        self._backend.controller_target_changed.connect(self._on_controller_target_changed)
        self._on_controller_target_changed()

        self._backend.temperatures_changed.connect(self._on_temperatures_changed)
        self._on_temperatures_changed()

        self._backend.micrometer_1_measurement_changed.connect(self._on_micrometer_1_measurement_changed)
        self._on_micrometer_1_measurement_changed()
        self._backend.micrometer_2_measurement_changed.connect(self._on_micrometer_2_measurement_changed)
        self._on_micrometer_2_measurement_changed()

        self._backend.set_controller_active(False)
        temperature_target = float(self._settings.value("temperature_target", 130.0))
        self._settings.setValue("temperature_target", temperature_target)
        self._backend.set_controller_target(temperature_target)
        self.ui.edtTemperatureTarget.setText(f"{temperature_target:.1f}")

        temperature_final = float(self._settings.value("temperature_final", 25.0))
        self._settings.setValue("temperature_final", temperature_final)
        # TODO self._backend.set_controller_target(target)
        self.ui.edtTemperatureFinal.setText(f"{temperature_final:.1f}")

        logging_interval = float(self._settings.value("logging_interval", 2.0))
        self._settings.setValue("logging_interval", logging_interval)
        self._backend.set_logging_interval(logging_interval)
        self.ui.edtLoggingInterval.setText(f"{logging_interval:.1f}")

        max_pwm = float(self._settings.value("max_pwm", 0.25))
        self._settings.setValue("max_pwm", max_pwm)
        self._backend.set_controller_max_pwm(max_pwm)
        self.ui.edtPwmMax.setText(f"{100*max_pwm:.1f}")

        p_factor = float(self._settings.value("p_factor", 0.02))
        self._settings.setValue("p_factor", p_factor)
        self._backend.set_controller_p_factor(p_factor)
        self.ui.edtPFactor.setText(f"{p_factor:.3f}")

    def set_settings(self, settings):
        self._settings = settings

    @Slot(bool)
    def _on_controller_active(self, checked):
        self._backend.set_controller_active(checked)

    @Slot(bool)
    def _on_logging_active(self, checked):
        self._backend.set_logging_active(checked)

    @Slot()
    def _on_user_logging_interval_changed(self):
        logging_interval = float(self.ui.edtLoggingInterval.text())
        self._backend.set_logging_interval(logging_interval)
        self._settings.setValue("logging_interval", logging_interval)

    @Slot()
    def _on_user_temperature_target_changed(self):
        temperature_target = float(self.ui.edtTemperatureTarget.text())
        self._backend.set_controller_target(temperature_target)
        self._settings.setValue("temperature_target", temperature_target)

    @Slot()
    def _on_user_temperature_final_changed(self):
        temperature_final = float(self.ui.edtTemperatureFinal.text())
        # TODO self._backend.set_(temperature_final)
        self._settings.setValue("temperature_final", temperature_final)

    @Slot()
    def _on_user_pwm_max_changed(self):
        pwm_max = float(self.ui.edtPwmMax.text())  / 100
        self._backend.set_controller_max_pwm(pwm_max)
        self._settings.setValue("pwm_max", pwm_max)

    @Slot()
    def _on_user_pwm_p_factor_changed(self):
        p_factor = float(self.ui.edtPFactor.text())  / 100
        self._backend.set_controller_p_factor(p_factor)
        self._settings.setValue("p_factor", p_factor)

    @Slot()
    def _on_heater_pwm_changed(self):
        pwm = self._backend.get_heater_pwm()
        self.ui.pbHeaterPwm.setValue(pwm*100)

    @Slot()
    def _on_temperatures_changed(self):
        temperatures = self._backend.get_temperatures()

        for idx, tc in enumerate([self.ui.pbTC1,
                                  self.ui.pbTC2,
                                  self.ui.pbTC3,
                                  self.ui.pbTC4,
                                  self.ui.pbTC5,
                                  self.ui.pbTC6,
                                  self.ui.pbTC7,
                                  self.ui.pbTC8]):
            tc.setValue(temperatures[idx])

        average_temperature = sum(temperatures) / len(temperatures)

    @Slot()
    def _on_controller_target_changed(self):
        target = self._backend.get_controller_target()
        for idx, tc in enumerate([self.ui.pbTC1,
                                  self.ui.pbTC2,
                                  self.ui.pbTC3,
                                  self.ui.pbTC4,
                                  self.ui.pbTC5,
                                  self.ui.pbTC6,
                                  self.ui.pbTC7,
                                  self.ui.pbTC8]):
            tc.setMaximum(target+5)

    @Slot()
    def _on_controller_max_pwm_changed(self):
        max_pwm = self._backend.get_controller_max_pwm()
        self.ui.pbHeaterPwm.setMaximum(100)#max_pwm*100)


    @Slot()
    def _on_micrometer_1_measurement_changed(self):
        measurement = self._backend.get_micrometer_1_measurement()
        self.ui.pbMicrometer1.setValue(measurement*1000)

    @Slot()
    def _on_micrometer_2_measurement_changed(self):
        measurement = self._backend.get_micrometer_2_measurement()
        self.ui.pbMicrometer2.setValue(measurement*1000)
