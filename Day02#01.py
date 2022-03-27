#練習：請將字串當中的出現的 not … at all 換成 good ， 中間的「…」代表的是任意字串或沒有內容 。
s = input()
# s1 = "This company is not poor at all."
# s2 = "I'm not at all happy about it."

start_index = s.find('not')
end_index = s.find('at all')
if start_index != (-1) and end_index != (-1): 
  s_re = s.replace(s[start_index:end_index+6],'good')
  print("result: " + s_re)
else:
  print("result: " + s)
