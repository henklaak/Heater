import gpiod
from PySide6.QtCore import QObject, QTimer, Slot, Signal
from gpiod.line import Direction, Value


class Heater(QObject):
    GPIO_HEATER = 18  # Heater output
    PERIOD = 1000  # pwm period in ms

    """ Heater, simple on off """

    def __init__(self, simulate):
        super().__init__()

        self._simulate = simulate
        self._pwm = 0.0
        self._period_on = 0
        self._period_off = self.PERIOD
        self._timer = QTimer()
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._on_period_timeout)
        self._pwm_state = False

        if not self._simulate:
            self._gpio_request = gpiod.request_lines("/dev/gpiochip4", consumer="solid-state-relay", config={
                self.GPIO_HEATER: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)})

    def get_pwm(self):
        return self._pwm

    def set_pwm(self, fraction: float):
        if fraction <= 0.01:
            self.disable()
            return

        self._pwm = fraction
        if fraction <= 0.01 or fraction > 1.0:
            raise RuntimeError(f"Invalid fraction {fraction}, must be [0.01 - 1.0]")
        self._period_on = int(fraction * self.PERIOD)
        self._period_off = int(self.PERIOD - self._period_on)
        self._timer.setInterval(self._period_on)
        self._timer.start()
        self._set_state(True)
        self.pwm_changed.emit()

    @Signal
    def pwm_changed(self):
        ...

    def disable(self):
        self._pwm = 0.0
        self.pwm_changed.emit()
        self._timer.stop()
        self._set_state(False)

    @Slot()
    def _on_period_timeout(self):
        if self._pwm_state:
            self._timer.setInterval(self._period_off)
            self._timer.start()
            self._set_state(False)
        else:
            self._timer.setInterval(self._period_on)
            self._timer.start()
            self._set_state(True)

    def get_state(self):
        return self._pwm_state

    def _set_state(self, on: bool):
        """ Set heater on or off
        Args:
            on(bool): Heater on
        """
        self._pwm_state = on
        if not self._simulate:
            self._gpio_request.set_value(self.GPIO_HEATER,
                                         Value.ACTIVE if on else Value.INACTIVE)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    SIMULATE = True

    app = QApplication(sys.argv)

    heater = Heater(SIMULATE)
    heater.set_pwm(0.1)

    app.exec()
