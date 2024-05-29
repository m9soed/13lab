from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        plot = pg.plot()

        df = pd.read_csv('hurricanes.csv')

        month = df.iloc[:, 0].values.flatten().tolist()
        value2007 = df.iloc[:, 4].values.flatten().tolist()
        x = [i + 1 for i in range(len(value2007))]
        bargraph = pg.BarGraphItem(x=x, height=value2007, width=0.6, brush='r')
        plot.addItem(bargraph)
        self.setCentralWidget(plot)
        ax = plot.getAxis('bottom')
        ticks = [list(zip(x, month))]
        ax.setTicks(ticks)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
