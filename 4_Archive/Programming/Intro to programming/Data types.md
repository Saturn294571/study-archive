#Intro_to_programming #Keggle #Programming #Python 
- ### Data types
	- int(실수)를 하면
		- 양수의 경우 그 수보다 낮은 가장 가까운 수로 돌아가고 ex) int(1.2) == 1
		- 음수의 경우 그 수보다 높은 가장 가까운 수로 돌아간다 ex) int(-9.22) == -9
```python
x = 14
print(x)
print(type(x))

nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))

almost_pi = 22/7
print(almost_pi)
print(type(almost_pi))

rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))

y_float = 1.
print(y_float)
print(type(y_float))

z_one = True
print(z_one)
print(type(z_one))

z_two = False
print(z_two)
print(type(z_two))

z_three = (1 < 2)
print(z_three)
print(type(z_three))

z_four = (5 < 3)
print(z_four)
print(type(z_four))

z_five = not z_four
print(z_five)
print(type(z_five))

w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))

shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))

my_number = "1.12321"
print(my_number)
print(type(my_number))

also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

new_string = "abc" + "def"
print(new_string)
print(type(new_string))

newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))

print(True * True)

def cost_of_project(engraving, solid_gold):
    is_solid_gold = solid_gold
    is_gold_plated = not solid_gold
    cost = is_gold_plated * 50 + is_gold_plated * 7 * len(engraving) + is_solid_gold * 100 + is_solid_gold * 10 * len(engraving)

    return cost
```