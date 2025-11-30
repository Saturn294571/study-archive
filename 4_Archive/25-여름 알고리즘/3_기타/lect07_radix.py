def lsd_sort(a) :
    WIDTH = 3 # 스트링 문자 수
    N = len(a) # 입력 크기
    R = 128 # radix 크기
    temp = [None] * N

    for d in reversed(range(WIDTH)) :
        # d번째 문자 처리, d=2,1,0 (↑)
        count = [0]*(R+1)

        for i in range(N) : # 빈도수 계산
            count[ord(a[i][d])+1] += 1 
        # ord()인자 unicode값 반환 (↑)

        for j in range(1,R) : 
            # 빈도수 누적 계산 (↑)
            count[j] += count[j-1]

        for k in range(N) : # data 복사
            p = ord(a[k][d])
            temp[count[p]] = a[k]
            count[p] += 1
        
        for l in range(N) : # t를 a로 복사
            a[l] = temp[l]
        
        print(f'{d}번째 문자 : ', end='')
        for x in a : print(x,end=' ')
        print()

a = ['INC', 'SFO', 'LAX', 'FRA','SIN', 'ROM', 'HKG', 'TLV', 
     'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']

print('정렬 전 : ',end='')
for x in a : print(x,end=' ')
print(); lsd_sort(a)
print('----------------')

from math import inf