#  Write a function that uses while, if and continue statements to
#   print all the even numbers between 0 and 50. 

def even_numbers():
     x=1
     while x<51:
         x+=1
         if x%2!=0:
            continue
         else:
            print(x)
           
    

even_numbers()
    

# Write a function that takes an integer argument and prints "Prime" if the number
# is prime, and "Not prime" if the number is not prime.

def prime_or_not_prime(num):
    if num < 1:
     print('not prime')
    else:
     for i in range(2, num):
        if num % i == 0:
            print('not prime')
            break
        else:
            print('prime')

prime_or_not_prime(20)

# Write a function that takes a list of integers as input
#  and prints the sum of all the even numbers in the list.

def even(list1):
   for i in list1:
      if i %2==0:
         print(i)
         
even([2,43,67,55,33,44,65,76])

# Write a function that takes any two integers as input, and prints 
# the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def divisible_by_three(num1,num2):
   if num1<=num2:
      start= num1
      end=num2
   else:
      start=num2
      end=num1
      sum=0
      for i in range(start, end+1):
         if i % 3 ==0:
            sum+=1
            print(sum)

divisible_by_three(num1=20,num2=87)

      
   
   
   
   




   