from urllib3.connectionpool import xrange


# Задание 1


def isEvenMy(value):
    x = value >> 1
    return value == (x << 1)


'''
Мой метод реализован с помощью побитового свдига вправо (деление на два) и влево (умножение на два). 
Таким образом мы можем разделить число на два, а затем умножить и сравнить с исходным значением.
Возможно, такой вариант будет работать быстрее, так как использует побитовый сдвиг, но вряд ли разница будет заметна 
в современных системах. Для реализации такого варианта необходимо понимать как работают побитовые операции, поэтому 
вариант с отстатком более простой и самый распространенный подход к этой задече. 
'''


# Задание 2


class FIFO_1:
    def __init__(self):
        self.items = []

    def __str__(self):
        return self.items

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


class FIFO_2:
    def __init__(self):
        self.items = []

    def __str__(self):
        return self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if self.items else None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


'''
Очередь можно реализовать через список, у которого уже есть подходящие методы для реализации нужного функционала. 
Оба варианта достаточно простые и похожи друг на друга. Они отличаются только стороной, с которой достаются элементы и 
куда кладутся. В таких вариантах, когда мы достаем элемент - он сразу удаляется, но, наверное, это верный подход,
потому что в следующий раз нам уже понадобится новый элемент. Можно реализовать очередь с переменными,
которые указывают на первый и последний элемент, но при наличии методов insert/append и pop, это кажется бессмысленным. 
'''


# Задание 3

def quicksort(arr):
    stack = [x for x in xrange(int(4 + len(arr) / 2))]
    last = 0
    stack[0] = 0
    stack[1] = len(arr) - 1
    while last >= 0:
        i = quicksort_pos(arr, stack[last], stack[last + 1])
        if i != stack[last + 1]:
            rl = i + 1
        else:
            rl = stack[last + 1]
        rr = stack[last + 1]
        ll = stack[last]
        if i != stack[last]:
            lr = i - 1
        else:
            lr = stack[last]
        last -= 2
        if rl != rr:
            last += 2
            stack[last] = rl
            stack[last + 1] = rr
        if ll != lr:
            last += 2
            stack[last] = ll
            stack[last + 1] = lr
    return


def quicksort_pos(arr, left, right):
    i = left
    j = right - 1
    while True:
        while arr[i] < arr[right]:
            i += 1
        while arr[j] > arr[right] and j > left:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[right], arr[i] = arr[i], arr[right]
    return i


'''
Я реализовала модифицированный вариант быстрой сортировки, который избавлен от рекурсии и выполняется быстрее, чем
обычная быстрая сортировка. Здесь мы храним границы наших интервалов. Такой алгоритм универсален для различных массивов
чисел. При этом быстрая сотировка является одной из самых быстрых сортировок. 
'''
