def my_country(country = "Rwanda"):
    print(f"Hello from{country}")

def greet(*names):
    for name in names:
        print(f"Hello {name}")

def my_family(*namess):
    for nam in namess:
      print(f"I love {nam}")
    
def sum (*numbers):
    answer = 0
    for num in numbers:
        answer+=num

    return answer
# * pass any parameter...it stores it in the form of a list
def multiply(*numberss):
    product=1
    for numb in numberss:
        product*=numb

    return product

# ** accepst any number of keyword arguments

def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    
    # In the arguments module add these two functions;
# A function named concatenate_args that takes any number of string
# arguments in positional arguments format and concatenates them
#  into a single string
def concatenate_args(*pupils):
    result = ""
    for pupil in pupils:
        result+=pupil   
    return result





# A function named concatenate_kwargs that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string
    
def concatenate_kwargs(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += str(key,value)
    return result


x = range(20,30)
for i in x:
    print(i*3)