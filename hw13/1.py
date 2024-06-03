import sys
import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets

# Создаем приложение
app = QtWidgets.QApplication(sys.argv)

# Создаем окно для отображения графиков
win = pg.GraphicsLayoutWidget(show=True, title="Синус и Косинус")
win.resize(800, 600)
win.setWindowTitle('PyQtGraph: Синус и Косинус')

# Добавляем график в окно
plot = win.addPlot(title="Графики синуса и косинуса")

# Генерируем данные
x = np.linspace(0, 2 * np.pi, 100)  # 100 точек
y_sin = np.sin(x)
y_cos = np.cos(x)

# Рисуем графики
plot.plot(x, y_sin, pen='r', name="sin(x)")  # красная линия для синуса
plot.plot(x, y_cos, pen='b', name="cos(x)")  # синяя линия для косинуса

# Показываем окно
if __name__ == '__main__':
    QtWidgets.QApplication.instance().exec()
