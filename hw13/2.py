# Импортируем необходимые модули из PySide6 и pyqtgraph
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pandas as pd

# Определяем класс основного окна приложения, наследуемый от QMainWindow
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Создаем виджет для графика и устанавливаем его в качестве центрального виджета
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Читаем данные из CSV-файла 'trees.csv'
        df = pd.read_csv("trees.csv")
        trees = df.iloc[:, 0].values.flatten().tolist()  # Извлекаем данные для деревьев
        grith = df.iloc[:, 1].values.flatten().tolist()  # Извлекаем данные об окружности
        height = df.iloc[:, 2].values.flatten().tolist()  # Извлекаем данные о высоте
        volume = df.iloc[:, 3].values.flatten().tolist()  # Извлекаем данные о объеме

        # Включаем сетку на графике
        self.graphWidget.showGrid(x=True, y=True)

        # Определяем ручки для рисования линий на графике с разными цветами и шириной
        g_pen = pg.mkPen(color=(255, 0, 0), width=8)  # Красная линия для окружности
        h_pen = pg.mkPen(color=(0, 255, 0), width=8)  # Зеленая линия для высоты
        v_pen = pg.mkPen(color=(0, 0, 255), width=8)  # Синяя линия для объема

        # Добавляем легенду к графику
        self.graphWidget.addLegend()

        # Добавляем линии на график для каждого набора данных
        self.graphWidget.plot(trees, grith, name="Grith", pen=g_pen, symbol='+', symbolSize=15, symbolBrush=('r'))
        self.graphWidget.plot(trees, height, name="Height", pen=h_pen, symbol='+', symbolSize=15, symbolBrush=('g'))
        self.graphWidget.plot(trees, volume, name="Volume", pen=v_pen, symbol='+', symbolSize=15, symbolBrush=('b'))

# Запускаем приложение
if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    app.exec()
