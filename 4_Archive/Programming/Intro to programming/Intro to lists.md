#Intro_to_programming #Keggle #Programming #Python 
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
