# 입력: 리스트 a, 출력: 정렬된 새 리스트
def find_ins_idx(r, v): # 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
    
    for i in range(0, len(r)): # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    
        if v < r[i]: # v 값보다 i번 위치에 있는 자료 값이 크면 -> v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
            return i
    
    return len(r) # 적절한 위치를 못 찾았을 때는 -> v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입

def ins_sort1(a):
    result = []  # 새 리스트를 만들어 정렬된 값을 저장
    
    while a:     # 기존 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0) # 기존 리스트에서 한 개를 꺼냄
        ins_idx = find_ins_idx(result, value)  # 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value)  # 찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)

    return result

d = [2, 4, 5, 1, 3]
print(ins_sort1(d))

# --------------------------------------------
# 삽입 정렬 입력: 리스트 a 출력: 없음(입력으로 주어진 a가 정렬됨)

def ins_sort2(a):
    n = len(a)
    
    for i in range(1, n):  # 1부터 n-1까지
        key = a[i] # i번 위치의 값을 key로 저장
        j = i - 1 # j를 i 바로 왼쪽 위치로 저장
        
        while j >= 0 and a[j] > key: # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
            a[j + 1] = a[j]  # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1

        a[j + 1] = key  # 찾은 삽입 위치에 key를 저장
        # print(a)

d = [2, 4, 5, 1, 3]
ins_sort2(d)
print(d)

aaa = [1,2]
aaa[0],aaa[1] = aaa[1],aaa[0]
print(aaa)

def ins(array) :
    for i in range(0,len(array)) :
        while (i >= 0 and i+1) < len(array) and array[i] > array[i+1] :
            array[i],array[i+1] = array[i+1],array[i]
            i += -1
    return array

print('---------------',ins([1,4,3,2]))

# ---------------------------------------------
def shell_sort(a):
    h = 4       # 3x+1 간격: 1, 4, 13, 40, 121,... 중에서 4 와 1만 사용
    while h >= 1:        
        for i in range(h, len(a)):  # h-정렬 수행
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
            print(a)
        h //= 3
        print(h)
        
# a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
a = [7,2,6,3,5,4,1]

print('정렬 전:\t', end='')
print(a)

shell_sort(a)
print('정렬 후:\t', end='')
print(a)