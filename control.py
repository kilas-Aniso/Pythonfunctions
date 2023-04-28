def even_numbe():
  x = range(1,10)
  for i in x:
    if (i%2==0):
      print(i)

even_numbe()

def odd_numbers():
  y=range(1,10)
  for m in y:
    if(m%2!=0):
      print(m)

odd_numbers()


# if else statement
# if statement can be combined with an else statement, the code
# inside the if statement is executed if the if statement returns false

def divisible_by_five():
  z = range(1,100)
  for k in z:
    if (k%5==0):
      print(k)
    else:
      print(f"number {k} not divisble by 5")


divisible_by_five()

# Elif statement
# else if statement allows us to do multiple comparisons


def check_if_divisible():
    x = range(10,50)
    for i in x:
     if (i %2 ==0):
      print(f"{i} is divisible by 2")
     elif i %3==0:
       print(f"{i} is divisible by 3")
     elif i%5==0:
      print(f"{i} is divisible by 5")
     else:
      print(f"{i} is not divisible by 2,3,5")

check_if_divisible()


# combine if/elif with logical operators
# used to do multiple comparisons at the same time


def multiple_divisoble():
  x=range(10,25)
  for i in x :
    if i%2==0 and i%2==3:
       print(f"{i} is divisible by 2,3,")
    elif i%5==0:
      print(f"{i} is not divisible by 5")
    else:
     print(f"{i} is not divisible by 2,3,5")


multiple_divisoble()


# while statement
# while loop contionus to iterate as long as the given condition is true


def checkk():
  
  l=1
  while l<10:
   print(l)
   l+=1

# break stops a while loop even if the condition is true
def break_endorsement():
    x=1
    while x <10:
        print(x)
        if x==5:
          break
        x+=1






# continue skips the remainder of the current iteration and jumps 
# to the next iteration
def skips():
  
  x=1
  while x <10:
    x+=1
    if x%2!=0:
      continue
    print(x)

