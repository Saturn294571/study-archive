#Intro_to_programming #Keggle #Programming #Python 
```python
def add_3(input_var):
    outpur_var = input_var + 3
    return outpur_var

new_num = add_3(10)
print(new_num)

def get_pay(num_hours):
    pay_pretax = num_hours * 15
    pay_aftertax = pay_pretax * (1-0.12)
    return pay_aftertax

pay_fulltime = get_pay(40)
print(pay_fulltime)

pay_parttime = get_pay(32)
print(pay_parttime)

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    pay_pretax = num_hours * hourly_wage
    pay_aftertax = pay_pretax * (1-tax_bracket)
    return pay_aftertax

higher_pay_aftertax = get_pay_with_more_inputs(40, 24, 0.22)
print(higher_pay_aftertax)

same_pay_fulltime = get_pay_with_more_inputs(40,15,0.12)
print(same_pay_fulltime)

def print_hello():
    print("Hello, you!")
    print("Good morning!")
  
print_hello()
```