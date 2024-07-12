from PySide6.QtCharts import QChartView, QLineSeries, QXYSeries, QScatterSeries, QChart
from PySide6.QtGui import QColor, QPen, Qt


class XYGraph(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)


class MyChart(QChart):
    def __init__(self):
        super().__init__()
        self._series1 = QLineSeries(self)
        self._series1.setName("MM1")
        self._series1.setPen(QPen(Qt.red))
        self.addSeries(self._series1)

        self._series2 = QLineSeries(self)
        self._series2.setName("MM2")
        self._series2.setPen(QPen(Qt.blue))
        self.addSeries(self._series2)

        self.createDefaultAxes()
        self.legend().setVisible(True)
        self.axisX().setRange(20, 140)
        self.axisX().setTitleText("Temperature [℃]")
        self.axisY().setRange(0, 1000)
        self.axisY().setTitleText("Length [µm]")

    def clearAll(self):
        self._series1.clear()
        self._series2.clear()

    def addMeasurement1(self,x,y):
        self._series1.append(x,y*1000)

    def addMeasurement2(self,x,y):
        self._series2.append(x,y*1000)
