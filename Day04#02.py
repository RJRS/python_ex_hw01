# 1. 讓使用可以輸入一個字串 S
# 2. 去計算字串中每個字母所出現的位置並且存入一個 list
# 3. 將出現字母當作 key、出現位置所組成的 list 組裝成一個 dict 後印出
s = 'Here are UPPERCASE and lowercase chars.'
d = {}
  
for i,j in enumerate(s):
    if j not in d:
        d[j]= [i+1]
    else:
        d[j].append(i)

print(d)
