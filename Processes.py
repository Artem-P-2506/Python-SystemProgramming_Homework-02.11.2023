import psutil
import json

def getProcesses(): # Получаем масив потоков с нужной информацией
    processesDICT = []
    for item in psutil.process_iter():
        streamName = f"Name:\t{item.name()}"
        streamMemoryInfo = f"Memory:\t{item.memory_info().rss}"
        processesDICT.append(f"{streamName}\t{streamMemoryInfo}")
    return processesDICT

def getAverageMemoryConsumption(processesDICT): # Получем среднее значение потребляемой памяти
    averageMemoryConsumption = 0
    for item in processesDICT:
        averageMemoryConsumption += int(item.split('\t')[3])
        averageMemoryConsumption = averageMemoryConsumption / len(processesDICT)
        return averageMemoryConsumption

def sortArrayByAmountMemoryConsumption(processesDICT): # Сортируем массив потоков по убыванию количества потребляемой потоком памяти
    sortedProcessesDICT = sorted(processesDICT, key=lambda x: int(x.split("\t")[3]), reverse=True)
    return sortedProcessesDICT

def getArrayOfBigMemoryProcesses(processesDICT, averageMemoryConsumption): # Получаем массив потоков с потреблением памяти больше среднего значения
    memoryBigProcessesDICT = []
    for item in processesDICT:
        if int(item.split('\t')[3]) > averageMemoryConsumption:
            memoryBigProcessesDICT.append(item)
    return memoryBigProcessesDICT

def logIntoFileJSON(fileName, ProcessesDICT): # Записываем полученый массив в JSON-файл
    with open(fileName, 'w') as file:
        memoryBigProcessesJSON = json.dumps(str(ProcessesDICT))
        file.write(memoryBigProcessesJSON)
    print(f"JSON-файл был успешно создан под названием '{fileName}'")

def closeProcessesWithMoreThanAverageAmountMemoryConsumption(): # Закрываем все программы которые потребляют больше среднего значения ОЗУ
    averageMemoryConsumption = getAverageMemoryConsumption(getProcesses())
    for item in psutil.process_iter():
        if item.memory_info().rss > averageMemoryConsumption:
            print(f"Program '{item.name()}' was klosed!")
            item.kill()