import os
from datetime import datetime
from typing import List

from PySide6.QtCore import QObject, QTimer, Slot

from .micrometer import Micrometer
from .temperature_card import TemperatureCard


# WIP pseudocode

class Logger(QObject):

    def __init__(self, temperature_card: TemperatureCard,
                 micrometers: List[Micrometer], parent=None):
        super().__init__(parent)

        self._temperature_card = temperature_card
        self._micrometers = micrometers
        self._logging_folder = os.getcwd()
        self._filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"

        self._timer = QTimer()
        self._timer.setInterval(1000)  # default logging interval
        self._timer.timeout.connect(self._on_log)

    def set_logging_interval(self, interval: float):
        self._timer.setInterval(int(interval * 1000))

    def set_logging_folder(self, logging_folder: str):
        self._logging_folder = logging_folder

    def set_active(self, active):
        if active:
            self._filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
            with open(self._filename, "at") as fp:
                fp.write(f"DateTime\t")  # TODO log formatting
                for idx in range(8):
                    fp.write(f"Temperatuur {1 + idx}\t")  # TODO log formatting
                for idx in range(2):
                    fp.write(f"Lengte {1 + idx}\t")  # TODO log formatting
                fp.write(f"\n")  # TODO log formatting
            self._timer.start()
        else:
            self._timer.stop()

    @Slot()
    def _on_log(self):
        temperatures = self._temperature_card.get_temperatures()

        lengths = []
        for micrometer in self._micrometers:
            lengths.append(micrometer.get_measurement())  # Triggering by GUI, TODO autonomous triggering?

        filepath = os.path.join(self._logging_folder, self._filename)
        with open(filepath, "at") as fp:
            fp.write(f"{datetime.now().isoformat()}\t")  # TODO log formatting
            for idx in range(8):
                fp.write(f"{temperatures[idx]}\t")  # TODO log formatting
            for idx in range(2):
                fp.write(f"{lengths[idx]}\t")  # TODO log formatting
            fp.write(f"\n")  # TODO log formatting

        """
        import datetime
        datetime.datetime.now().isoformat()
        >>> 2020-03-20T14:28:23.382748
        """
