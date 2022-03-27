#練習：map(…) function 是 Python 中常用的一種 functional method，可以對列表內的所有元素進行同一個 function 操作。 接下來，請你試試看在 Python 中實現 map(F, L) 方法（而非直接使用內建的 map(…)）。
def add1(n):
  return n + 1
  
def isPrime(n):
  if n > 1:
    for i in range (2, n//2 +1):
      if (n % i) == 0:
        return False
    else:
      return True
  else:
    return False

def f(L, F):
  m = []
  for i in L:
    result = F(i)
    m.append(result)
  return m

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]

L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]
