```python
help(round)
'''
help() displays two things:
    the header of that function round(number, ndigits=None). In this case, this tells us that round() takes an argument we can describe as number. Additionally, we can optionally give a separate argument which could be described as ndigits.
    A brief English description of what the function does.
주의점 : 함수에 값을 넣지 않은 이름만 적어서 내라
'''

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)
# 여러줄을 함수 인자로 넣을 땐 ,로 끊어준다
  
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
# """~"""나 '''~'''와 같은 docstring은 함수나 기능을 설명할 때 좋다 또한 help()를 사용할 때도 아무것도 없는 상태


# 인자의 기본값
print(1,2,3,sep=' < ')
# >>> 1 < 2 < 3
print(1,2,3)
# >>> 1 2 3

def greet(who="Colin"):
    print("Hello, ", who)

greet()
greet(who="Keggle")
# 이 상황에선 인자의 이름(Keggle)을 굳이 지정할 필요는 없다
greet("world")
# >>> Hello, Colin
# >>> Hello, Keggle
# >>> Hello, world
  

# 함수에 적용되는 함수들
def add_42(x):
    return x + 42

def call_fn(fn, arg):
    return fn(arg)
    
def call_fn_2_times(fn,arg):
    return fn(fn(arg))

print(
    add_42(10),
    call_fn(add_42,10),
    call_fn_2_times(add_42,10),
    sep="\n",
      )

# 함수 내에서 key="(함수)" 인자를 사용하면 함수에서 나온 값을 함수에 또 적용한다
def square_2_and_mod_2(x):
    """Returns the remainder of 2 after dividing by 2 and square 2"""
    return (x ** 2) % 2

print(
    "which is biggest?",
    max(2,3,5),
    "which is biggest after square 2 and modoulo 2?",
    max(2,3,5, key=square_2_and_mod_2),
    sep="\n",
)

# Q1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places.
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(num, 2)
  
print(round_to_two_places(3.141))

# Q2
# round의 2번째 인자를 통해 소수점 이하의 버림 뿐만이 아니라 n번째 자리수의 버림도 가능하다
print(round(1234.5678, -2))
# >>> 1200.0

#Q3
def to_smash(total_candies, num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    >>> to_smash(91)
    1
    """
    return total_candies % num_friends

# total_candies(10), total_candies(42,7) 둘 다 가능하다
```