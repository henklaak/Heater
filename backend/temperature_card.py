import random

import sm_tc
from PySide6.QtCore import QTimer, QObject, Slot, Signal


class TemperatureCard(QObject):
    """ Temperature Card readout"""

    def __init__(self, simulate, parent=None):
        super().__init__(parent)

        self._simulate = simulate
        self._simulation_heater = 0.0
        self._simulation_temperature = 20.0

        if not self._simulate:
            self._tc = sm_tc.SMtc()
            for idx in range(sm_tc._IN_CH_COUNT):
                self._tc.set_sensor_type(1 + idx, sm_tc._TC_TYPE_K)

        self._temperatures = [0.0] * sm_tc._IN_CH_COUNT

        self._periodic_timer = QTimer()
        self._periodic_timer.setInterval(1000)  # DTR zal x ms laag worden gemaakt als triggerpuls
        self._periodic_timer.timeout.connect(self._on_periodic_timeout)  # na afloop van timer call deze functie
        self._periodic_timer.start()
        self._on_periodic_timeout()  # Initial measurements

    def get_temperatures(self):
        return self._temperatures

    @Signal
    def temperatures_changed(self):
        """ Signal, emitted when a new measurement is available."""
        ...

    def hint_simulation(self, heater_pwm: float):
        self._simulation_heater = heater_pwm

    def _read_channel(self, idx):
        """
        Args:
             idx (int): Channel index 0-7
        """
        if idx < 0 or idx > 7:
            raise ValueError(f"Idx {idx} out of valid range [0-7]")
        if not self._simulate:
            return self._tc.get_temp(1 + idx)
        else:
            if idx == 0:
                self._simulation_temperature += self._simulation_heater * 5 - (self._simulation_temperature-20) * 0.01
            return self._simulation_temperature  # + random.uniform(-2,2)

    @Slot()
    def _on_periodic_timeout(self):
        """ A measurement is started when the trigger is toggle from low to high. """
        for idx in range(sm_tc._IN_CH_COUNT):
            self._temperatures[idx] = self._read_channel(idx)

        self.temperatures_changed.emit()


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    import sys

    SIMULATE = True

    app = QApplication(sys.argv)

    tc = TemperatureCard(SIMULATE)
    for ch in range(0, 8):
        print(f"Ch: {ch:d}   T: {tc.temperatures()[ch]:5.1f} ℃")

    QTimer.singleShot(5000, lambda: app.quit())

    sys.exit(app.exec())
