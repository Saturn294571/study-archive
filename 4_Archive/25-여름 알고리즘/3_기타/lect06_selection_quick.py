def selectionSort1(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = arr[0]
    smallest_index = 0
    
    for j in range(1, len(arr)):
      
      if arr[j] < smallest:
        smallest = arr[j]
        smallest_index = j
    
    newArr.append(arr.pop(smallest_index))
  return newArr

print(selectionSort1([5,3,6,2,10]),'\n-----------------------------------------') 

# ---------------------------------------

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
      if arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i
    
    return smallest_index

def selectionSort2(arr):
  newArr = []
  
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
  
  return newArr

print(selectionSort2([5,3,6,2,10]),'\n-----------------------------------------')

# ----------------------------------------

def quicksort1(array):
  
  if len(array) < 2: # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else: # recursive case
    pivot = array[0] # sub-array of all the elements less than the pivot
    less = []

    for i in array[1:]:
        if i <= pivot:
            less.append(i)
            # sub-array of all the elements greater than the pivot
    
    greater = [i for i in array[1:] if i > pivot]
    return quicksort1(less) + [pivot] + quicksort1(greater)

print(quicksort1([10, 5, 2, 3]),'\n-----------------------------------------')

# -----------------------------------------

# 퀵 정렬; 입력: 리스트 a, 출력: 없음(입력으로 주어진 a가 정렬됨), 리스트 a의 어디부터(start) 어디까지(end)가 정렬 대상인지 범위를 지정하여 정렬하는 재귀 호출 함수

def quick_sort_sub(a, start, end):
    
    if end - start <= 0: # 종료 조건: 정렬 대상이 1개 이하면 정렬할 필요 없음
        return
    
    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤; [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = a[end]    # 편의상 리스트의 마지막 값을 기준 값으로 정합
    # print(a[end])
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            # print(a[i], a[j])
            a[i], a[j] = a[j], a[i]
            # print(a[i], a[j])
            i += 1

    a[i], a[end] = a[end], a[i]
    # 재귀 호출 부분
    quick_sort_sub(a, start, i - 1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i + 1, end)   # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬
 
# 리스트 전체(0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def quick_sort2(a):
    quick_sort_sub(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

quick_sort2(d)

print(d)
