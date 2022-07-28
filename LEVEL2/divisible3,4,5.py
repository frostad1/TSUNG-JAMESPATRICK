def divisible(num):
   result = [ ]
   for i in range(num):
       if i%3 == 0 and i%4 == 0 or i%5 == 0:
           result.append(i)
   return result
 
num = int (input('Enter your number: '))
result = divisible(num)
print(result)