import random

from PySide6.QtCore import QIODevice, QObject, Signal, QTimer, Slot
from PySide6.QtSerialPort import QSerialPortInfo, QSerialPort


class Micrometer(QObject):
    """Micrometer class, to be used for reading out a MarCator micrometer."""

    def __init__(self, serial_number: str, simulate, parent=None):
        """
        Args:
            serial_number (str): Serial number of the serial port (USB-RS232 converter).
        """
        super().__init__(parent)
        self._simulate = simulate
        self._simulation_temperature = 20.0

        self._measurement = 0.0

        if not self._simulate:
            self._data = ""

            # Find Serial port with serial_number (USB-poortnaam zou nl ooit kunnen veranderen)
            self._serial_port_info = None
            serial_port_infos = QSerialPortInfo.availablePorts()
            available_ports = []
            for serial_port_info in serial_port_infos:
                available_ports.append(serial_port_info.serialNumber())
                if serial_port_info.serialNumber() == serial_number:
                    self._serial_port_info = serial_port_info

            if self._serial_port_info is None:
                raise RuntimeError(f"Serial port {serial_number} not found. "
                                   f"Found: {', '.join(available_ports)}")

            self._serial = QSerialPort(self._serial_port_info)
            self._serial.setBaudRate(4800)
            self._serial.setStopBits(QSerialPort.StopBits.TwoStop)
            self._serial.setDataBits(QSerialPort.DataBits.Data7)
            self._serial.setParity(QSerialPort.Parity.EvenParity)
            self._serial.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
            self._serial.open(QIODevice.ReadOnly)
            self._serial.setRequestToSend(True)  # Abused for powering device
            self._serial.setDataTerminalReady(True)

            self._serial.readyRead.connect(self._on_ready_read)  # Qt geeft aan als de read klaar is

        self._periodic_timer = QTimer()
        self._periodic_timer.setInterval(1000)  # DTR zal x ms laag worden gemaakt als triggerpuls
        self._periodic_timer.timeout.connect(self._on_periodic_timeout)  # na afloop van timer call deze functie
        self._periodic_timer.start()

        self._pulse_timer = QTimer()
        self._pulse_timer.setSingleShot(True)
        self._pulse_timer.setInterval(250)  # DTR zal x ms laag worden gemaakt als triggerpuls
        self._pulse_timer.timeout.connect(self._on_pulse_timeout)  # na afloop van timer call deze functie

    def get_measurement(self) -> float:
        """ Return most recent measurement in meters."""
        return self._measurement

    @Signal
    def measurement_changed(self):
        """ Signal, emitted when a new measurement is available."""
        ...

    def hint_simulation(self, temperature: float):
        self._simulation_temperature = temperature

    def _on_ready_read(self):
        """ Handle incoming serial port bytes """
        if self._simulate:
            self._measurement = self._simulation_temperature * 0.01  + random.uniform(-0.001,0.001)
            self.measurement_changed.emit()  # Signal send there is a new value
        else:
            self._data = self._data + bytes(self._serial.readAll()).decode()  # Todo type mismatch

            pos = self._data.find('\r')
            if pos > 0:
                cleaned = self._data[0:pos]
                if len(self._data) > pos + 1:
                    self._data = self._data[pos + 1:]
                else:
                    self._data = ""
                self._measurement = float(cleaned)
                self.measurement_changed.emit()  # Signal send there is a new value

    @Slot()
    def _on_periodic_timeout(self):
        """ A measurement is started when the trigger is toggle from low to high. """
        if self._simulate:
            self._on_ready_read()
        else:
            self._serial.setDataTerminalReady(False)
            self._pulse_timer.start()

    @Slot()
    def _on_pulse_timeout(self):
        self._serial.setDataTerminalReady(True)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    import sys

    SIMULATE = True

    app = QApplication(sys.argv)

    micrometers = [Micrometer('AGCQj137C01', SIMULATE),
                   Micrometer('BBDDj137C01', SIMULATE)]

    QTimer.singleShot(5000, lambda: app.quit())

    sys.exit(app.exec())
