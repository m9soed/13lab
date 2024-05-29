from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        plot = pg.plot()

        df = pd.read_csv('hurricanes.csv')
        years = []
        nums = []
        for i in df.columns[2:]:
            years.append(i)
            nums.append(sum(df[i].values))
            print(years, nums)
        x = [i+1 for i in range(len(nums))]
        bargraph = pg.BarGraphItem(x=x, height=nums, width=0.6, brush ='r')
        plot.addItem(bargraph)
        self.setCentralWidget(plot)
        ax = plot.getAxis('bottom')
        ticks = [list(zip(x, years))]
        ax.setTicks(ticks)

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()