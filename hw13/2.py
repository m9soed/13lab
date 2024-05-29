from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pandas as pd

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        df = pd.read_csv("trees.csv")
        trees = df.iloc[:,0].values.flatten().tolist()
        grith = df.iloc[:,1].values.flatten().tolist()
        height = df.iloc[:,2].values.flatten().tolist()
        volume = df.iloc[:,3].values.flatten().tolist()

        self.graphWidget.showGrid(x=True, y=True)

        g_pen = pg.mkPen(color=(255, 0, 0), width=8)
        h_pen = pg.mkPen(color=(0, 255, 0), width=8)
        v_pen = pg.mkPen(color=(0, 0, 255), width=8)

        self.graphWidget.addLegend()

        self.graphWidget.plot(trees, grith, name="Greeth",  pen=g_pen, symbol='+', symbolSize=15, symbolBrush=('r'))
        self.graphWidget.plot(trees, height, name="Height",  pen=h_pen, symbol='+', symbolSize=15, symbolBrush=('g'))
        self.graphWidget.plot(trees, volume, name="Volume",  pen=v_pen, symbol='+', symbolSize=15, symbolBrush=('b'))


        
if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec()
