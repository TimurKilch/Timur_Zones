import numpy
import numpy as np
from map_io import from_file

numpy_arr = np.load('zones/K36_target.npy')
numpy_arr = np.reshape(numpy_arr, (64, 64)) #Массив npy
x = from_file('zones/K36.rmap').data
rmap_arr = x.reshape((x.shape[0] * x.shape[1]), x.shape[2]) #Массив rmap
c = np.array(numpy_arr) - np.array(rmap_arr) # Результат разница между массивами
unique, counts = numpy.unique(c, return_counts=True)
uniqueDict = dict(zip(unique, counts))

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
    return accuracy, er2


def count_1(all, current, error1, error2):
    accuracy = (current / all) * 100
    er1 = (error1 / (all - current)) * 100
    er2 = (error2 / (all - current)) * 100
    return accuracy, er1, er2


def count_2(all, current, error1, error2):
    accuracy = (current / all) * 100
    er1 = (error1 / (all - current)) * 100
    er2 = (error2 / (all - current)) * 100
    return accuracy, er1, er2


def count_3(all, current, error1):
    accuracy = (current / all) * 100
    er2 = (error1 / (all - current)) * 100
    return accuracy, er2


for i in range(len(numpy_arr)):
    for j in range(len(numpy_arr)):
        if numpy_arr[i][j] - rmap_arr[i][j] < 0:
            err_all_1 += 1
        elif numpy_arr[i][j] - rmap_arr[i][j] > 0:
            err_all_2 += 1
        elif numpy_arr[i][j] == rmap_arr[i][j]:
            curr_all += 1


def count_all(all,current,error1,error2):
    accuracy = (current / all) * 100
    er1 = (error1 / (all - current)) * 100
    er2 = (error2 / (all - current)) * 100
    return accuracy, er1, er2





#TODO: все эти метрики в таблицу, НЛ вывод, по дизайну че то по красивее сделать, ГГВП









#zero = uniqueDict[0]
#sum = c.size
#minus = 0
#plus = 0
#for key, value in uniqueDict.items():
#    if key < 0:
#        minus += value
#    if key > 0:
#        plus += value
#
#print(f'Accuracy ={zero/sum}')
#print(f'Ошибки 1го рода : {minus/ sum}')
#print(f'Ошибки 2го рода : {plus/ sum}')
