from PySide6.QtCore import QObject, QTimer, Slot

from .heater import Heater
from .temperature_card import TemperatureCard

SIMULATE = True


class Controller(QObject):
    """ Temperature controller """

    def __init__(self, temperature_card: TemperatureCard,  # maak instances van classes TemperatureCard en Heater
                 heater: Heater, parent=None):
        """
        Args:
            temperature_card(TemperatureCard): Supplier of temperature measurements
        """
        super().__init__(parent)

        self._temperature_card = temperature_card
        self._heater = heater

        self._max_pwm = 0.25
        self._p_factor = 0.1
        self._target = 40.0  # initi"ele waarde deze wordt door MainWindow via set_target() geschreven.
        self._active = False

        self._timer = QTimer()
        self._timer.setInterval(2000)
        self._timer.timeout.connect(self._on_timeout)
        self._timer.start()

    def set_active(self, active: bool):
        """ Set mode (MODE_IDLE or MODE_ACTIVE """
        self._active = active

    def set_target(self, target: float):
        self._target = target

    def set_max_pwm(self, max_pwm: float):
        self._max_pwm = max_pwm

    def set_p_factor(self, p_factor: float):
        self._p_factor = p_factor

    @Slot()
    def _on_timeout(self):
        """ Control loop step """
        try:
            temperatures = self._temperature_card.get_temperatures()

            if self._active:
                tgt = self._target
                act = temperatures[3]
                err = tgt - act

                pwm = self._p_factor * err
                pwm = max(0.0, min(self._max_pwm, pwm))  # Clamp to 0-0.25
                self._heater.set_pwm(pwm)
            else:
                self._heater.disable()

        except Exception as e:
            self._timer.stop()
            self._heater.disable()
            raise


if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    temperature_card = TemperatureCard()
    heater = Heater()
    ctr = Controller(temperature_card, heater)
    ctr.set_target(60)
    ctr.set_mode(ctr.MODE_ACTIVE)

    QTimer.singleShot(500000, lambda: app.quit())

    sys.exit(app.exec())
