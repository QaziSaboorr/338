import sys
import urllib.request, json 
import matplotlib.pyplot as plt
import timeit
import random
sys.setrecursionlimit(9000000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def func1improved(arr, low, high):
    if low < high:
        pi = func2improved(arr, low, high)
        func1improved(arr, low, pi-1)
        func1improved(arr, pi + 1, high)
def func2improved(array, start, end):
    pivot_index = random.randint(start, end)
    array[start], array[pivot_index] = array[pivot_index], array[start]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with urllib.request.urlopen("https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json") as url:
    data = json.load(url)

time = []
timeimproved = []
array = []
for x in data:
    lowa = x.index(min(x))
    maxa = x.index(max(x))
    time.append(timeit.repeat(lambda: func1(x,lowa,maxa),number=1,repeat=1))
    array.append(len(x))

for x in data:
    lowa = x.index(min(x))
    maxa = x.index(max(x))
    timeimproved.append(timeit.repeat(lambda: func1improved(x,lowa,maxa),number=1,repeat=1))

print(timeimproved)
plt.plot(array,time,label = 'original')
plt.plot(array,timeimproved, label = 'improved')
plt.xlabel('array size (n)')
plt.ylabel('Time function took (s)')
plt.title('Plot of time taken for quicksort algorithm')
plt.legend()
plt.show()