#練習：You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
n = int(input("Please input stairs: "))

# 建立函數
def climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2        
# 爬到倒數第n梯時，其解法 = (n-1)再爬一梯 + (n-2) 再爬二梯
    s1, s2 = 1, 2
    for _ in range(n - 2):
        s1, s2 = s2, s1 + s2
    return s2

print("Total solution of clumbing is: " + str(climb(n)))
