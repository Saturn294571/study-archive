#Intro_to_programming #Keggle #Programming #Python 
### Condition and conditional statement
- True를 곱하거나 더할 땐 숫자 1로 취급된다 마찬가지로 False를 곱하거나 더할 땐 0으로 취급된다
	- 단, 문자열 * False는 ""으로 취급된다
- if ~ elif 문을 써서 많은 수의 경우의 수를 취급할 땐 가장 범위가 큰 것부터 줄여나가면 된다
```python
print(2 > 3)

var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))
print(evaluate_temp(39))

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)
```