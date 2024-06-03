# Импортируем необходимые модули из PySide6 и pyqtgraph
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import pandas as pd

# Определяем класс основного окна приложения, наследуемый от QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Создаем объект графика
        plot = pg.plot()

        # Читаем данные из CSV-файла 'hurricanes.csv'
        df = pd.read_csv('hurricanes.csv')

        # Извлекаем данные: месяцы и значения за 2007 год
        month = df.iloc[:, 0].values.flatten().tolist()
        value2007 = df.iloc[:, 4].values.flatten().tolist()
        x = [i + 1 for i in range(len(value2007))]  # Создаем список номеров месяцев

        # Создаем объект столбчатого графика и добавляем его на график
        bargraph = pg.BarGraphItem(x=x, height=value2007, width=0.6, brush='r')
        plot.addItem(bargraph)

        # Устанавливаем график в качестве центрального виджета основного окна
        self.setCentralWidget(plot)

        # Настраиваем ось X для отображения меток с месяцами
        ax = plot.getAxis('bottom')
        ticks = [list(zip(x, month))]
        ax.setTicks(ticks)

# Запускаем приложение
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
