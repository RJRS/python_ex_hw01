#練習：請根據使用者的輸入的字串，產生不重複的排列組合。
# 將輸入的字串轉為set，確定無重複字元，再轉成list
str_input = list(set(input("Please input: ")))

# 使用轉位的方式
def f(str, i, j):
  if i == j:
    print(''.join(str), end=" ")
    return 
  for a in range (i, j + 1):
    str[i], str[a] = str[a], str[i] 
    f(str, i + 1, j)
    str[i], str[a] = str[a], str[i] 
    
f(str_input, 0, len(str_input) - 1)
