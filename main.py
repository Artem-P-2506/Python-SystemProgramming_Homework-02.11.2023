import Processes

if __name__ == "__main__":
    # Получаем масив потоков с нужной информацией
    processesDICT = Processes.getProcesses()
    # Получем среднее значение потребляемой памяти
    averageMemoryConsumption = Processes.getAverageMemoryConsumption(processesDICT)
    # Сортируем массив потоков по убыванию количества потребляемой потоком памяти
    processesDICT = Processes.sortArrayByAmountMemoryConsumption(processesDICT)
    # Получаем массив потоков с потреблением памяти больше среднего значения
    memoryBigProcessesDICT = Processes.getArrayOfBigMemoryProcesses(processesDICT, averageMemoryConsumption)
    # Сортируем массив потоков по убыванию количества потребляемой потоком памяти
    memoryBigProcessesDICT = Processes.sortArrayByAmountMemoryConsumption(memoryBigProcessesDICT)
    # Записываем полученый массив в JSON-файл
    Processes.logIntoFileJSON("processes.json", memoryBigProcessesDICT)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Д.З. -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # Закрываем все программы которые потребляют больше среднего значения ОЗУ
    Processes.closeProcessesWithMoreThanAverageAmountMemoryConsumption()





#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ПРОЦЕДУРНЫЙ СТИЛЬ -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# import psutil
# import json
#
# if __name__ == "__main__":
#     # Получаем масив потоков с нужной информацией
#     processesDICT = []
#     AverageMemoryConsumption = 0
#     for item in psutil.process_iter():
#         streamName = f"Name:\t{item.name()}"
#         memoryConsumption = int(item.memory_info().rss)
#         streamMemoryInfo = f"Memory:\t{memoryConsumption}"
#         processesDICT.append(f"{streamName}\t{streamMemoryInfo}")
#
#         # Получем среднее значение потребляемой памяти
#         AverageMemoryConsumption += memoryConsumption
#     AverageMemoryConsumption = AverageMemoryConsumption / len(processesDICT)
#
#     # Сортируем массив потоков по убыванию количества потребляемой потоком памяти
#     processesDICT = sorted(processesDICT, key=lambda x: int(x.split("\t")[3]), reverse=True)
#     for item in processesDICT:
#         print(item)
#     print("\nAverage memory consumption:\t", AverageMemoryConsumption)
#
#     # Логируем потоки с потреблением больше среднего в JSON-файл
#         # Получаем массив потоков с потреблением памяти больше среднего
#     memoryBigProcessesDICT = []
#     for item in processesDICT:
#         if int(item.split('\t')[3]) > AverageMemoryConsumption:
#             memoryBigProcessesDICT.append(item)
#
#     # Сортируем массив потоков по убыванию количества потребляемой потоком памяти
#     memoryBigProcessesDICT = sorted(memoryBigProcessesDICT, key=lambda x: int(x.split("\t")[3]), reverse=True)
#
#     # Записываем полученый массив в JSON-файл
#     fileName = "processes.json"
#     with open(fileName, 'w') as file:
#         memoryBigProcessesJSON = json.dumps(str(memoryBigProcessesDICT))
#         file.write(memoryBigProcessesJSON)
#     print(f"JSON-файл был успешно создан под названием '{fileName}'")