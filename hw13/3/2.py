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

        # Инициализируем списки для хранения лет и суммарных значений по каждому году
        years = []
        nums = []

        # Перебираем все столбцы, начиная со второго, чтобы извлечь данные по годам
        for i in df.columns[2:]:
            years.append(i)  # Добавляем год в список years
            nums.append(sum(df[i].values))  # Суммируем значения и добавляем их в список nums
            print(years, nums)  # Печатаем текущие значения списков years и nums для отладки

        # Создаем список номеров для оси X
        x = [i + 1 for i in range(len(nums))]

        # Создаем объект столбчатого графика и добавляем его на график
        bargraph = pg.BarGraphItem(x=x, height=nums, width=0.6, brush='r')
        plot.addItem(bargraph)

        # Устанавливаем график в качестве центрального виджета основного окна
        self.setCentralWidget(plot)

        # Настраиваем ось X для отображения меток с годами
        ax = plot.getAxis('bottom')
        ticks = [list(zip(x, years))]
        ax.setTicks(ticks)

# Запускаем приложение
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
