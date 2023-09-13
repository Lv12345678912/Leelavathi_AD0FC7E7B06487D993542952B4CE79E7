
def fact_rec(n):
   if n==1:
     return 1
   else:
     return n*fact(n-1)
number=2
res=fact_rec(number)
  print ("the factorial of{}is{}.". format (number,rec))