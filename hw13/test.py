from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
from math import sin, cos

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y_sin = [sin(i) for i in range(100)]  # 100 data points for sin
        self.y_cos = [cos(i) for i in range(100)]  # 100 data points for cos

        self.graphWidget.setBackground('w')

        pen_sin = pg.mkPen(color=(255, 0, 255))
        self.data_line_sin = self.graphWidget.plot(self.x, self.y_sin, pen=pen_sin)

        pen_cos = pg.mkPen(color=(0, 255, 0))
        self.data_line_cos = self.graphWidget.plot(self.x, self.y_cos, pen=pen_cos)

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        # print(self.x)
        new_x = self.x[-1] + 1
        self.x = self.x[1:]  # Remove the first element.
        self.x.append(new_x)

        self.y_sin = self.y_sin[1:]  # Remove the first element.
        self.y_sin.append(sin(new_x))  # Add a new value for sin.

        self.y_cos = self.y_cos[1:]  # Remove the first element.
        self.y_cos.append(cos(new_x))  # Add a new value for cos.

        self.data_line_sin.setData(self.x, self.y_sin)  # Update sin data.
        self.data_line_cos.setData(self.x, self.y_cos)  # Update cos data.


app = QApplication([])
w = MainWindow()
w.show()
app.exec()
