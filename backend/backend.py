from PySide6.QtCore import QObject, Signal, Slot

from .controller import Controller
from .heater import Heater
from .logger import Logger
from .micrometer import Micrometer
from .temperature_card import TemperatureCard

SIMULATE = True


class Backend(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._temperature_card = TemperatureCard(SIMULATE)
        self._temperature_card.temperatures_changed.connect(self.temperatures_changed)
        self._temperature_card.temperatures_changed.connect(self._on_temperature_changed)

        self._heater = Heater(SIMULATE)
        self._heater.pwm_changed.connect(self.heater_pwm_changed)
        self._heater.pwm_changed.connect(self._on_heater_pwm_changed)
        self._heater.state_changed.connect(self.heater_state_changed)
        self._heater.disable()

        self._controller = Controller(self._temperature_card, self._heater)
        self._controller.active_changed.connect(self.controller_active_changed)
        self._controller.target_changed.connect(self.controller_target_changed)

        self._micrometer_1 = Micrometer('AGCQj137C01', SIMULATE)
        self._micrometer_1.measurement_changed.connect(self.micrometer_1_measurement_changed)
        self._micrometer_2 = Micrometer('BBDDj137C01', SIMULATE)
        self._micrometer_2.measurement_changed.connect(self.micrometer_2_measurement_changed)

        self._logger = Logger(self._temperature_card, [self._micrometer_1, self._micrometer_2])
        self._on_temperature_changed()

    def get_temperatures(self):
        return self._temperature_card.get_temperatures()

    @Signal
    def temperatures_changed(self):
        ...

    @Slot()
    def _on_temperature_changed(self):
        temperatures = self._temperature_card.get_temperatures()
        self._micrometer_1.hint_simulation(temperatures[0])
        self._micrometer_2.hint_simulation(temperatures[-1])

    def get_heater_pwm(self):
        return self._heater.get_pwm()

    @Signal
    def heater_pwm_changed(self):
        ...

    @Slot()
    def _on_heater_pwm_changed(self):
        pwm = self._heater.get_pwm()
        self._temperature_card.hint_simulation(pwm)

    def get_heater_state(self):
        return self._heater.get_state()

    @Signal
    def heater_state_changed(self):
        ...

    def set_controller_active(self, active):
        return self._controller.set_active(active)

    def get_controller_active(self):
        return self._controller.get_active()

    @Signal
    def controller_active_changed(self):
        ...

    def set_controller_target(self, target):
        return self._controller.set_target(target)

    def get_controller_target(self):
        return self._controller.get_target()

    @Signal
    def controller_target_changed(self):
        ...

    def set_controller_max_pwm(self, max_pwm):
        self._controller.set_max_pwm(max_pwm)

    def set_controller_p_factor(self, p_factor):
        self._controller.set_p_factor(p_factor)

    def get_controller_max_pwm(self):
        return self._controller.get_max_pwm()


    def get_micrometer_1_measurement(self):
        return self._micrometer_1.get_measurement()

    @Signal
    def micrometer_1_measurement_changed(self):
        ...

    def get_micrometer_2_measurement(self):
        return self._micrometer_2.get_measurement()

    @Signal
    def micrometer_2_measurement_changed(self):
        ...

    def set_logging_active(self, active):
        return self._logger.set_active(active)

    def set_logging_interval(self, interval):
        self._logger.set_logging_interval(interval)