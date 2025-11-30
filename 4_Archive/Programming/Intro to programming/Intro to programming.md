#Keggle #Programming #Python #Intro_to_programming
- ### Arithmetic and variables
	- math.ceil(~)은 올림을 해준다
	- math.floor(~)은 내림을 해준다
	- 문자열 * 정수 는 문자열을 정수만큼 반복하지만, 문자열 * 실수 는 오류가 난다 1.0 또한 오류가 난다
	
- ### Data types
	- int(실수)를 하면
		- 양수의 경우 그 수보다 낮은 가장 가까운 수로 돌아가고 ex) int(1.2) == 1
		- 음수의 경우 그 수보다 높은 가장 가까운 수로 돌아간다 ex) int(-9.22) == -9

- ### Condition and conditional statement
    - True를 곱하거나 더할 땐 숫자 1로 취급된다 마찬가지로 False를 곱하거나 더할 땐 0으로 취급된다
        - 단, 문자열 * False는 ""으로 취급된다
    - if ~ elif 문을 써서 많은 수의 경우의 수를 취급할 땐 가장 범위가 큰 것부터 줄여나가면 된다

- ### Intro to lists    
    - 리스트에 슬라이싱을 통해 접근할 수 있다
		```python
my_list = [1,2,3,4,5]

# my_list[시작(포함O):끝(포함X)]
my_list[2:4]

# 마지막 3개의 원소에 접근하고 싶다면
my_list[-3:]

# 처음 2개의 원소에 접근하고 싶다면 my_list[:m]
my_list[:2]

# .remove(), .append()를 통해 원소를 추가/삭제할 수 있다
my_list.remove(1)
my_list.append(6)

# max(my_list), min(my_list), sum(my_list)를 통해 리스트의 최대, 최소 합계를 구할 수 있다
max(my_list)
min(my_list)
sum(my_list)
		```
        
    - 문자열이 있을 때 '문자열'.split("구분하고자 하는 문자")를 통해 문자열을 배열로 각각 구분할 수 있다.
		```python
date = 2024.09.03
formated_date = date.split(".")
# [2024,09,03]
```
    - 리스트 생성
        - 한 리스트를 가지고 특정 조건에 부합하는 리스트를 생성할 수 있다
        - (새 리스트) = (조건) for (변수) in (기존 리스트)
```python
test_ratings = [1,2,3,4,5]
test_liked = [i>=4 for i in test_ratings]
# [False,False, False, True, True]
```

