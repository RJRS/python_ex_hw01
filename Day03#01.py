#練習：Self-Dividing Number（自除數）
a, b = int(input("Enter Number A: ")), int(input("Enter Number B: "))

# 函式，將數字轉成字串，再取出元素相除
def self_div(num):
  for c in str(num):
    if c  == '0' or num % int(c) > 0:
      return False
  return True

# 將符合的元素建立成 list
num_list = []
for num in range(a, b+1):
  if self_div(num):
    num_list.append(num)

# 建議 list 進行二二相減，取出最大值，取得index值
dif_list = []
for i in range(len(num_list)):
  if i < len(num_list) - 1:
    dif = num_list[i+1] - num_list[i]
    dif_list.append(dif)
    max_dif = max(dif_list)
    index_dif = dif_list.index(max_dif)
print( (num_list[index_dif], num_list[index_dif+1]) )
