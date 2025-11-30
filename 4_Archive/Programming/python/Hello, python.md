#Keggle #Programming #Python #
```python
# a // b 몫
# a % b 나머지
# a ** b 지수
print(min(1,2,3))
print(max(1,2,3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

# Q1
pi = 3.14159 # approximate
diameter = 3
# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = radius ** 2 * pi
  
# Q2
a = [1, 2, 3]
b = [3, 2, 1]
c = a
a = b
b = c

# Q3a
#Add parentheses to the following expression so that it evaluates to 1.
5 - 3 // 2
(5-3)//2
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109
# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
total_candies = alice_candies + bob_candies + carol_candies

to_smash = total_candies % 3
```