import sys
import os
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import mainWindow
from draw_map import draw
import matplotlib.pyplot as plt
from map_io import from_file

class MainApp(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.openButton.clicked.connect(self.open_image)
        self.closeButton.clicked.connect(self.close_image)
        self.numpyWindow.setScaledContents(True)
        self.rmapWindow.setScaledContents(True)

    def open_image(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.curr_dir = directory

        for img in os.listdir(directory):
            if os.path.basename(img).split('.')[1] == 'rmap':
                draw(f'{directory}/{img}', f'{directory}/')
                rmap = from_file(f'{directory}/{img}')
            if os.path.basename(img).split('.')[1] == 'npy':
                numpy_arr = np.load(f'{directory}/{img}')
                numpy_arr = np.reshape(numpy_arr, (64, 64))
                plt.imsave(f'{directory}/numpy.png', numpy_arr)
        if directory:
            self.directory.setText(os.path.basename(directory))
            for file in os.listdir(directory):
                if os.path.basename(file).split('.')[0] == 'numpy' and os.path.basename(file).split('.')[1] == 'png':
                    pixmap = QPixmap(f'{directory}/{file}')
                    self.numpyWindow.setPixmap(pixmap)

                if os.path.basename(file).split('.')[1] == 'png' and os.path.basename(file).split('.')[0] != 'numpy':
                    pixmap = QPixmap(f'{directory}/{file}')
                    self.rmapWindow.setPixmap(pixmap)

        x = rmap.data
        rmap_arr = x.reshape((x.shape[0] * x.shape[1]), x.shape[2])

        all_0 = 0
        curr_0 = 0
        err_0_2 = 0

        all_1 = 0
        curr_1 = 0
        err_1_1 = 0
        err_1_2 = 0

        all_2 = 0
        curr_2 = 0
        err_2_1 = 0
        err_2_2 = 0

        all_3 = 0
        curr_3 = 0
        err_3_1 = 0

        err_all_1 = 0
        err_all_2 = 0
        curr_all = 0

        for i in range(len(numpy_arr)):
            for j in range(len(numpy_arr)):
                if numpy_arr[i][j] == 0:
                    if numpy_arr[i][j] - rmap_arr[i][j] < 0:
                        err_0_2 += 1
                    else:
                        curr_0 += 1
                    all_0 += 1
                elif numpy_arr[i][j] == 1:
                    if numpy_arr[i][j] - rmap_arr[i][j] < 0:
                        err_1_1 += 1
                    elif numpy_arr[i][j] - rmap_arr[i][j] > 0:
                        err_1_2 += 1
                    else:
                        curr_1 += 1
                    all_1 += 1
                elif numpy_arr[i][j] == 2:
                    if numpy_arr[i][j] - rmap_arr[i][j] < 0:
                        err_2_1 += 1
                    elif numpy_arr[i][j] - rmap_arr[i][j] > 0:
                        err_2_2 += 1
                    else:
                        curr_2 += 1
                    all_2 += 1
                elif numpy_arr[i][j] == 3:
                    if numpy_arr[i][j] - rmap_arr[i][j] > 0:
                        err_3_1 += 1
                    else:
                        curr_3 += 1
                    all_3 += 1

        def count_0(all, current, error2):
            accuracy = (current / all) * 100
            er2 = (error2 / (all - current)) * 100

            accuracy = float('{:.1f}'.format(accuracy))
            er2 = float('{:.1f}'.format(er2))

            return accuracy, 0, er2

        def count_1(all, current, error1, error2):
            accuracy = (current / all) * 100
            er1 = (error1 / (all - current)) * 100
            er2 = (error2 / (all - current)) * 100

            accuracy = float('{:.1f}'.format(accuracy))
            er1 = float('{:.1f}'.format(er1))
            er2 = float('{:.1f}'.format(er2))

            return accuracy, er1, er2

        def count_2(all, current, error1, error2):
            accuracy = (current / all) * 100
            er1 = (error1 / (all - current)) * 100
            er2 = (error2 / (all - current)) * 100

            accuracy = float('{:.1f}'.format(accuracy))
            er1 = float('{:.1f}'.format(er1))
            er2 = float('{:.1f}'.format(er2))

            return accuracy, er1, er2

        def count_3(all, current, error1):
            accuracy = (current / all) * 100
            er1 = (error1 / (all - current)) * 100

            accuracy = float('{:.1f}'.format(accuracy))
            er1 = float('{:.1f}'.format(er1))

            return accuracy, er1, 0

        for i in range(len(numpy_arr)):
            for j in range(len(numpy_arr)):
                if numpy_arr[i][j] - rmap_arr[i][j] < 0:
                    err_all_1 += 1
                elif numpy_arr[i][j] - rmap_arr[i][j] > 0:
                    err_all_2 += 1
                elif numpy_arr[i][j] == rmap_arr[i][j]:
                    curr_all += 1

        def count_all(all, current, error1, error2):
            accuracy = (current / all) * 100
            er1 = (error1 / (all - current)) * 100
            er2 = (error2 / (all - current)) * 100

            accuracy = float('{:.1f}'.format(accuracy))
            er1 = float('{:.1f}'.format(er1))
            er2 = float('{:.1f}'.format(er2))

            return accuracy, er1, er2

        tableDict = { 0 : count_all(numpy_arr.size, curr_all, err_all_1, err_all_2),
                      1 : count_0(all_0, curr_0, err_0_2),
                      2 : count_1(all_1, curr_1, err_1_1, err_1_2),
                      3 : count_2(all_2, curr_2, err_2_1, err_2_2),
                      4 : count_3(all_3, curr_3, err_3_1)}

        for col in range(5):
            for row in range(3):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(tableDict[col][row])))


    def close_image(self):
        self.numpyWindow.clear()
        self.rmapWindow.clear()
        for img in os.listdir(self.curr_dir):
            if os.path.basename(img).split('.')[1] == 'png':
                os.remove(f'{self.curr_dir}/{img}')

        for col in range(5):
            for row in range(3):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(''))

        self.directory.setText("")

        #TODO Очистку таблицы без удаления названия колонок,
        # дизайн адекватный сделать, добавить НЛ куда нибудь,
        # сделать кучу Rmap и выбрать 4-5 хороших снимков



def main():
    if sys.version_info[0:2] != (3, 9):
        raise Exception('Requires python 3.9')

    app = QtWidgets.QApplication(sys.argv)

    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
